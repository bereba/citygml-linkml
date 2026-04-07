#!/usr/bin/env python3
"""
Convert OGC CityGML 3.0 XMI/UML to LinkML YAML schema.

Usage:
    python convert_xmi_to_linkml.py

Output:
    citygml_schema.yaml
"""

import glob
import xml.etree.ElementTree as ET
import subprocess
import os
import tempfile
from dataclasses import dataclass, field

from linkml_runtime.utils.schema_builder import SchemaBuilder
from linkml_runtime.linkml_model.meta import (
    ClassDefinition,
    SlotDefinition,
    EnumDefinition,
    PermissibleValue,
)
from linkml_runtime.dumpers import yaml_dumper

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

XMI_FILE = "OGC CityGML 3.0/Integrated/CityGML_3.0.xml"
OUTPUT_FILE = "citygml_schema.yaml"
SCHEMA_ID = "https://www.ogc.org/standards/citygml"
SCHEMA_NAME = "citygml"
XSD_DIR = "citygml-3_0_0_xsd"

XMI_NS = "http://schema.omg.org/spec/XMI/2.1"
UML_NS = "http://schema.omg.org/spec/UML/2.1"
XMI_ID = f"{{{XMI_NS}}}id"
XMI_TYPE = f"{{{XMI_NS}}}type"
XMI_IDREF = f"{{{XMI_NS}}}idref"

# Mapping from UML/EAStub primitive type names to LinkML built-in types
PRIMITIVE_TYPE_MAP: dict[str, str] = {
    "Boolean": "boolean",
    "Integer": "integer",
    "Real": "float",
    "Decimal": "float",
    "Number": "float",
    "CharacterString": "string",
    "Character": "string",
    "ScopedName": "string",
    "GenericName": "string",
    "Date": "date",
    "DateTime": "datetime",
    "URI": "uri",
    "UnitOfMeasure": "string",
    # GML geometry / temporal types – no direct LinkML equivalent, map to string
    "Length": "float",
    "Area": "float",
    "Volume": "float",
    "Measure": "float",
    "DirectPosition": "string",
    "GM_Object": "string",
    "TM_Position": "string",
    "TM_Duration": "string",
    "EngineeringCRS": "string",
    "MeasureOrNilReasonList": "string",
}

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class ElementInfo:
    xmi_id: str
    name: str
    element_type: str   # 'uml:Class', 'uml:DataType', 'uml:Enumeration', 'EAStub'
    is_abstract: bool = False
    package: str = ""


# Global warnings list, populated during conversion
warnings_log: list[str] = []


# ---------------------------------------------------------------------------
# Pass 1: Build ID registry
# ---------------------------------------------------------------------------

def collect_elements(
    element: ET.Element,
    registry: dict[str, ElementInfo],
    current_package: str = "",
) -> None:
    """Recursive DFS walk – collects all packagedElements into registry."""
    xmi_type = element.get(XMI_TYPE)
    xmi_id = element.get(XMI_ID)
    name = element.get("name")

    # Track the current package name as we descend
    if xmi_type == "uml:Package" and name:
        current_package = name

    if xmi_type in ("uml:Class", "uml:DataType", "uml:Enumeration") and xmi_id and name:
        registry[xmi_id] = ElementInfo(
            xmi_id=xmi_id,
            name=name,
            element_type=xmi_type,
            is_abstract=(element.get("isAbstract") == "true"),
            package=current_package,
        )

    for child in element:
        collect_elements(child, registry, current_package)


def collect_ea_stubs(root: ET.Element, registry: dict[str, ElementInfo]) -> None:
    """Collect EAStub primitive-type references from <xmi:Extension>."""
    for ext in root:
        if ext.tag == f"{{{XMI_NS}}}Extension":
            for stub in ext.iter("EAStub"):
                xmi_id = stub.get(XMI_ID)
                name = stub.get("name")
                if xmi_id and name and xmi_id not in registry:
                    registry[xmi_id] = ElementInfo(
                        xmi_id=xmi_id,
                        name=name,
                        element_type="EAStub",
                    )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_cardinality(attr_el: ET.Element) -> tuple[bool, bool]:
    """
    Return (required, multivalued) from lowerValue/upperValue child elements.

    EA encodes unlimited upper bound as value="-1" (uml:LiteralUnlimitedNatural).
    EA sometimes emits lowerValue value="-1" on association ends meaning
    "unspecified" – treat that as 0 (not required).
    """
    lower_el = attr_el.find("lowerValue")
    upper_el = attr_el.find("upperValue")

    lower_val = lower_el.get("value", "0") if lower_el is not None else "0"
    upper_val = upper_el.get("value", "1") if upper_el is not None else "1"

    required = lower_val == "1"
    multivalued = upper_val in ("-1", "*")

    return required, multivalued


def resolve_type(
    type_idref: str,
    registry: dict[str, ElementInfo],
) -> tuple[str, str]:
    """
    Return (linkml_range, category) where category is one of:
    'builtin', 'enum', 'class', 'unknown'.
    """
    info = registry.get(type_idref)
    if info is None:
        warnings_log.append(f"Unresolved type ID: {type_idref}")
        return "string", "unknown"

    if info.element_type == "EAStub":
        mapped = PRIMITIVE_TYPE_MAP.get(info.name)
        if mapped is None:
            warnings_log.append(
                f"Unknown EAStub type '{info.name}' (id={type_idref}), defaulting to string"
            )
            return "string", "unknown"
        return mapped, "builtin"

    if info.element_type == "uml:Enumeration":
        return info.name, "enum"

    # uml:Class or uml:DataType (complex) → LinkML class
    return info.name, "class"


def safe_name(name: str) -> str:
    """Ensure a name is a valid LinkML identifier (no spaces, etc.)."""
    return name.replace(" ", "_").replace("-", "_")


# ---------------------------------------------------------------------------
# XSD description loader
# ---------------------------------------------------------------------------

XSD_NS = "http://www.w3.org/2001/XMLSchema"


def load_xsd_descriptions(
    xsd_dir: str,
) -> tuple[dict[str, str], dict[tuple[str, str], str], dict[str, str]]:
    """
    Parse all XSD files under *xsd_dir* and extract documentation strings.

    Returns:
        class_docs  – {element_name: doc}  (top-level <element> annotations)
        attr_docs   – {(class_name, attr_name): doc}  (child <element> annotations
                      inside <complexType name="ClassNameType">)
        enum_docs   – {enum_base_name: doc}  (<simpleType> enumeration annotations,
                      with trailing "Type" stripped from the XSD name)
    """
    class_docs: dict[str, str] = {}
    attr_docs: dict[tuple[str, str], str] = {}
    enum_docs: dict[str, str] = {}

    xsd_files = glob.glob(os.path.join(xsd_dir, "**", "*.xsd"), recursive=True)
    for xsd_file in xsd_files:
        try:
            root = ET.parse(xsd_file).getroot()
        except ET.ParseError:
            continue

        # Top-level <element> → class description
        for el in root:
            if el.tag == f"{{{XSD_NS}}}element":
                name = el.get("name")
                ann = el.find(f"{{{XSD_NS}}}annotation/{{{XSD_NS}}}documentation")
                if name and ann is not None and ann.text:
                    class_docs[name] = ann.text.strip()

        # <complexType name="FooType"> children → attribute descriptions
        for ct in root.iter(f"{{{XSD_NS}}}complexType"):
            ct_name = ct.get("name", "")
            cls_name = ct_name[:-4] if ct_name.endswith("Type") else ct_name
            for seq in ct.iter(f"{{{XSD_NS}}}sequence"):
                for child_el in seq:
                    if child_el.tag == f"{{{XSD_NS}}}element":
                        attr_name = child_el.get("name")
                        ann = child_el.find(
                            f"{{{XSD_NS}}}annotation/{{{XSD_NS}}}documentation"
                        )
                        if attr_name and ann is not None and ann.text:
                            attr_docs[(cls_name, attr_name)] = ann.text.strip()

        # <simpleType> with enumeration restriction → enum description
        for st in root.iter(f"{{{XSD_NS}}}simpleType"):
            restr = st.find(f"{{{XSD_NS}}}restriction")
            if restr is None or restr.find(f"{{{XSD_NS}}}enumeration") is None:
                continue
            st_name = st.get("name", "")
            base_name = st_name[:-4] if st_name.endswith("Type") else st_name
            ann = st.find(f"{{{XSD_NS}}}annotation/{{{XSD_NS}}}documentation")
            if base_name and ann is not None and ann.text:
                enum_docs[base_name] = ann.text.strip()

    print(
        f"  XSD docs loaded: {len(class_docs)} class, "
        f"{len(attr_docs)} attribute, {len(enum_docs)} enum descriptions"
    )
    return class_docs, attr_docs, enum_docs


# ---------------------------------------------------------------------------
# Pass 2: Build schema
# ---------------------------------------------------------------------------

def build_enumerations(
    root: ET.Element,
    registry: dict[str, ElementInfo],
    sb: SchemaBuilder,
    xsd_docs: tuple[dict, dict, dict],
) -> None:
    """Extract all uml:Enumeration elements and add them as LinkML enums."""
    class_docs, _, enum_docs = xsd_docs
    count = 0
    for el in root.iter():
        if el.get(XMI_TYPE) != "uml:Enumeration":
            continue
        # Skip extension reference elements (they have xmi:idref, not xmi:id)
        if el.get(XMI_ID) is None:
            continue
        name = el.get("name")
        if not name:
            continue
        enum_def = EnumDefinition(name)

        # Prefer XSD descriptions; fall back to package note
        doc = enum_docs.get(name) or class_docs.get(name)
        if doc:
            enum_def.description = doc
        else:
            xmi_id = el.get(XMI_ID, "")
            pkg = registry.get(xmi_id, ElementInfo("", name, "uml:Enumeration")).package
            if pkg:
                enum_def.description = f"CityGML enumeration from package {pkg}"

        for literal in el:
            if literal.tag == "ownedLiteral":
                lit_name = literal.get("name")
                if lit_name:
                    enum_def.permissible_values[lit_name] = PermissibleValue(text=lit_name)

        sb.schema.enums[name] = enum_def
        count += 1

    print(f"  Added {count} enumerations")


def build_class_from_element(
    el: ET.Element,
    registry: dict[str, ElementInfo],
    sb: SchemaBuilder,
    xsd_docs: tuple[dict, dict, dict],
) -> None:
    """Build a single LinkML class from a uml:Class or uml:DataType element."""
    class_docs, attr_docs, _ = xsd_docs
    xmi_id = el.get(XMI_ID)
    # Skip extension reference elements (they have xmi:idref, not xmi:id)
    if xmi_id is None:
        return
    name = el.get("name")
    if not name:
        return

    cls = ClassDefinition(name)
    cls.abstract = el.get("isAbstract") == "true"

    # Prefer XSD description; fall back to package note
    doc = class_docs.get(name)
    if doc:
        cls.description = doc
    else:
        info = registry.get(xmi_id)
        if info and info.package:
            cls.description = f"CityGML class from package {info.package}"

    # Inheritance: first <generalization> element
    gen_el = el.find("generalization")
    if gen_el is not None:
        parent_id = gen_el.get("general")
        if parent_id:
            parent_info = registry.get(parent_id)
            if parent_info:
                cls.is_a = parent_info.name
            else:
                warnings_log.append(f"Class {name}: unknown parent ID {parent_id}")

    # Attributes (both plain and association-linked ownedAttribute elements)
    seen_attrs: set[str] = set()
    for attr in el:
        if attr.tag != "ownedAttribute":
            continue
        attr_name = attr.get("name")
        if not attr_name:
            continue

        if attr_name in seen_attrs:
            warnings_log.append(
                f"Duplicate attribute '{attr_name}' on class {name}, skipping"
            )
            continue
        seen_attrs.add(attr_name)

        type_el = attr.find("type")
        type_idref = type_el.get(XMI_IDREF) if type_el is not None else None

        required, multivalued = parse_cardinality(attr)

        if type_idref:
            range_name, _ = resolve_type(type_idref, registry)
        else:
            range_name = "string"
            warnings_log.append(f"{name}.{attr_name}: no type reference, defaulting to string")

        slot = SlotDefinition(attr_name)
        slot.range = range_name
        slot.required = required
        slot.multivalued = multivalued
        slot.description = attr_docs.get((name, attr_name))

        cls.attributes[attr_name] = slot

    sb.schema.classes[name] = cls


def build_datatype_classes(
    root: ET.Element,
    registry: dict[str, ElementInfo],
    sb: SchemaBuilder,
    xsd_docs: tuple[dict, dict, dict],
) -> None:
    """Add all uml:DataType elements as LinkML classes."""
    count = 0
    for el in root.iter():
        if el.get(XMI_TYPE) != "uml:DataType":
            continue
        build_class_from_element(el, registry, sb, xsd_docs)
        count += 1
    print(f"  Added {count} DataType classes")


def build_uml_classes(
    root: ET.Element,
    registry: dict[str, ElementInfo],
    sb: SchemaBuilder,
    xsd_docs: tuple[dict, dict, dict],
) -> None:
    """Add all uml:Class elements as LinkML classes."""
    count = 0
    for el in root.iter():
        if el.get(XMI_TYPE) != "uml:Class":
            continue
        build_class_from_element(el, registry, sb, xsd_docs)
        count += 1
    print(f"  Added {count} UML classes")


# ---------------------------------------------------------------------------
# Lint checkpoint
# ---------------------------------------------------------------------------

def lint_checkpoint(
    schema,
    checkpoint_name: str,
    output_file: str | None = None,
) -> None:
    """Write schema to a file and run linkml-lint, printing results."""
    yaml_content = yaml_dumper.dumps(schema)

    if output_file is not None:
        path = output_file
        with open(path, "w", encoding="utf-8") as f:
            f.write(yaml_content)
        delete_after = False
    else:
        fd, path = tempfile.mkstemp(suffix=".yaml", prefix="citygml_check_")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(yaml_content)
        delete_after = True

    # Try 'linkml-lint' then fall back to the .venv path
    for cmd in [".venv/bin/linkml-lint", "linkml-lint"]:
        result = subprocess.run(
            [cmd, "--validate", path],
            capture_output=True,
            text=True,
        )
        if result.returncode != 127:  # 127 = command not found
            break

    print(f"\n=== Lint checkpoint: {checkpoint_name} ===")
    combined = (result.stdout + result.stderr).strip()
    if not combined or result.returncode == 0:
        print("  PASS – no issues")
    else:
        print("  Issues found (first 3000 chars):")
        print(combined[:3000])

    if delete_after:
        os.unlink(path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"Parsing {XMI_FILE} ...")
    tree = ET.parse(XMI_FILE)
    root = tree.getroot()

    # ------------------------------------------------------------------
    # Pass 1: Build ID registry
    # ------------------------------------------------------------------
    print("\nPass 1: Building ID registry ...")
    registry: dict[str, ElementInfo] = {}
    collect_elements(root, registry)
    collect_ea_stubs(root, registry)

    counts = {"uml:Class": 0, "uml:DataType": 0, "uml:Enumeration": 0, "EAStub": 0}
    for info in registry.values():
        if info.element_type in counts:
            counts[info.element_type] += 1
    print(
        f"  Registry: {counts['uml:Class']} classes, "
        f"{counts['uml:DataType']} datatypes, "
        f"{counts['uml:Enumeration']} enumerations, "
        f"{counts['EAStub']} EAStubs"
    )

    # ------------------------------------------------------------------
    # Load XSD descriptions
    # ------------------------------------------------------------------
    print("\nLoading XSD descriptions ...")
    xsd_docs = load_xsd_descriptions(XSD_DIR)

    # ------------------------------------------------------------------
    # Pass 2: Build schema
    # ------------------------------------------------------------------
    print("\nPass 2: Building schema ...")

    sb = SchemaBuilder(SCHEMA_NAME)
    sb.schema.id = SCHEMA_ID
    sb.schema.title = "OGC CityGML 3.0"
    sb.schema.description = (
        "LinkML schema generated from OGC CityGML 3.0 UML/XMI model "
        "(Enterprise Architect export)"
    )
    sb.schema.version = "3.0"
    sb.add_defaults()

    # Step 1 – Enumerations (no dependencies)
    print("\nStep 1: Enumerations ...")
    build_enumerations(root, registry, sb, xsd_docs)
    lint_checkpoint(sb.schema, "after enumerations")

    # Step 2 – DataType classes (may reference enumerations and primitives)
    print("\nStep 2: DataType classes ...")
    build_datatype_classes(root, registry, sb, xsd_docs)
    lint_checkpoint(sb.schema, "after DataType classes")

    # Step 3 – UML classes (may reference everything above)
    print("\nStep 3: UML classes ...")
    build_uml_classes(root, registry, sb, xsd_docs)
    lint_checkpoint(sb.schema, "after UML classes")

    # ------------------------------------------------------------------
    # Write output and final lint
    # ------------------------------------------------------------------
    print(f"\nWriting {OUTPUT_FILE} ...")
    lint_checkpoint(sb.schema, "final (written to disk)", output_file=OUTPUT_FILE)

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    n_classes = len(sb.schema.classes)
    n_enums = len(sb.schema.enums)
    print(f"\nSchema summary: {n_classes} classes, {n_enums} enums")

    if warnings_log:
        print(f"\nWarnings ({len(warnings_log)} total, showing first 50):")
        for w in warnings_log[:50]:
            print(f"  {w}")
        if len(warnings_log) > 50:
            print(f"  ... and {len(warnings_log) - 50} more")
    else:
        print("\nNo warnings.")

    print("\nDone.")


if __name__ == "__main__":
    main()
