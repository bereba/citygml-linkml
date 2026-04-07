

# Slot: worldToTexture 


_Specifies the 3x4 transformation matrix that defines the transformation between world coordinates and texture coordinates._





URI: [citygml:worldToTexture](https://www.ogc.org/standards/citygml/worldToTexture)
Alias: worldToTexture

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TexCoordGen](TexCoordGen.md) | TexCoordGen defines texture parameterization using a transformation matrix |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TransformationMatrix3x4](TransformationMatrix3x4.md) |
| Domain Of | [TexCoordGen](TexCoordGen.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TexCoordGen](TexCoordGen.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:worldToTexture |
| native | citygml:worldToTexture |




## LinkML Source

<details>
```yaml
name: worldToTexture
description: Specifies the 3x4 transformation matrix that defines the transformation
  between world coordinates and texture coordinates.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: worldToTexture
owner: TexCoordGen
domain_of:
- TexCoordGen
range: TransformationMatrix3x4
required: true
multivalued: false

```
</details>