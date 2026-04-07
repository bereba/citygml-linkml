

# Slot: timeValuePair 


_Relates to the time-value-pairs that are part of the GenericTimeseries._





URI: [citygml:timeValuePair](https://www.ogc.org/standards/citygml/timeValuePair)
Alias: timeValuePair

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTimeseries](GenericTimeseries.md) | A GenericTimeseries represents time-varying data in the form of embedded time... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimeValuePair](TimeValuePair.md) |
| Domain Of | [GenericTimeseries](GenericTimeseries.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [GenericTimeseries](GenericTimeseries.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:timeValuePair |
| native | citygml:timeValuePair |




## LinkML Source

<details>
```yaml
name: timeValuePair
description: Relates to the time-value-pairs that are part of the GenericTimeseries.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: timeValuePair
owner: GenericTimeseries
domain_of:
- GenericTimeseries
range: TimeValuePair
required: true
multivalued: true

```
</details>