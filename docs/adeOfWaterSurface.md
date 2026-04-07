

# Slot: adeOfWaterSurface 


_Augments the WaterSurface with properties defined in an ADE._





URI: [citygml:adeOfWaterSurface](https://www.ogc.org/standards/citygml/adeOfWaterSurface)
Alias: adeOfWaterSurface

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSurface](WaterSurface.md) | A WaterSurface represents the upper exterior interface between a water body a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfWaterSurface](ADEOfWaterSurface.md) |
| Domain Of | [WaterSurface](WaterSurface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [WaterSurface](WaterSurface.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfWaterSurface |
| native | citygml:adeOfWaterSurface |




## LinkML Source

<details>
```yaml
name: adeOfWaterSurface
description: Augments the WaterSurface with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfWaterSurface
owner: WaterSurface
domain_of:
- WaterSurface
range: ADEOfWaterSurface
required: false
multivalued: true

```
</details>