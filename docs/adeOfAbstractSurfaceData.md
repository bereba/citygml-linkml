

# Slot: adeOfAbstractSurfaceData 


_Augments AbstractSurfaceData with properties defined in an ADE._





URI: [citygml:adeOfAbstractSurfaceData](https://www.ogc.org/standards/citygml/adeOfAbstractSurfaceData)
Alias: adeOfAbstractSurfaceData

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
| Range | [ADEOfAbstractSurfaceData](ADEOfAbstractSurfaceData.md) |
| Domain Of | [AbstractSurfaceData](AbstractSurfaceData.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | citygml:adeOfAbstractSurfaceData |
| native | citygml:adeOfAbstractSurfaceData |




## LinkML Source

<details>
```yaml
name: adeOfAbstractSurfaceData
description: Augments AbstractSurfaceData with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractSurfaceData
owner: AbstractSurfaceData
domain_of:
- AbstractSurfaceData
range: ADEOfAbstractSurfaceData
required: false
multivalued: true

```
</details>