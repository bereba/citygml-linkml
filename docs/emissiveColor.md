

# Slot: emissiveColor 


_Specifies the color of the light emitted by the surface geometry object._





URI: [citygml:emissiveColor](https://www.ogc.org/standards/citygml/emissiveColor)
Alias: emissiveColor

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
| self | citygml:emissiveColor |
| native | citygml:emissiveColor |




## LinkML Source

<details>
```yaml
name: emissiveColor
description: Specifies the color of the light emitted by the surface geometry object.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: emissiveColor
owner: X3DMaterial
domain_of:
- X3DMaterial
range: Color
required: false
multivalued: false

```
</details>