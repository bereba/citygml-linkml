

# Slot: orientation 


_Specifies the rotation and scaling of the image in form of a 2x2 matrix._





URI: [citygml:orientation](https://www.ogc.org/standards/citygml/orientation)
Alias: orientation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeoreferencedTexture](GeoreferencedTexture.md) | A GeoreferencedTexture is a texture that uses a planimetric projection |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TransformationMatrix2x2](TransformationMatrix2x2.md) |
| Domain Of | [GeoreferencedTexture](GeoreferencedTexture.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [GeoreferencedTexture](GeoreferencedTexture.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:orientation |
| native | citygml:orientation |




## LinkML Source

<details>
```yaml
name: orientation
description: Specifies the rotation and scaling of the image in form of a 2x2 matrix.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: orientation
owner: GeoreferencedTexture
domain_of:
- GeoreferencedTexture
range: TransformationMatrix2x2
required: false
multivalued: false

```
</details>