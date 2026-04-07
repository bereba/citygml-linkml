

# Slot: dynamicData 


_Relates to the timeseries data that is given either inline within a CityGML dataset or by a link to an external file containing timeseries data._





URI: [citygml:dynamicData](https://www.ogc.org/standards/citygml/dynamicData)
Alias: dynamicData

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dynamizer](Dynamizer.md) | A Dynamizer is an object that injects timeseries data for an individual attri... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AbstractTimeseries](AbstractTimeseries.md) |
| Domain Of | [Dynamizer](Dynamizer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dynamizer](Dynamizer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:dynamicData |
| native | citygml:dynamicData |




## LinkML Source

<details>
```yaml
name: dynamicData
description: Relates to the timeseries data that is given either inline within a CityGML
  dataset or by a link to an external file containing timeseries data.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: dynamicData
owner: Dynamizer
domain_of:
- Dynamizer
range: AbstractTimeseries
required: false
multivalued: false

```
</details>