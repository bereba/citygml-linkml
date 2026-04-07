

# Slot: timeColumnNo 


_Specifies the number of the column that stores the timestamp of the time-value-pair._





URI: [citygml:timeColumnNo](https://www.ogc.org/standards/citygml/timeColumnNo)
Alias: timeColumnNo

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TabulatedFileTimeseries](TabulatedFileTimeseries.md) | A TabulatedFileTimeseries represents time-varying data of a specific data typ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [TabulatedFileTimeseries](TabulatedFileTimeseries.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TabulatedFileTimeseries](TabulatedFileTimeseries.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:timeColumnNo |
| native | citygml:timeColumnNo |




## LinkML Source

<details>
```yaml
name: timeColumnNo
description: Specifies the number of the column that stores the timestamp of the time-value-pair.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: timeColumnNo
owner: TabulatedFileTimeseries
domain_of:
- TabulatedFileTimeseries
range: integer
required: false
multivalued: false

```
</details>