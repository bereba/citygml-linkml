

# Slot: adeOfWaterBody 


_Augments the WaterBody with properties defined in an ADE._





URI: [citygml:adeOfWaterBody](https://www.ogc.org/standards/citygml/adeOfWaterBody)
Alias: adeOfWaterBody

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterBody](WaterBody.md) | A WaterBody represents significant and permanent or semi-permanent accumulati... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfWaterBody](ADEOfWaterBody.md) |
| Domain Of | [WaterBody](WaterBody.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [WaterBody](WaterBody.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfWaterBody |
| native | citygml:adeOfWaterBody |




## LinkML Source

<details>
```yaml
name: adeOfWaterBody
description: Augments the WaterBody with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfWaterBody
owner: WaterBody
domain_of:
- WaterBody
range: ADEOfWaterBody
required: false
multivalued: true

```
</details>