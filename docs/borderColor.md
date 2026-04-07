

# Slot: borderColor 


_Specifies the color of that part of the surface that is not covered by the texture._





URI: [citygml:borderColor](https://www.ogc.org/standards/citygml/borderColor)
Alias: borderColor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AbstractTexture](AbstractTexture.md) | AbstractTexture is the abstract superclass to represent the common attributes... |  no  |
| [GeoreferencedTexture](GeoreferencedTexture.md) | A GeoreferencedTexture is a texture that uses a planimetric projection |  no  |
| [ParameterizedTexture](ParameterizedTexture.md) | A ParameterizedTexture is a texture that uses texture coordinates or a transf... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ColorPlusOpacity](ColorPlusOpacity.md) |
| Domain Of | [AbstractTexture](AbstractTexture.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractTexture](AbstractTexture.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:borderColor |
| native | citygml:borderColor |




## LinkML Source

<details>
```yaml
name: borderColor
description: Specifies the color of that part of the surface that is not covered by
  the texture.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: borderColor
owner: AbstractTexture
domain_of:
- AbstractTexture
range: ColorPlusOpacity
required: false
multivalued: false

```
</details>