

# Slot: lod 



URI: [citygml:lod](https://www.ogc.org/standards/citygml/lod)
Alias: lod

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TINRelief](TINRelief.md) | A TINRelief represents a terrain component as a triangulated irregular networ... |  no  |
| [BreaklineRelief](BreaklineRelief.md) | A BreaklineRelief represents a terrain component with 3D lines |  no  |
| [RasterRelief](RasterRelief.md) | A RasterRelief represents a terrain component as a regular raster or grid |  no  |
| [MassPointRelief](MassPointRelief.md) | A MassPointRelief represents a terrain component as a collection of 3D points |  no  |
| [ReliefFeature](ReliefFeature.md) | A ReliefFeature is a collection of terrain components representing the Earth'... |  no  |
| [AbstractReliefComponent](AbstractReliefComponent.md) | An AbstractReliefComponent represents an element of the terrain surface - eit... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AbstractReliefComponent](AbstractReliefComponent.md), [ReliefFeature](ReliefFeature.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:lod |
| native | citygml:lod |




## LinkML Source

<details>
```yaml
name: lod
alias: lod
domain_of:
- AbstractReliefComponent
- ReliefFeature
range: string

```
</details>