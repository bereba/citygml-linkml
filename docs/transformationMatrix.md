

# Slot: transformationMatrix 


_Specifies the mathematical transformation (translation, rotation, and scaling) between the prototypical geometry and the actual spatial position of the object._





URI: [citygml:transformationMatrix](https://www.ogc.org/standards/citygml/transformationMatrix)
Alias: transformationMatrix

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImplicitGeometry](ImplicitGeometry.md) | ImplicitGeometry is a geometry representation where the shape is stored only ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TransformationMatrix4x4](TransformationMatrix4x4.md) |
| Domain Of | [ImplicitGeometry](ImplicitGeometry.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | citygml:transformationMatrix |
| native | citygml:transformationMatrix |




## LinkML Source

<details>
```yaml
name: transformationMatrix
description: Specifies the mathematical transformation (translation, rotation, and
  scaling) between the prototypical geometry and the actual spatial position of the
  object.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: transformationMatrix
owner: ImplicitGeometry
domain_of:
- ImplicitGeometry
range: TransformationMatrix4x4
required: true
multivalued: false

```
</details>