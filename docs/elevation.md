

# Slot: elevation 



URI: [citygml:elevation](https://www.ogc.org/standards/citygml/elevation)
Alias: elevation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Building](Building.md) | A Building is a free-standing, self-supporting construction that is roofed, u... |  no  |
| [Storey](Storey.md) | A Storey is typically a horizontal section of a Building |  no  |
| [AbstractBuilding](AbstractBuilding.md) | AbstractBuilding is an abstract superclass representing the common attributes... |  no  |
| [Bridge](Bridge.md) | A Bridge represents a structure that affords the passage of pedestrians, anim... |  no  |
| [OtherConstruction](OtherConstruction.md) | An OtherConstruction is a construction that is not covered by any of the othe... |  no  |
| [AbstractBridge](AbstractBridge.md) | AbstractBridge is an abstract superclass representing the common attributes a... |  no  |
| [AbstractConstruction](AbstractConstruction.md) | AbstractConstruction is the abstract superclass for objects that are manufact... |  no  |
| [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) | AbstractBuildingSubdivision is the abstract superclass for different kinds of... |  no  |
| [BuildingPart](BuildingPart.md) | A BuildingPart is a physical or functional subdivision of a Building |  no  |
| [BridgePart](BridgePart.md) | A BridgePart is a physical or functional subdivision of a Bridge |  no  |
| [TunnelPart](TunnelPart.md) | A TunnelPart is a physical or functional subdivision of a Tunnel |  no  |
| [BuildingUnit](BuildingUnit.md) | A BuildingUnit is a logical subdivision of a Building |  no  |
| [Tunnel](Tunnel.md) | A Tunnel represents a horizontal or sloping enclosed passage way of a certain... |  no  |
| [AbstractTunnel](AbstractTunnel.md) | AbstractTunnel is an abstract superclass representing the common attributes a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AbstractConstruction](AbstractConstruction.md), [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:elevation |
| native | citygml:elevation |




## LinkML Source

<details>
```yaml
name: elevation
alias: elevation
domain_of:
- AbstractConstruction
- AbstractBuildingSubdivision
range: string

```
</details>