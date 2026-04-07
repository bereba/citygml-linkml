

# Slot: idColumnName 


_Specifies the name of the column that stores the identifier of the time-value-pair._





URI: [citygml:idColumnName](https://www.ogc.org/standards/citygml/idColumnName)
Alias: idColumnName

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
| self | citygml:idColumnName |
| native | citygml:idColumnName |




## LinkML Source

<details>
```yaml
name: idColumnName
description: Specifies the name of the column that stores the identifier of the time-value-pair.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: idColumnName
owner: TabulatedFileTimeseries
domain_of:
- TabulatedFileTimeseries
range: string
required: false
multivalued: false

```
</details>