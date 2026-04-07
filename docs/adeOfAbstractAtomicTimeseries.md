

# Slot: adeOfAbstractAtomicTimeseries 


_Augments AbstractAtomicTimeseries with properties defined in an ADE._





URI: [citygml:adeOfAbstractAtomicTimeseries](https://www.ogc.org/standards/citygml/adeOfAbstractAtomicTimeseries)
Alias: adeOfAbstractAtomicTimeseries

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTimeseries](GenericTimeseries.md) | A GenericTimeseries represents time-varying data in the form of embedded time... |  no  |
| [StandardFileTimeseries](StandardFileTimeseries.md) | A StandardFileTimeseries represents time-varying data for a single contiguous... |  no  |
| [TabulatedFileTimeseries](TabulatedFileTimeseries.md) | A TabulatedFileTimeseries represents time-varying data of a specific data typ... |  no  |
| [AbstractAtomicTimeseries](AbstractAtomicTimeseries.md) | AbstractAtomicTimeseries represents the attributes and relationships that are... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractAtomicTimeseries](ADEOfAbstractAtomicTimeseries.md) |
| Domain Of | [AbstractAtomicTimeseries](AbstractAtomicTimeseries.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractAtomicTimeseries](AbstractAtomicTimeseries.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractAtomicTimeseries |
| native | citygml:adeOfAbstractAtomicTimeseries |




## LinkML Source

<details>
```yaml
name: adeOfAbstractAtomicTimeseries
description: Augments AbstractAtomicTimeseries with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractAtomicTimeseries
owner: AbstractAtomicTimeseries
domain_of:
- AbstractAtomicTimeseries
range: ADEOfAbstractAtomicTimeseries
required: false
multivalued: true

```
</details>