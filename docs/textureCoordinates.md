

# Slot: textureCoordinates 


_Specifies the coordinates of texture used for parameterization. The texture coordinates are provided separately for each LinearRing of the surface geometry object._





URI: [citygml:textureCoordinates](https://www.ogc.org/standards/citygml/textureCoordinates)
Alias: textureCoordinates

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TexCoordList](TexCoordList.md) | TexCoordList defines texture parameterization using texture coordinates |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DoubleList](DoubleList.md) |
| Domain Of | [TexCoordList](TexCoordList.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TexCoordList](TexCoordList.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:textureCoordinates |
| native | citygml:textureCoordinates |




## LinkML Source

<details>
```yaml
name: textureCoordinates
description: Specifies the coordinates of texture used for parameterization. The texture
  coordinates are provided separately for each LinearRing of the surface geometry
  object.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: textureCoordinates
owner: TexCoordList
domain_of:
- TexCoordList
range: DoubleList
required: true
multivalued: true

```
</details>