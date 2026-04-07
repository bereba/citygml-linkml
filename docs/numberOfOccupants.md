

# Slot: numberOfOccupants 


_Indicates the number of occupants contained by a feature._





URI: [citygml:numberOfOccupants](https://www.ogc.org/standards/citygml/numberOfOccupants)
Alias: numberOfOccupants

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Occupancy](Occupancy.md) | Occupancy is an application-dependent indication of what is contained by a fe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Occupancy](Occupancy.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | citygml:numberOfOccupants |
| native | citygml:numberOfOccupants |




## LinkML Source

<details>
```yaml
name: numberOfOccupants
description: Indicates the number of occupants contained by a feature.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: numberOfOccupants
owner: Occupancy
domain_of:
- Occupancy
range: integer
required: true
multivalued: false

```
</details>