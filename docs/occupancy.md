

# Slot: occupancy 



URI: [citygml:occupancy](https://www.ogc.org/standards/citygml/occupancy)
Alias: occupancy

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Building](Building.md) | A Building is a free-standing, self-supporting construction that is roofed, u... |  no  |
| [Railway](Railway.md) | A Railway is a transportation space used by wheeled vehicles on rails |  no  |
| [Waterway](Waterway.md) | A Waterway is a transportation space used for the movement of vessels upon or... |  no  |
| [Bridge](Bridge.md) | A Bridge represents a structure that affords the passage of pedestrians, anim... |  no  |
| [OtherConstruction](OtherConstruction.md) | An OtherConstruction is a construction that is not covered by any of the othe... |  no  |
| [AbstractBridge](AbstractBridge.md) | AbstractBridge is an abstract superclass representing the common attributes a... |  no  |
| [Track](Track.md) | A Track is a small path mainly used by pedestrians |  no  |
| [Intersection](Intersection.md) | An Intersection is a transportation space that is a shared segment of multipl... |  no  |
| [Tunnel](Tunnel.md) | A Tunnel represents a horizontal or sloping enclosed passage way of a certain... |  no  |
| [Section](Section.md) | A Section is a transportation space that is a segment of a Road, Railway, Tra... |  no  |
| [AbstractBuilding](AbstractBuilding.md) | AbstractBuilding is an abstract superclass representing the common attributes... |  no  |
| [Road](Road.md) | A Road is a transportation space used by vehicles, bicycles and/or pedestrian... |  no  |
| [AbstractTransportationSpace](AbstractTransportationSpace.md) | AbstractTransportationSpace is the abstract superclass of transportation obje... |  no  |
| [TunnelPart](TunnelPart.md) | A TunnelPart is a physical or functional subdivision of a Tunnel |  no  |
| [BuildingPart](BuildingPart.md) | A BuildingPart is a physical or functional subdivision of a Building |  no  |
| [AbstractConstruction](AbstractConstruction.md) | AbstractConstruction is the abstract superclass for objects that are manufact... |  no  |
| [Square](Square.md) | A Square is a transportation space for unrestricted movement for vehicles, bi... |  no  |
| [BridgePart](BridgePart.md) | A BridgePart is a physical or functional subdivision of a Bridge |  no  |
| [TrafficSpace](TrafficSpace.md) | A TrafficSpace is a space in which traffic takes place |  no  |
| [AbstractTunnel](AbstractTunnel.md) | AbstractTunnel is an abstract superclass representing the common attributes a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AbstractConstruction](AbstractConstruction.md), [AbstractTransportationSpace](AbstractTransportationSpace.md), [TrafficSpace](TrafficSpace.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:occupancy |
| native | citygml:occupancy |




## LinkML Source

<details>
```yaml
name: occupancy
alias: occupancy
domain_of:
- AbstractConstruction
- AbstractTransportationSpace
- TrafficSpace
range: string

```
</details>