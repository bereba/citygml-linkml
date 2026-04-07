

# Slot: lod3ImplicitRepresentation 


_Relates to an implicit geometry that represents the occupied space in Level of Detail 3._





URI: [citygml:lod3ImplicitRepresentation](https://www.ogc.org/standards/citygml/lod3ImplicitRepresentation)
Alias: lod3ImplicitRepresentation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Building](Building.md) | A Building is a free-standing, self-supporting construction that is roofed, u... |  no  |
| [TunnelFurniture](TunnelFurniture.md) | A TunnelFurniture is an equipment for occupant use, usually not fixed to the ... |  no  |
| [SolitaryVegetationObject](SolitaryVegetationObject.md) | A SolitaryVegetationObject represents individual vegetation objects, e |  no  |
| [Window](Window.md) | A Window is a construction for closing an opening in a wall  or roof, primari... |  no  |
| [AbstractInstallation](AbstractInstallation.md) | AbstractInstallation is the abstract superclass for the representation of ins... |  no  |
| [AbstractOccupiedSpace](AbstractOccupiedSpace.md) | AbstractOccupiedSpace is the abstract superclass for all types of physically ... |  no  |
| [Bridge](Bridge.md) | A Bridge represents a structure that affords the passage of pedestrians, anim... |  no  |
| [OtherConstruction](OtherConstruction.md) | An OtherConstruction is a construction that is not covered by any of the othe... |  no  |
| [AbstractBridge](AbstractBridge.md) | AbstractBridge is an abstract superclass representing the common attributes a... |  no  |
| [AbstractFurniture](AbstractFurniture.md) | AbstractFurniture is the abstract superclass for the representation of furnit... |  no  |
| [PlantCover](PlantCover.md) | A PlantCover represents a space covered by vegetation |  no  |
| [BridgeFurniture](BridgeFurniture.md) | A BridgeFurniture is an equipment for occupant use, usually not fixed to the ... |  no  |
| [Tunnel](Tunnel.md) | A Tunnel represents a horizontal or sloping enclosed passage way of a certain... |  no  |
| [TunnelInstallation](TunnelInstallation.md) | A TunnelInstallation is a permanent part of a Tunnel (inside and/or outside) ... |  no  |
| [AbstractBuilding](AbstractBuilding.md) | AbstractBuilding is an abstract superclass representing the common attributes... |  no  |
| [BridgeInstallation](BridgeInstallation.md) | A BridgeInstallation is a permanent part of a Bridge (inside and/or outside) ... |  no  |
| [AbstractVegetationObject](AbstractVegetationObject.md) | AbstractVegetationObject is the abstract superclass for all kinds of vegetati... |  no  |
| [TunnelConstructiveElement](TunnelConstructiveElement.md) | A TunnelConstructiveElement is an element of a Tunnel which is essential from... |  no  |
| [CityFurniture](CityFurniture.md) | CityFurniture is an object or piece of equipment installed in the outdoor env... |  no  |
| [TunnelPart](TunnelPart.md) | A TunnelPart is a physical or functional subdivision of a Tunnel |  no  |
| [BridgeConstructiveElement](BridgeConstructiveElement.md) | A BridgeConstructiveElement is an element of a bridge which is essential from... |  no  |
| [Door](Door.md) | A Door is a construction for closing an opening intended primarily for access... |  no  |
| [WaterBody](WaterBody.md) | A WaterBody represents significant and permanent or semi-permanent accumulati... |  no  |
| [AbstractConstructiveElement](AbstractConstructiveElement.md) | AbstractConstructiveElement is the abstract superclass for the representation... |  no  |
| [BuildingFurniture](BuildingFurniture.md) | A BuildingFurniture is an equipment for occupant use, usually not fixed to th... |  no  |
| [BuildingPart](BuildingPart.md) | A BuildingPart is a physical or functional subdivision of a Building |  no  |
| [AbstractConstruction](AbstractConstruction.md) | AbstractConstruction is the abstract superclass for objects that are manufact... |  no  |
| [BridgePart](BridgePart.md) | A BridgePart is a physical or functional subdivision of a Bridge |  no  |
| [BuildingInstallation](BuildingInstallation.md) | A BuildingInstallation is a permanent part of a Building (inside and/or outsi... |  no  |
| [AbstractFillingElement](AbstractFillingElement.md) | AbstractFillingElement is the abstract superclass for different kinds of elem... |  no  |
| [GenericOccupiedSpace](GenericOccupiedSpace.md) | A GenericOccupiedSpace is a space that is not represented by any explicitly m... |  no  |
| [BuildingConstructiveElement](BuildingConstructiveElement.md) | A BuildingConstructiveElement is an element of a Building which is essential ... |  no  |
| [AbstractTunnel](AbstractTunnel.md) | AbstractTunnel is an abstract superclass representing the common attributes a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImplicitGeometry](ImplicitGeometry.md) |
| Domain Of | [AbstractOccupiedSpace](AbstractOccupiedSpace.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractOccupiedSpace](AbstractOccupiedSpace.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:lod3ImplicitRepresentation |
| native | citygml:lod3ImplicitRepresentation |




## LinkML Source

<details>
```yaml
name: lod3ImplicitRepresentation
description: Relates to an implicit geometry that represents the occupied space in
  Level of Detail 3.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: lod3ImplicitRepresentation
owner: AbstractOccupiedSpace
domain_of:
- AbstractOccupiedSpace
range: ImplicitGeometry
required: false
multivalued: false

```
</details>