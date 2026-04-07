

# Slot: buildingInstallation 



URI: [citygml:buildingInstallation](https://www.ogc.org/standards/citygml/buildingInstallation)
Alias: buildingInstallation

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
| [BuildingRoom](BuildingRoom.md) | A BuildingRoom is a space within a Building or BuildingPart intended for huma... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AbstractBuilding](AbstractBuilding.md), [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md), [BuildingRoom](BuildingRoom.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:buildingInstallation |
| native | citygml:buildingInstallation |




## LinkML Source

<details>
```yaml
name: buildingInstallation
alias: buildingInstallation
domain_of:
- AbstractBuilding
- AbstractBuildingSubdivision
- BuildingRoom
range: string

```
</details>