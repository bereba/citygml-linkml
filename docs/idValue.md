

# Slot: idValue 


_Specifies the value of the identifier for which the time-value-pairs are to be selected._





URI: [citygml:idValue](https://www.ogc.org/standards/citygml/idValue)
Alias: idValue

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
| self | citygml:idValue |
| native | citygml:idValue |




## LinkML Source

<details>
```yaml
name: idValue
description: Specifies the value of the identifier for which the time-value-pairs
  are to be selected.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: idValue
owner: TabulatedFileTimeseries
domain_of:
- TabulatedFileTimeseries
range: string
required: false
multivalued: false

```
</details>