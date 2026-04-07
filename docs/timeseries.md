

# Slot: timeseries 


_Relates a timeseries to the TimeseriesComponent._





URI: [citygml:timeseries](https://www.ogc.org/standards/citygml/timeseries)
Alias: timeseries

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeseriesComponent](TimeseriesComponent.md) | TimeseriesComponent represents an element of a CompositeTimeseries |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AbstractTimeseries](AbstractTimeseries.md) |
| Domain Of | [TimeseriesComponent](TimeseriesComponent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TimeseriesComponent](TimeseriesComponent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:timeseries |
| native | citygml:timeseries |




## LinkML Source

<details>
```yaml
name: timeseries
description: Relates a timeseries to the TimeseriesComponent.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: timeseries
owner: TimeseriesComponent
domain_of:
- TimeseriesComponent
range: AbstractTimeseries
required: true
multivalued: false

```
</details>