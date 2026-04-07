

# Slot: storeysBelowGround 


_Indicates the number of storeys positioned below ground level._





URI: [citygml:storeysBelowGround](https://www.ogc.org/standards/citygml/storeysBelowGround)
Alias: storeysBelowGround

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Building](Building.md) | A Building is a free-standing, self-supporting construction that is roofed, u... |  no  |
| [AbstractBuilding](AbstractBuilding.md) | AbstractBuilding is an abstract superclass representing the common attributes... |  no  |
| [BuildingPart](BuildingPart.md) | A BuildingPart is a physical or functional subdivision of a Building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [AbstractBuilding](AbstractBuilding.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractBuilding](AbstractBuilding.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:storeysBelowGround |
| native | citygml:storeysBelowGround |




## LinkML Source

<details>
```yaml
name: storeysBelowGround
description: Indicates the number of storeys positioned below ground level.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: storeysBelowGround
owner: AbstractBuilding
domain_of:
- AbstractBuilding
range: integer
required: false
multivalued: false

```
</details>