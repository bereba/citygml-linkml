

# Slot: storeysAboveGround 


_Indicates the number of storeys positioned above ground level._





URI: [citygml:storeysAboveGround](https://www.ogc.org/standards/citygml/storeysAboveGround)
Alias: storeysAboveGround

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
| self | citygml:storeysAboveGround |
| native | citygml:storeysAboveGround |




## LinkML Source

<details>
```yaml
name: storeysAboveGround
description: Indicates the number of storeys positioned above ground level.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: storeysAboveGround
owner: AbstractBuilding
domain_of:
- AbstractBuilding
range: integer
required: false
multivalued: false

```
</details>