

# Slot: adeOfAbstractUnoccupiedSpace 


_Augments AbstractUnoccupiedSpace with properties defined in an ADE._





URI: [citygml:adeOfAbstractUnoccupiedSpace](https://www.ogc.org/standards/citygml/adeOfAbstractUnoccupiedSpace)
Alias: adeOfAbstractUnoccupiedSpace

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Section](Section.md) | A Section is a transportation space that is a segment of a Road, Railway, Tra... |  no  |
| [AuxiliaryTrafficSpace](AuxiliaryTrafficSpace.md) | An AuxiliaryTrafficSpace is a space within the transportation space not inten... |  no  |
| [ClearanceSpace](ClearanceSpace.md) | A ClearanceSpace represents the actual free space above a TrafficArea within ... |  no  |
| [Hole](Hole.md) | A Hole is an opening in the surface of a Road, Track or Square such as road d... |  no  |
| [AbstractUnoccupiedSpace](AbstractUnoccupiedSpace.md) | AbstractUnoccupiedSpace is the abstract superclass for all types of physicall... |  no  |
| [Waterway](Waterway.md) | A Waterway is a transportation space used for the movement of vessels upon or... |  no  |
| [HollowSpace](HollowSpace.md) | A HollowSpace is a space within a Tunnel or TunnelPart intended for certain f... |  no  |
| [Railway](Railway.md) | A Railway is a transportation space used by wheeled vehicles on rails |  no  |
| [Road](Road.md) | A Road is a transportation space used by vehicles, bicycles and/or pedestrian... |  no  |
| [Track](Track.md) | A Track is a small path mainly used by pedestrians |  no  |
| [Intersection](Intersection.md) | An Intersection is a transportation space that is a shared segment of multipl... |  no  |
| [BridgeRoom](BridgeRoom.md) | A BridgeRoom is a space within a Bridge or BridgePart intended for human occu... |  no  |
| [Square](Square.md) | A Square is a transportation space for unrestricted movement for vehicles, bi... |  no  |
| [AbstractTransportationSpace](AbstractTransportationSpace.md) | AbstractTransportationSpace is the abstract superclass of transportation obje... |  no  |
| [BuildingRoom](BuildingRoom.md) | A BuildingRoom is a space within a Building or BuildingPart intended for huma... |  no  |
| [TrafficSpace](TrafficSpace.md) | A TrafficSpace is a space in which traffic takes place |  no  |
| [GenericUnoccupiedSpace](GenericUnoccupiedSpace.md) | A GenericUnoccupiedSpace is a space that is not represented by any explicitly... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractUnoccupiedSpace](ADEOfAbstractUnoccupiedSpace.md) |
| Domain Of | [AbstractUnoccupiedSpace](AbstractUnoccupiedSpace.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractUnoccupiedSpace](AbstractUnoccupiedSpace.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractUnoccupiedSpace |
| native | citygml:adeOfAbstractUnoccupiedSpace |




## LinkML Source

<details>
```yaml
name: adeOfAbstractUnoccupiedSpace
description: Augments AbstractUnoccupiedSpace with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractUnoccupiedSpace
owner: AbstractUnoccupiedSpace
domain_of:
- AbstractUnoccupiedSpace
range: ADEOfAbstractUnoccupiedSpace
required: false
multivalued: true

```
</details>