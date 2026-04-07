

# Slot: roomHeight 


_Specifies qualified heights of the BuildingRoom._





URI: [citygml:roomHeight](https://www.ogc.org/standards/citygml/roomHeight)
Alias: roomHeight

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BuildingRoom](BuildingRoom.md) | A BuildingRoom is a space within a Building or BuildingPart intended for huma... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RoomHeight](RoomHeight.md) |
| Domain Of | [BuildingRoom](BuildingRoom.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BuildingRoom](BuildingRoom.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:roomHeight |
| native | citygml:roomHeight |




## LinkML Source

<details>
```yaml
name: roomHeight
description: Specifies qualified heights of the BuildingRoom.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: roomHeight
owner: BuildingRoom
domain_of:
- BuildingRoom
range: RoomHeight
required: false
multivalued: true

```
</details>