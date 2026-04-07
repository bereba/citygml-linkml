

# Slot: adeOfTabulatedFileTimeseries 


_Augments the TabulatedFileTimeseries with properties defined in an ADE._





URI: [citygml:adeOfTabulatedFileTimeseries](https://www.ogc.org/standards/citygml/adeOfTabulatedFileTimeseries)
Alias: adeOfTabulatedFileTimeseries

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TabulatedFileTimeseries](TabulatedFileTimeseries.md) | A TabulatedFileTimeseries represents time-varying data of a specific data typ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfTabulatedFileTimeseries](ADEOfTabulatedFileTimeseries.md) |
| Domain Of | [TabulatedFileTimeseries](TabulatedFileTimeseries.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | citygml:adeOfTabulatedFileTimeseries |
| native | citygml:adeOfTabulatedFileTimeseries |




## LinkML Source

<details>
```yaml
name: adeOfTabulatedFileTimeseries
description: Augments the TabulatedFileTimeseries with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfTabulatedFileTimeseries
owner: TabulatedFileTimeseries
domain_of:
- TabulatedFileTimeseries
range: ADEOfTabulatedFileTimeseries
required: false
multivalued: true

```
</details>