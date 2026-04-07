

# Slot: decimalSymbol 


_Indicates which symbol is used to separate the integer part from the fractional part of a decimal number._





URI: [citygml:decimalSymbol](https://www.ogc.org/standards/citygml/decimalSymbol)
Alias: decimalSymbol

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
| self | citygml:decimalSymbol |
| native | citygml:decimalSymbol |




## LinkML Source

<details>
```yaml
name: decimalSymbol
description: Indicates which symbol is used to separate the integer part from the
  fractional part of a decimal number.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: decimalSymbol
owner: TabulatedFileTimeseries
domain_of:
- TabulatedFileTimeseries
range: string
required: false
multivalued: false

```
</details>