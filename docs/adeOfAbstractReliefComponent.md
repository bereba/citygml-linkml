

# Slot: adeOfAbstractReliefComponent 


_Augments AbstractReliefComponent with properties defined in an ADE._





URI: [citygml:adeOfAbstractReliefComponent](https://www.ogc.org/standards/citygml/adeOfAbstractReliefComponent)
Alias: adeOfAbstractReliefComponent

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
| Range | [ADEOfAbstractReliefComponent](ADEOfAbstractReliefComponent.md) |
| Domain Of | [AbstractReliefComponent](AbstractReliefComponent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | citygml:adeOfAbstractReliefComponent |
| native | citygml:adeOfAbstractReliefComponent |




## LinkML Source

<details>
```yaml
name: adeOfAbstractReliefComponent
description: Augments AbstractReliefComponent with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractReliefComponent
owner: AbstractReliefComponent
domain_of:
- AbstractReliefComponent
range: ADEOfAbstractReliefComponent
required: false
multivalued: true

```
</details>