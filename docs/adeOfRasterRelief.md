

# Slot: adeOfRasterRelief 


_Augments the RasterRelief with properties defined in an ADE._





URI: [citygml:adeOfRasterRelief](https://www.ogc.org/standards/citygml/adeOfRasterRelief)
Alias: adeOfRasterRelief

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RasterRelief](RasterRelief.md) | A RasterRelief represents a terrain component as a regular raster or grid |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfRasterRelief](ADEOfRasterRelief.md) |
| Domain Of | [RasterRelief](RasterRelief.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | citygml:adeOfRasterRelief |
| native | citygml:adeOfRasterRelief |




## LinkML Source

<details>
```yaml
name: adeOfRasterRelief
description: Augments the RasterRelief with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfRasterRelief
owner: RasterRelief
domain_of:
- RasterRelief
range: ADEOfRasterRelief
required: false
multivalued: true

```
</details>