

# Slot: adeOfBuildingRoom 


_Augments the BuildingRoom with properties defined in an ADE._





URI: [citygml:adeOfBuildingRoom](https://www.ogc.org/standards/citygml/adeOfBuildingRoom)
Alias: adeOfBuildingRoom

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BuildingRoom](BuildingRoom.md) | A BuildingRoom is a space within a Building or BuildingPart intended for huma... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfBuildingRoom](ADEOfBuildingRoom.md) |
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
| self | citygml:adeOfBuildingRoom |
| native | citygml:adeOfBuildingRoom |




## LinkML Source

<details>
```yaml
name: adeOfBuildingRoom
description: Augments the BuildingRoom with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfBuildingRoom
owner: BuildingRoom
domain_of:
- BuildingRoom
range: ADEOfBuildingRoom
required: false
multivalued: true

```
</details>