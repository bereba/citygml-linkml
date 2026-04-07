

# Slot: interval 


_Indicates the time period the occupants are contained by a feature._





URI: [citygml:interval](https://www.ogc.org/standards/citygml/interval)
Alias: interval

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Occupancy](Occupancy.md) | Occupancy is an application-dependent indication of what is contained by a fe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IntervalValue](IntervalValue.md) |
| Domain Of | [Occupancy](Occupancy.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Occupancy](Occupancy.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:interval |
| native | citygml:interval |




## LinkML Source

<details>
```yaml
name: interval
description: Indicates the time period the occupants are contained by a feature.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: interval
owner: Occupancy
domain_of:
- Occupancy
range: IntervalValue
required: false
multivalued: false

```
</details>