# LinkML Schema for the CityGML Standard

In this repo we build a linkml schema based on the OGC CityGML standard: https://www.ogc.org/standards/citygml/

## Steps

We have:

- xml files defining the citygml standard in OGC CityGML 3.0/Integrated/CityGML_3.0.xml and in citygml-3_0_0_xsd, both taken from https://www.ogc.org/standards/citygml/
- linkml model standard:
  - https://linkml.io/linkml/schemas/index.html
  - https://github.com/linkml/linkml/blob/main/examples/PersonSchema

The script `convert_xmi_to_linkml.py` mainly uses the xmi files from the folder `OGC CityGML 3.0` to create the linkml schema in `citygml_schema.yml`. Since the xmi files do not have a description for classes and attributes, the `xsd` files are then used to get descriptions. This is a prototype. In the end it might be better to only use the xsd files for schema generation and delete the XMI files from this repo.

## AI Usage

This prototypical implementation was done with the help of AI tools.
