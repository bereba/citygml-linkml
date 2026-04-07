

# Slot: textureParameterization 


_Relates to the texture coordinates or transformation matrices used for parameterization._





URI: [citygml:textureParameterization](https://www.ogc.org/standards/citygml/textureParameterization)
Alias: textureParameterization

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ParameterizedTexture](ParameterizedTexture.md) | A ParameterizedTexture is a texture that uses texture coordinates or a transf... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AbstractTextureParameterization](AbstractTextureParameterization.md) |
| Domain Of | [ParameterizedTexture](ParameterizedTexture.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ParameterizedTexture](ParameterizedTexture.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:textureParameterization |
| native | citygml:textureParameterization |




## LinkML Source

<details>
```yaml
name: textureParameterization
description: Relates to the texture coordinates or transformation matrices used for
  parameterization.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: textureParameterization
owner: ParameterizedTexture
domain_of:
- ParameterizedTexture
range: AbstractTextureParameterization
required: false
multivalued: true

```
</details>