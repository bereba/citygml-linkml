

# Slot: buildingSubdivision 


_Relates the logical subdivisions to the Building or BuildingPart._





URI: [citygml:buildingSubdivision](https://www.ogc.org/standards/citygml/buildingSubdivision)
Alias: buildingSubdivision

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
| Range | [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) |
| Domain Of | [AbstractBuilding](AbstractBuilding.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | citygml:buildingSubdivision |
| native | citygml:buildingSubdivision |




## LinkML Source

<details>
```yaml
name: buildingSubdivision
description: Relates the logical subdivisions to the Building or BuildingPart.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: buildingSubdivision
owner: AbstractBuilding
domain_of:
- AbstractBuilding
range: AbstractBuildingSubdivision
required: false
multivalued: true

```
</details>