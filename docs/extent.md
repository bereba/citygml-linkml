

# Slot: extent 


_Indicates the geometrical extent of the terrain component. The geometrical extent is provided as a 2D Surface geometry._





URI: [citygml:extent](https://www.ogc.org/standards/citygml/extent)
Alias: extent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TINRelief](TINRelief.md) | A TINRelief represents a terrain component as a triangulated irregular networ... |  no  |
| [BreaklineRelief](BreaklineRelief.md) | A BreaklineRelief represents a terrain component with 3D lines |  no  |
| [RasterRelief](RasterRelief.md) | A RasterRelief represents a terrain component as a regular raster or grid |  no  |
| [MassPointRelief](MassPointRelief.md) | A MassPointRelief represents a terrain component as a collection of 3D points |  no  |
| [AbstractReliefComponent](AbstractReliefComponent.md) | An AbstractReliefComponent represents an element of the terrain surface - eit... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AbstractReliefComponent](AbstractReliefComponent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractReliefComponent](AbstractReliefComponent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:extent |
| native | citygml:extent |




## LinkML Source

<details>
```yaml
name: extent
description: Indicates the geometrical extent of the terrain component. The geometrical
  extent is provided as a 2D Surface geometry.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: extent
owner: AbstractReliefComponent
domain_of:
- AbstractReliefComponent
range: string
required: false
multivalued: false

```
</details>