

# Slot: address 



URI: [citygml:address](https://www.ogc.org/standards/citygml/address)
Alias: address

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Building](Building.md) | A Building is a free-standing, self-supporting construction that is roofed, u... |  no  |
| [Door](Door.md) | A Door is a construction for closing an opening intended primarily for access... |  no  |
| [AbstractBuilding](AbstractBuilding.md) | AbstractBuilding is an abstract superclass representing the common attributes... |  no  |
| [Bridge](Bridge.md) | A Bridge represents a structure that affords the passage of pedestrians, anim... |  no  |
| [AbstractBridge](AbstractBridge.md) | AbstractBridge is an abstract superclass representing the common attributes a... |  no  |
| [BuildingPart](BuildingPart.md) | A BuildingPart is a physical or functional subdivision of a Building |  no  |
| [BridgePart](BridgePart.md) | A BridgePart is a physical or functional subdivision of a Bridge |  no  |
| [BuildingUnit](BuildingUnit.md) | A BuildingUnit is a logical subdivision of a Building |  no  |
| [DoorSurface](DoorSurface.md) | A DoorSurface is either a boundary surface of a Door feature or a surface tha... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Door](Door.md), [DoorSurface](DoorSurface.md), [AbstractBridge](AbstractBridge.md), [AbstractBuilding](AbstractBuilding.md), [BuildingUnit](BuildingUnit.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:address |
| native | citygml:address |




## LinkML Source

<details>
```yaml
name: address
alias: address
domain_of:
- Door
- DoorSurface
- AbstractBridge
- AbstractBuilding
- BuildingUnit
range: string

```
</details>