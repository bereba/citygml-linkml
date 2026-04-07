

# Slot: fieldSeparator 


_Indicates which symbol is used to separate the individual values in the tabulated file._





URI: [citygml:fieldSeparator](https://www.ogc.org/standards/citygml/fieldSeparator)
Alias: fieldSeparator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TabulatedFileTimeseries](TabulatedFileTimeseries.md) | A TabulatedFileTimeseries represents time-varying data of a specific data typ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [TabulatedFileTimeseries](TabulatedFileTimeseries.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | citygml:fieldSeparator |
| native | citygml:fieldSeparator |




## LinkML Source

<details>
```yaml
name: fieldSeparator
description: Indicates which symbol is used to separate the individual values in the
  tabulated file.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: fieldSeparator
owner: TabulatedFileTimeseries
domain_of:
- TabulatedFileTimeseries
range: string
required: true
multivalued: false

```
</details>