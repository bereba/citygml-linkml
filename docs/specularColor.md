

# Slot: specularColor 


_Specifies the color of the light directly reflected by the surface geometry object._





URI: [citygml:specularColor](https://www.ogc.org/standards/citygml/specularColor)
Alias: specularColor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [X3DMaterial](X3DMaterial.md) | X3DMaterial defines properties for surface geometry objects based on the mate... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Color](Color.md) |
| Domain Of | [X3DMaterial](X3DMaterial.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [X3DMaterial](X3DMaterial.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:specularColor |
| native | citygml:specularColor |




## LinkML Source

<details>
```yaml
name: specularColor
description: Specifies the color of the light directly reflected by the surface geometry
  object.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: specularColor
owner: X3DMaterial
domain_of:
- X3DMaterial
range: Color
required: false
multivalued: false

```
</details>