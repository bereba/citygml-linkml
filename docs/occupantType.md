

# Slot: occupantType 


_Indicates the specific type of the occupants that are contained by a feature._





URI: [citygml:occupantType](https://www.ogc.org/standards/citygml/occupantType)
Alias: occupantType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Occupancy](Occupancy.md) | Occupancy is an application-dependent indication of what is contained by a fe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OccupantTypeValue](OccupantTypeValue.md) |
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
| self | citygml:occupantType |
| native | citygml:occupantType |




## LinkML Source

<details>
```yaml
name: occupantType
description: Indicates the specific type of the occupants that are contained by a
  feature.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: occupantType
owner: Occupancy
domain_of:
- Occupancy
range: OccupantTypeValue
required: false
multivalued: false

```
</details>