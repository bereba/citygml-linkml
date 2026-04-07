

# Slot: waterLevel 


_Specifies the level of the WaterSurface._





URI: [citygml:waterLevel](https://www.ogc.org/standards/citygml/waterLevel)
Alias: waterLevel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSurface](WaterSurface.md) | A WaterSurface represents the upper exterior interface between a water body a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [WaterLevelValue](WaterLevelValue.md) |
| Domain Of | [WaterSurface](WaterSurface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | citygml:waterLevel |
| native | citygml:waterLevel |




## LinkML Source

<details>
```yaml
name: waterLevel
description: Specifies the level of the WaterSurface.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: waterLevel
owner: WaterSurface
domain_of:
- WaterSurface
range: WaterLevelValue
required: false
multivalued: false

```
</details>