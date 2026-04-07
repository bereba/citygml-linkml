

# Slot: wrapMode 


_Specifies the behaviour of the texture when the texture is smaller than the surface to which it is applied._





URI: [citygml:wrapMode](https://www.ogc.org/standards/citygml/wrapMode)
Alias: wrapMode

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
| Range | [WrapMode](WrapMode.md) |
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
| self | citygml:wrapMode |
| native | citygml:wrapMode |




## LinkML Source

<details>
```yaml
name: wrapMode
description: Specifies the behaviour of the texture when the texture is smaller than
  the surface to which it is applied.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: wrapMode
owner: AbstractTexture
domain_of:
- AbstractTexture
range: WrapMode
required: false
multivalued: false

```
</details>