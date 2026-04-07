

# Slot: buildingRoom 



URI: [citygml:buildingRoom](https://www.ogc.org/standards/citygml/buildingRoom)
Alias: buildingRoom

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Building](Building.md) | A Building is a free-standing, self-supporting construction that is roofed, u... |  no  |
| [Storey](Storey.md) | A Storey is typically a horizontal section of a Building |  no  |
| [AbstractBuilding](AbstractBuilding.md) | AbstractBuilding is an abstract superclass representing the common attributes... |  no  |
| [BuildingPart](BuildingPart.md) | A BuildingPart is a physical or functional subdivision of a Building |  no  |
| [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) | AbstractBuildingSubdivision is the abstract superclass for different kinds of... |  no  |
| [BuildingUnit](BuildingUnit.md) | A BuildingUnit is a logical subdivision of a Building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AbstractBuilding](AbstractBuilding.md), [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:buildingRoom |
| native | citygml:buildingRoom |




## LinkML Source

<details>
```yaml
name: buildingRoom
alias: buildingRoom
domain_of:
- AbstractBuilding
- AbstractBuildingSubdivision
range: string

```
</details>