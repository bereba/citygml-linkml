

# Slot: adeOfStandardFileTimeseries 


_Augments the StandardFileTimeseries with properties defined in an ADE._





URI: [citygml:adeOfStandardFileTimeseries](https://www.ogc.org/standards/citygml/adeOfStandardFileTimeseries)
Alias: adeOfStandardFileTimeseries

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StandardFileTimeseries](StandardFileTimeseries.md) | A StandardFileTimeseries represents time-varying data for a single contiguous... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfStandardFileTimeseries](ADEOfStandardFileTimeseries.md) |
| Domain Of | [StandardFileTimeseries](StandardFileTimeseries.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StandardFileTimeseries](StandardFileTimeseries.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfStandardFileTimeseries |
| native | citygml:adeOfStandardFileTimeseries |




## LinkML Source

<details>
```yaml
name: adeOfStandardFileTimeseries
description: Augments the StandardFileTimeseries with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfStandardFileTimeseries
owner: StandardFileTimeseries
domain_of:
- StandardFileTimeseries
range: ADEOfStandardFileTimeseries
required: false
multivalued: true

```
</details>