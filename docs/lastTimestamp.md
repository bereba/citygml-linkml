

# Slot: lastTimestamp 


_Specifies the end of the timeseries._





URI: [citygml:lastTimestamp](https://www.ogc.org/standards/citygml/lastTimestamp)
Alias: lastTimestamp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AbstractTimeseries](AbstractTimeseries.md) | AbstractTimeseries is the abstract superclass representing any type of timese... |  no  |
| [CompositeTimeseries](CompositeTimeseries.md) | A CompositeTimeseries is a (possibly recursive) aggregation of atomic and com... |  no  |
| [StandardFileTimeseries](StandardFileTimeseries.md) | A StandardFileTimeseries represents time-varying data for a single contiguous... |  no  |
| [TabulatedFileTimeseries](TabulatedFileTimeseries.md) | A TabulatedFileTimeseries represents time-varying data of a specific data typ... |  no  |
| [AbstractAtomicTimeseries](AbstractAtomicTimeseries.md) | AbstractAtomicTimeseries represents the attributes and relationships that are... |  no  |
| [GenericTimeseries](GenericTimeseries.md) | A GenericTimeseries represents time-varying data in the form of embedded time... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AbstractTimeseries](AbstractTimeseries.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractTimeseries](AbstractTimeseries.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:lastTimestamp |
| native | citygml:lastTimestamp |




## LinkML Source

<details>
```yaml
name: lastTimestamp
description: Specifies the end of the timeseries.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: lastTimestamp
owner: AbstractTimeseries
domain_of:
- AbstractTimeseries
range: string
required: false
multivalued: false

```
</details>