

# Slot: numberOfHeaderLines 


_Indicates the number of lines at the beginning of the tabulated file that represent headers._





URI: [citygml:numberOfHeaderLines](https://www.ogc.org/standards/citygml/numberOfHeaderLines)
Alias: numberOfHeaderLines

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
| self | citygml:numberOfHeaderLines |
| native | citygml:numberOfHeaderLines |




## LinkML Source

<details>
```yaml
name: numberOfHeaderLines
description: Indicates the number of lines at the beginning of the tabulated file
  that represent headers.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: numberOfHeaderLines
owner: TabulatedFileTimeseries
domain_of:
- TabulatedFileTimeseries
range: integer
required: false
multivalued: false

```
</details>