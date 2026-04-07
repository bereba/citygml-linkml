

# Slot: storeyHeightsAboveGround 


_Lists the heights of each storey above ground. The first value in the list denotes the height of the storey closest to the ground level, the last value denotes the height furthest away._





URI: [citygml:storeyHeightsAboveGround](https://www.ogc.org/standards/citygml/storeyHeightsAboveGround)
Alias: storeyHeightsAboveGround

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
| Range | [String](String.md) |
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
| self | citygml:storeyHeightsAboveGround |
| native | citygml:storeyHeightsAboveGround |




## LinkML Source

<details>
```yaml
name: storeyHeightsAboveGround
description: Lists the heights of each storey above ground. The first value in the
  list denotes the height of the storey closest to the ground level, the last value
  denotes the height furthest away.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: storeyHeightsAboveGround
owner: AbstractBuilding
domain_of:
- AbstractBuilding
range: string
required: false
multivalued: false

```
</details>