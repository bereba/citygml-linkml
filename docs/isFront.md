

# Slot: isFront 


_Indicates whether the texture or material is assigned to the front side or the back side of the surface geometry object._





URI: [citygml:isFront](https://www.ogc.org/standards/citygml/isFront)
Alias: isFront

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [X3DMaterial](X3DMaterial.md) | X3DMaterial defines properties for surface geometry objects based on the mate... |  no  |
| [AbstractTexture](AbstractTexture.md) | AbstractTexture is the abstract superclass to represent the common attributes... |  no  |
| [AbstractSurfaceData](AbstractSurfaceData.md) | AbstractSurfaceData is the abstract superclass for different kinds of texture... |  no  |
| [ParameterizedTexture](ParameterizedTexture.md) | A ParameterizedTexture is a texture that uses texture coordinates or a transf... |  no  |
| [GeoreferencedTexture](GeoreferencedTexture.md) | A GeoreferencedTexture is a texture that uses a planimetric projection |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [AbstractSurfaceData](AbstractSurfaceData.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractSurfaceData](AbstractSurfaceData.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:isFront |
| native | citygml:isFront |




## LinkML Source

<details>
```yaml
name: isFront
description: Indicates whether the texture or material is assigned to the front side
  or the back side of the surface geometry object.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: isFront
owner: AbstractSurfaceData
domain_of:
- AbstractSurfaceData
range: boolean
required: false
multivalued: false

```
</details>