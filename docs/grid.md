

# Slot: grid 


_Relates to the DiscreteGridPointCoverage of the RasterRelief._





URI: [citygml:grid](https://www.ogc.org/standards/citygml/grid)
Alias: grid

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RasterRelief](RasterRelief.md) | A RasterRelief represents a terrain component as a regular raster or grid |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [RasterRelief](RasterRelief.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [RasterRelief](RasterRelief.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:grid |
| native | citygml:grid |




## LinkML Source

<details>
```yaml
name: grid
description: Relates to the DiscreteGridPointCoverage of the RasterRelief.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: grid
owner: RasterRelief
domain_of:
- RasterRelief
range: string
required: true
multivalued: false

```
</details>