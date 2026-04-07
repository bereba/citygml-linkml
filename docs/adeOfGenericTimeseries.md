

# Slot: adeOfGenericTimeseries 


_Augments the GenericTimeseries with properties defined in an ADE._





URI: [citygml:adeOfGenericTimeseries](https://www.ogc.org/standards/citygml/adeOfGenericTimeseries)
Alias: adeOfGenericTimeseries

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenericTimeseries](GenericTimeseries.md) | A GenericTimeseries represents time-varying data in the form of embedded time... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfGenericTimeseries](ADEOfGenericTimeseries.md) |
| Domain Of | [GenericTimeseries](GenericTimeseries.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | citygml:adeOfGenericTimeseries |
| native | citygml:adeOfGenericTimeseries |




## LinkML Source

<details>
```yaml
name: adeOfGenericTimeseries
description: Augments the GenericTimeseries with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfGenericTimeseries
owner: GenericTimeseries
domain_of:
- GenericTimeseries
range: ADEOfGenericTimeseries
required: false
multivalued: true

```
</details>