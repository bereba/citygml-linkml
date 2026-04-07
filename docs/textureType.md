

# Slot: textureType 


_Indicates the specific type of the texture._





URI: [citygml:textureType](https://www.ogc.org/standards/citygml/textureType)
Alias: textureType

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
| Range | [TextureType](TextureType.md) |
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
| self | citygml:textureType |
| native | citygml:textureType |




## LinkML Source

<details>
```yaml
name: textureType
description: Indicates the specific type of the texture.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: textureType
owner: AbstractTexture
domain_of:
- AbstractTexture
range: TextureType
required: false
multivalued: false

```
</details>