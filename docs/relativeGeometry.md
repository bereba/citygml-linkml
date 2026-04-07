

# Slot: relativeGeometry 


_Relates to a prototypical geometry in a local coordinate system stored inline with the city model._





URI: [citygml:relativeGeometry](https://www.ogc.org/standards/citygml/relativeGeometry)
Alias: relativeGeometry

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImplicitGeometry](ImplicitGeometry.md) | ImplicitGeometry is a geometry representation where the shape is stored only ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImplicitGeometry](ImplicitGeometry.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImplicitGeometry](ImplicitGeometry.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:relativeGeometry |
| native | citygml:relativeGeometry |




## LinkML Source

<details>
```yaml
name: relativeGeometry
description: Relates to a prototypical geometry in a local coordinate system stored
  inline with the city model.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: relativeGeometry
owner: ImplicitGeometry
domain_of:
- ImplicitGeometry
range: string
required: false
multivalued: false

```
</details>