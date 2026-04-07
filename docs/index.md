# OGC CityGML 3.0

!!! note

    This documentation has been build with an automated pipeline as defined in this repository using linkml and takes no responsibility for unfulfilled stanadards or incomplete information.

LinkML schema generated from OGC CityGML 3.0 UML/XMI model (Enterprise Architect export)

URI: https://www.ogc.org/standards/citygml

Name: citygml



## Classes

| Class | Description |
| --- | --- |
| [AbstractFeature](AbstractFeature.md) | AbstractFeature is the abstract superclass of all feature types within the Ci... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md) | AbstractFeatureWithLifespan is the base class for all CityGML features |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractAppearance](AbstractAppearance.md) | AbstractAppearance is the abstract superclass to represent any kind of appear... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Appearance](Appearance.md) | An Appearance is a collection of surface data, i |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractCityObject](AbstractCityObject.md) | AbstractCityObject is the abstract superclass of all thematic classes within ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractSpace](AbstractSpace.md) | AbstractSpace is the abstract superclass for all types of spaces |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractLogicalSpace](AbstractLogicalSpace.md) | AbstractLogicalSpace is the abstract superclass for all types of logical spac... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) | AbstractBuildingSubdivision is the abstract superclass for different kinds of... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BuildingUnit](BuildingUnit.md) | A BuildingUnit is a logical subdivision of a Building |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Storey](Storey.md) | A Storey is typically a horizontal section of a Building |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CityObjectGroup](CityObjectGroup.md) | A CityObjectGroup represents an application-specific aggregation of city obje... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenericLogicalSpace](GenericLogicalSpace.md) | A GenericLogicalSpace is a space that is not represented by any explicitly mo... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractPhysicalSpace](AbstractPhysicalSpace.md) | AbstractPhysicalSpace is the abstract superclass for all types of physical sp... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractOccupiedSpace](AbstractOccupiedSpace.md) | AbstractOccupiedSpace is the abstract superclass for all types of physically ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractConstruction](AbstractConstruction.md) | AbstractConstruction is the abstract superclass for objects that are manufact... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractBridge](AbstractBridge.md) | AbstractBridge is an abstract superclass representing the common attributes a... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bridge](Bridge.md) | A Bridge represents a structure that affords the passage of pedestrians, anim... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BridgePart](BridgePart.md) | A BridgePart is a physical or functional subdivision of a Bridge |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractBuilding](AbstractBuilding.md) | AbstractBuilding is an abstract superclass representing the common attributes... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Building](Building.md) | A Building is a free-standing, self-supporting construction that is roofed, u... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BuildingPart](BuildingPart.md) | A BuildingPart is a physical or functional subdivision of a Building |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractTunnel](AbstractTunnel.md) | AbstractTunnel is an abstract superclass representing the common attributes a... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Tunnel](Tunnel.md) | A Tunnel represents a horizontal or sloping enclosed passage way of a certain... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TunnelPart](TunnelPart.md) | A TunnelPart is a physical or functional subdivision of a Tunnel |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OtherConstruction](OtherConstruction.md) | An OtherConstruction is a construction that is not covered by any of the othe... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractConstructiveElement](AbstractConstructiveElement.md) | AbstractConstructiveElement is the abstract superclass for the representation... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BridgeConstructiveElement](BridgeConstructiveElement.md) | A BridgeConstructiveElement is an element of a bridge which is essential from... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BuildingConstructiveElement](BuildingConstructiveElement.md) | A BuildingConstructiveElement is an element of a Building which is essential ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TunnelConstructiveElement](TunnelConstructiveElement.md) | A TunnelConstructiveElement is an element of a Tunnel which is essential from... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractFillingElement](AbstractFillingElement.md) | AbstractFillingElement is the abstract superclass for different kinds of elem... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Door](Door.md) | A Door is a construction for closing an opening intended primarily for access... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Window](Window.md) | A Window is a construction for closing an opening in a wall  or roof, primari... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractFurniture](AbstractFurniture.md) | AbstractFurniture is the abstract superclass for the representation of furnit... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BridgeFurniture](BridgeFurniture.md) | A BridgeFurniture is an equipment for occupant use, usually not fixed to the ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BuildingFurniture](BuildingFurniture.md) | A BuildingFurniture is an equipment for occupant use, usually not fixed to th... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TunnelFurniture](TunnelFurniture.md) | A TunnelFurniture is an equipment for occupant use, usually not fixed to the ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractInstallation](AbstractInstallation.md) | AbstractInstallation is the abstract superclass for the representation of ins... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BridgeInstallation](BridgeInstallation.md) | A BridgeInstallation is a permanent part of a Bridge (inside and/or outside) ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BuildingInstallation](BuildingInstallation.md) | A BuildingInstallation is a permanent part of a Building (inside and/or outsi... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TunnelInstallation](TunnelInstallation.md) | A TunnelInstallation is a permanent part of a Tunnel (inside and/or outside) ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractVegetationObject](AbstractVegetationObject.md) | AbstractVegetationObject is the abstract superclass for all kinds of vegetati... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PlantCover](PlantCover.md) | A PlantCover represents a space covered by vegetation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SolitaryVegetationObject](SolitaryVegetationObject.md) | A SolitaryVegetationObject represents individual vegetation objects, e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CityFurniture](CityFurniture.md) | CityFurniture is an object or piece of equipment installed in the outdoor env... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenericOccupiedSpace](GenericOccupiedSpace.md) | A GenericOccupiedSpace is a space that is not represented by any explicitly m... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[WaterBody](WaterBody.md) | A WaterBody represents significant and permanent or semi-permanent accumulati... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractUnoccupiedSpace](AbstractUnoccupiedSpace.md) | AbstractUnoccupiedSpace is the abstract superclass for all types of physicall... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractTransportationSpace](AbstractTransportationSpace.md) | AbstractTransportationSpace is the abstract superclass of transportation obje... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Intersection](Intersection.md) | An Intersection is a transportation space that is a shared segment of multipl... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Railway](Railway.md) | A Railway is a transportation space used by wheeled vehicles on rails |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Road](Road.md) | A Road is a transportation space used by vehicles, bicycles and/or pedestrian... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Section](Section.md) | A Section is a transportation space that is a segment of a Road, Railway, Tra... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Square](Square.md) | A Square is a transportation space for unrestricted movement for vehicles, bi... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Track](Track.md) | A Track is a small path mainly used by pedestrians |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Waterway](Waterway.md) | A Waterway is a transportation space used for the movement of vessels upon or... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AuxiliaryTrafficSpace](AuxiliaryTrafficSpace.md) | An AuxiliaryTrafficSpace is a space within the transportation space not inten... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BridgeRoom](BridgeRoom.md) | A BridgeRoom is a space within a Bridge or BridgePart intended for human occu... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BuildingRoom](BuildingRoom.md) | A BuildingRoom is a space within a Building or BuildingPart intended for huma... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClearanceSpace](ClearanceSpace.md) | A ClearanceSpace represents the actual free space above a TrafficArea within ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenericUnoccupiedSpace](GenericUnoccupiedSpace.md) | A GenericUnoccupiedSpace is a space that is not represented by any explicitly... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Hole](Hole.md) | A Hole is an opening in the surface of a Road, Track or Square such as road d... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HollowSpace](HollowSpace.md) | A HollowSpace is a space within a Tunnel or TunnelPart intended for certain f... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TrafficSpace](TrafficSpace.md) | A TrafficSpace is a space in which traffic takes place |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractSpaceBoundary](AbstractSpaceBoundary.md) | AbstractSpaceBoundary is the abstract superclass for all types of space bound... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractReliefComponent](AbstractReliefComponent.md) | An AbstractReliefComponent represents an element of the terrain surface - eit... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BreaklineRelief](BreaklineRelief.md) | A BreaklineRelief represents a terrain component with 3D lines |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MassPointRelief](MassPointRelief.md) | A MassPointRelief represents a terrain component as a collection of 3D points |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RasterRelief](RasterRelief.md) | A RasterRelief represents a terrain component as a regular raster or grid |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TINRelief](TINRelief.md) | A TINRelief represents a terrain component as a triangulated irregular networ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractThematicSurface](AbstractThematicSurface.md) | AbstractThematicSurface is the abstract superclass for all types of thematic ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractConstructionSurface](AbstractConstructionSurface.md) | AbstractConstructionSurface is the abstract superclass for different kinds of... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CeilingSurface](CeilingSurface.md) | A CeilingSurface is a surface that represents the interior ceiling of a const... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FloorSurface](FloorSurface.md) | A FloorSurface is surface that represents the interior floor of a constructio... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GroundSurface](GroundSurface.md) | A GroundSurface is a surface that represents the ground plate of a constructi... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InteriorWallSurface](InteriorWallSurface.md) | An InteriorWallSurface is a surface that is visible from inside a constructio... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OuterCeilingSurface](OuterCeilingSurface.md) | An OuterCeilingSurface is a surface that belongs to the outer building shell ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OuterFloorSurface](OuterFloorSurface.md) | An OuterFloorSurface is a surface that belongs to the outer construction shel... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RoofSurface](RoofSurface.md) | A RoofSurface is a surface that delimits major roof parts of a construction |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[WallSurface](WallSurface.md) | A WallSurface is a surface that is part of the building facade visible from t... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractFillingSurface](AbstractFillingSurface.md) | AbstractFillingSurface is the abstract superclass for different kinds of surf... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DoorSurface](DoorSurface.md) | A DoorSurface is either a boundary surface of a Door feature or a surface tha... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[WindowSurface](WindowSurface.md) | A WindowSurface is either a boundary surface of a Window feature or a surface... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractWaterBoundarySurface](AbstractWaterBoundarySurface.md) | AbstractWaterBoundarySurface is the abstract superclass for all kinds of them... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[WaterGroundSurface](WaterGroundSurface.md) | A WaterGroundSurface represents the exterior boundary surface of the submerge... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[WaterSurface](WaterSurface.md) | A WaterSurface represents the upper exterior interface between a water body a... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AuxiliaryTrafficArea](AuxiliaryTrafficArea.md) | An AuxiliaryTrafficArea is the ground surface of an AuxiliaryTrafficSpace |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClosureSurface](ClosureSurface.md) | ClosureSurface is a special type of thematic surface used to close holes in v... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenericThematicSurface](GenericThematicSurface.md) | A GenericThematicSurface is a surface that is not represented by any explicit... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HoleSurface](HoleSurface.md) | A HoleSurface is a representation of the ground surface of a hole |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LandUse](LandUse.md) | A LandUse object is an area of the earth's surface dedicated to a specific la... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Marking](Marking.md) | A Marking is a visible pattern on a transportation area relevant to the struc... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TrafficArea](TrafficArea.md) | A TrafficArea is the ground surface of a TrafficSpace |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ReliefFeature](ReliefFeature.md) | A ReliefFeature is a collection of terrain components representing the Earth'... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractDynamizer](AbstractDynamizer.md) | AbstractDynamizer is the abstract superclass to represent Dynamizer objects |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Dynamizer](Dynamizer.md) | A Dynamizer is an object that injects timeseries data for an individual attri... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractVersion](AbstractVersion.md) | AbstractVersion is the abstract superclass to represent Version objects |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Version](Version.md) | Version represents a defined state of a city model consisting of the dedicate... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractVersionTransition](AbstractVersionTransition.md) | AbstractVersionTransition is the abstract superclass to represent VersionTran... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VersionTransition](VersionTransition.md) | VersionTransition describes the change of the state of a city model from one ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CityModel](CityModel.md) | CityModel is the container for all objects belonging to a city model |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractPointCloud](AbstractPointCloud.md) | AbstractPointCloud is the abstract superclass to represent PointCloud objects |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PointCloud](PointCloud.md) | A PointCloud is an unordered collection of points that is a sampling of the g... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractSurfaceData](AbstractSurfaceData.md) | AbstractSurfaceData is the abstract superclass for different kinds of texture... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractTexture](AbstractTexture.md) | AbstractTexture is the abstract superclass to represent the common attributes... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeoreferencedTexture](GeoreferencedTexture.md) | A GeoreferencedTexture is a texture that uses a planimetric projection |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ParameterizedTexture](ParameterizedTexture.md) | A ParameterizedTexture is a texture that uses texture coordinates or a transf... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[X3DMaterial](X3DMaterial.md) | X3DMaterial defines properties for surface geometry objects based on the mate... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractTimeseries](AbstractTimeseries.md) | AbstractTimeseries is the abstract superclass representing any type of timese... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AbstractAtomicTimeseries](AbstractAtomicTimeseries.md) | AbstractAtomicTimeseries represents the attributes and relationships that are... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenericTimeseries](GenericTimeseries.md) | A GenericTimeseries represents time-varying data in the form of embedded time... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StandardFileTimeseries](StandardFileTimeseries.md) | A StandardFileTimeseries represents time-varying data for a single contiguous... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TabulatedFileTimeseries](TabulatedFileTimeseries.md) | A TabulatedFileTimeseries represents time-varying data of a specific data typ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CompositeTimeseries](CompositeTimeseries.md) | A CompositeTimeseries is a (possibly recursive) aggregation of atomic and com... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Address](Address.md) | Address represents an address of a city object |
| [AbstractGenericAttribute](AbstractGenericAttribute.md) | AbstractGenericAttribute is the abstract superclass for all types of generic ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CodeAttribute](CodeAttribute.md) | CodeAttribute is a data type used to define generic attributes of type "Code" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DateAttribute](DateAttribute.md) | DateAttribute is a data type used to define generic attributes of type "Date" |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DoubleAttribute](DoubleAttribute.md) | DoubleAttribute is a data type used to define generic attributes of type "Dou... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenericAttributeSet](GenericAttributeSet.md) | A GenericAttributeSet is a named collection of generic attributes |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IntAttribute](IntAttribute.md) | IntAttribute is a data type used to define generic attributes of type "Intege... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeasureAttribute](MeasureAttribute.md) | MeasureAttribute is a data type used to define generic attributes of type "Me... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StringAttribute](StringAttribute.md) | StringAttribute is a data type used to define generic attributes of type "Str... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UriAttribute](UriAttribute.md) | UriAttribute is a data type used to define generic attributes of type "URI" |
| [AbstractTextureParameterization](AbstractTextureParameterization.md) | AbstractTextureParameterization is the abstract superclass for different kind... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TexCoordGen](TexCoordGen.md) | TexCoordGen defines texture parameterization using a transformation matrix |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TexCoordList](TexCoordList.md) | TexCoordList defines texture parameterization using texture coordinates |
| [ADEOfAbstractAppearance](ADEOfAbstractAppearance.md) | ADEOfAbstractAppearance acts as a hook to define properties within an ADE tha... |
| [ADEOfAbstractAtomicTimeseries](ADEOfAbstractAtomicTimeseries.md) | ADEOfAbstractAtomicTimeseries acts as a hook to define properties within an A... |
| [ADEOfAbstractBridge](ADEOfAbstractBridge.md) | ADEOfAbstractBridge acts as a hook to define properties within an ADE that ar... |
| [ADEOfAbstractBuilding](ADEOfAbstractBuilding.md) | ADEOfAbstractBuilding acts as a hook to define properties within an ADE that ... |
| [ADEOfAbstractBuildingSubdivision](ADEOfAbstractBuildingSubdivision.md) | ADEOfAbstractBuildingSubdivision acts as a hook to define properties within a... |
| [ADEOfAbstractCityObject](ADEOfAbstractCityObject.md) | ADEOfAbstractCityObject acts as a hook to define properties within an ADE tha... |
| [ADEOfAbstractConstruction](ADEOfAbstractConstruction.md) | ADEOfAbstractConstruction acts as a hook to define properties within an ADE t... |
| [ADEOfAbstractConstructionSurface](ADEOfAbstractConstructionSurface.md) | ADEOfAbstractConstructionSurface acts as a hook to define properties within a... |
| [ADEOfAbstractConstructiveElement](ADEOfAbstractConstructiveElement.md) | ADEOfAbstractConstructiveElement acts as a hook to define properties within a... |
| [ADEOfAbstractDynamizer](ADEOfAbstractDynamizer.md) | ADEOfAbstractDynamizer acts as a hook to define properties within an ADE that... |
| [ADEOfAbstractFeature](ADEOfAbstractFeature.md) | ADEOfAbstractFeature acts as a hook to define properties within an ADE that a... |
| [ADEOfAbstractFeatureWithLifespan](ADEOfAbstractFeatureWithLifespan.md) | ADEOfAbstractFeatureWithLifespan acts as a hook to define properties within a... |
| [ADEOfAbstractFillingElement](ADEOfAbstractFillingElement.md) | ADEOfAbstractFillingElement acts as a hook to define properties within an ADE... |
| [ADEOfAbstractFillingSurface](ADEOfAbstractFillingSurface.md) | ADEOfAbstractFillingSurface acts as a hook to define properties within an ADE... |
| [ADEOfAbstractFurniture](ADEOfAbstractFurniture.md) | ADEOfAbstractFurniture acts as a hook to define properties within an ADE that... |
| [ADEOfAbstractInstallation](ADEOfAbstractInstallation.md) | ADEOfAbstractInstallation acts as a hook to define properties within an ADE t... |
| [ADEOfAbstractLogicalSpace](ADEOfAbstractLogicalSpace.md) | ADEOfAbstractLogicalSpace acts as a hook to define properties within an ADE t... |
| [ADEOfAbstractOccupiedSpace](ADEOfAbstractOccupiedSpace.md) | ADEOfAbstractOccupiedSpace acts as a hook to define properties within an ADE ... |
| [ADEOfAbstractPhysicalSpace](ADEOfAbstractPhysicalSpace.md) | ADEOfAbstractPhysicalSpace acts as a hook to define properties within an ADE ... |
| [ADEOfAbstractPointCloud](ADEOfAbstractPointCloud.md) | ADEOfAbstractPointCloud acts as a hook to define properties within an ADE tha... |
| [ADEOfAbstractReliefComponent](ADEOfAbstractReliefComponent.md) | ADEOfAbstractReliefComponent acts as a hook to define properties within an AD... |
| [ADEOfAbstractSpace](ADEOfAbstractSpace.md) | ADEOfAbstractSpace acts as a hook to define properties within an ADE that are... |
| [ADEOfAbstractSpaceBoundary](ADEOfAbstractSpaceBoundary.md) | ADEOfAbstractSpaceBoundary acts as a hook to define properties within an ADE ... |
| [ADEOfAbstractSurfaceData](ADEOfAbstractSurfaceData.md) | ADEOfAbstractSurfaceData acts as a hook to define properties within an ADE th... |
| [ADEOfAbstractTexture](ADEOfAbstractTexture.md) | ADEOfAbstractTexture acts as a hook to define properties within an ADE that a... |
| [ADEOfAbstractThematicSurface](ADEOfAbstractThematicSurface.md) | ADEOfAbstractThematicSurface acts as a hook to define properties within an AD... |
| [ADEOfAbstractTimeseries](ADEOfAbstractTimeseries.md) | ADEOfAbstractTimeseries acts as a hook to define properties within an ADE tha... |
| [ADEOfAbstractTransportationSpace](ADEOfAbstractTransportationSpace.md) | ADEOfAbstractTransportationSpace acts as a hook to define properties within a... |
| [ADEOfAbstractTunnel](ADEOfAbstractTunnel.md) | ADEOfAbstractTunnel acts as a hook to define properties within an ADE that ar... |
| [ADEOfAbstractUnoccupiedSpace](ADEOfAbstractUnoccupiedSpace.md) | ADEOfAbstractUnoccupiedSpace acts as a hook to define properties within an AD... |
| [ADEOfAbstractVegetationObject](ADEOfAbstractVegetationObject.md) | ADEOfAbstractVegetationObject acts as a hook to define properties within an A... |
| [ADEOfAbstractVersion](ADEOfAbstractVersion.md) | ADEOfAbstractVersion acts as a hook to define properties within an ADE that a... |
| [ADEOfAbstractVersionTransition](ADEOfAbstractVersionTransition.md) | ADEOfAbstractVersionTransition acts as a hook to define properties within an ... |
| [ADEOfAbstractWaterBoundarySurface](ADEOfAbstractWaterBoundarySurface.md) | ADEOfAbstractWaterBoundarySurface acts as a hook to define properties within ... |
| [ADEOfAddress](ADEOfAddress.md) | ADEOfAddress acts as a hook to define properties within an ADE that are to be... |
| [ADEOfAppearance](ADEOfAppearance.md) | ADEOfAppearance acts as a hook to define properties within an ADE that are to... |
| [ADEOfAuxiliaryTrafficArea](ADEOfAuxiliaryTrafficArea.md) | ADEOfAuxiliaryTrafficArea acts as a hook to define properties within an ADE t... |
| [ADEOfAuxiliaryTrafficSpace](ADEOfAuxiliaryTrafficSpace.md) | ADEOfAuxiliaryTrafficSpace acts as a hook to define properties within an ADE ... |
| [ADEOfBreaklineRelief](ADEOfBreaklineRelief.md) | ADEOfBreaklineRelief acts as a hook to define properties within an ADE that a... |
| [ADEOfBridge](ADEOfBridge.md) | ADEOfBridge acts as a hook to define properties within an ADE that are to be ... |
| [ADEOfBridgeConstructiveElement](ADEOfBridgeConstructiveElement.md) | ADEOfBridgeConstructiveElement acts as a hook to define properties within an ... |
| [ADEOfBridgeFurniture](ADEOfBridgeFurniture.md) | ADEOfBridgeFurniture acts as a hook to define properties within an ADE that a... |
| [ADEOfBridgeInstallation](ADEOfBridgeInstallation.md) | ADEOfBridgeInstallation acts as a hook to define properties within an ADE tha... |
| [ADEOfBridgePart](ADEOfBridgePart.md) | ADEOfBridgePart acts as a hook to define properties within an ADE that are to... |
| [ADEOfBridgeRoom](ADEOfBridgeRoom.md) | ADEOfBridgeRoom acts as a hook to define properties within an ADE that are to... |
| [ADEOfBuilding](ADEOfBuilding.md) | ADEOfBuilding acts as a hook to define properties within an ADE that are to b... |
| [ADEOfBuildingConstructiveElement](ADEOfBuildingConstructiveElement.md) | ADEOfBuildingConstructiveElement acts as a hook to define properties within a... |
| [ADEOfBuildingFurniture](ADEOfBuildingFurniture.md) | ADEOfBuildingFurniture acts as a hook to define properties within an ADE that... |
| [ADEOfBuildingInstallation](ADEOfBuildingInstallation.md) | ADEOfBuildingInstallation acts as a hook to define properties within an ADE t... |
| [ADEOfBuildingPart](ADEOfBuildingPart.md) | ADEOfBuildingPart acts as a hook to define properties within an ADE that are ... |
| [ADEOfBuildingRoom](ADEOfBuildingRoom.md) | ADEOfBuildingRoom acts as a hook to define properties within an ADE that are ... |
| [ADEOfBuildingUnit](ADEOfBuildingUnit.md) | ADEOfBuildingUnit acts as a hook to define properties within an ADE that are ... |
| [ADEOfCeilingSurface](ADEOfCeilingSurface.md) | ADEOfCeilingSurface acts as a hook to define properties within an ADE that ar... |
| [ADEOfCityFurniture](ADEOfCityFurniture.md) | ADEOfCityFurniture acts as a hook to define properties within an ADE that are... |
| [ADEOfCityModel](ADEOfCityModel.md) | ADEOfCityModel acts as a hook to define properties within an ADE that are to ... |
| [ADEOfCityObjectGroup](ADEOfCityObjectGroup.md) | ADEOfCityObjectGroup acts as a hook to define properties within an ADE that a... |
| [ADEOfClearanceSpace](ADEOfClearanceSpace.md) | ADEOfClearanceSpace acts as a hook to define properties within an ADE that ar... |
| [ADEOfClosureSurface](ADEOfClosureSurface.md) | ADEOfClosureSurface acts as a hook to define properties within an ADE that ar... |
| [ADEOfCompositeTimeseries](ADEOfCompositeTimeseries.md) | ADEOfCompositeTimeseries acts as a hook to define properties within an ADE th... |
| [ADEOfDoor](ADEOfDoor.md) | ADEOfDoor acts as a hook to define properties within an ADE that are to be ad... |
| [ADEOfDoorSurface](ADEOfDoorSurface.md) | ADEOfDoorSurface acts as a hook to define properties within an ADE that are t... |
| [ADEOfDynamizer](ADEOfDynamizer.md) | ADEOfDynamizer acts as a hook to define properties within an ADE that are to ... |
| [ADEOfFloorSurface](ADEOfFloorSurface.md) | ADEOfFloorSurface acts as a hook to define properties within an ADE that are ... |
| [ADEOfGenericLogicalSpace](ADEOfGenericLogicalSpace.md) | ADEOfGenericLogicalSpace acts as a hook to define properties within an ADE th... |
| [ADEOfGenericOccupiedSpace](ADEOfGenericOccupiedSpace.md) | ADEOfGenericOccupiedSpace acts as a hook to define properties within an ADE t... |
| [ADEOfGenericThematicSurface](ADEOfGenericThematicSurface.md) | ADEOfGenericThematicSurface acts as a hook to define properties within an ADE... |
| [ADEOfGenericTimeseries](ADEOfGenericTimeseries.md) | ADEOfGenericTimeseries acts as a hook to define properties within an ADE that... |
| [ADEOfGenericUnoccupiedSpace](ADEOfGenericUnoccupiedSpace.md) | ADEOfGenericUnoccupiedSpace acts as a hook to define properties within an ADE... |
| [ADEOfGeoreferencedTexture](ADEOfGeoreferencedTexture.md) | ADEOfGeoreferencedTexture acts as a hook to define properties within an ADE t... |
| [ADEOfGroundSurface](ADEOfGroundSurface.md) | ADEOfGroundSurface acts as a hook to define properties within an ADE that are... |
| [ADEOfHole](ADEOfHole.md) | ADEOfHole acts as a hook to define properties within an ADE that are to be ad... |
| [ADEOfHoleSurface](ADEOfHoleSurface.md) | ADEOfHoleSurface acts as a hook to define properties within an ADE that are t... |
| [ADEOfHollowSpace](ADEOfHollowSpace.md) | ADEOfHollowSpace acts as a hook to define properties within an ADE that are t... |
| [ADEOfInteriorWallSurface](ADEOfInteriorWallSurface.md) | ADEOfInteriorWallSurface acts as a hook to define properties within an ADE th... |
| [ADEOfIntersection](ADEOfIntersection.md) | ADEOfIntersection acts as a hook to define properties within an ADE that are ... |
| [ADEOfLandUse](ADEOfLandUse.md) | ADEOfLandUse acts as a hook to define properties within an ADE that are to be... |
| [ADEOfMarking](ADEOfMarking.md) | ADEOfMarking acts as a hook to define properties within an ADE that are to be... |
| [ADEOfMassPointRelief](ADEOfMassPointRelief.md) | ADEOfMassPointRelief acts as a hook to define properties within an ADE that a... |
| [ADEOfOtherConstruction](ADEOfOtherConstruction.md) | ADEOfOtherConstruction acts as a hook to define properties within an ADE that... |
| [ADEOfOuterCeilingSurface](ADEOfOuterCeilingSurface.md) | ADEOfOuterCeilingSurface acts as a hook to define properties within an ADE th... |
| [ADEOfOuterFloorSurface](ADEOfOuterFloorSurface.md) | ADEOfOuterFloorSurface acts as a hook to define properties within an ADE that... |
| [ADEOfParameterizedTexture](ADEOfParameterizedTexture.md) | ADEOfParameterizedTexture acts as a hook to define properties within an ADE t... |
| [ADEOfPlantCover](ADEOfPlantCover.md) | ADEOfPlantCover acts as a hook to define properties within an ADE that are to... |
| [ADEOfPointCloud](ADEOfPointCloud.md) | ADEOfPointCloud acts as a hook to define properties within an ADE that are to... |
| [ADEOfRailway](ADEOfRailway.md) | ADEOfRailway acts as a hook to define properties within an ADE that are to be... |
| [ADEOfRasterRelief](ADEOfRasterRelief.md) | ADEOfRasterRelief acts as a hook to define properties within an ADE that are ... |
| [ADEOfReliefFeature](ADEOfReliefFeature.md) | ADEOfReliefFeature acts as a hook to define properties within an ADE that are... |
| [ADEOfRoad](ADEOfRoad.md) | ADEOfRoad acts as a hook to define properties within an ADE that are to be ad... |
| [ADEOfRoofSurface](ADEOfRoofSurface.md) | ADEOfRoofSurface acts as a hook to define properties within an ADE that are t... |
| [ADEOfSection](ADEOfSection.md) | ADEOfSection acts as a hook to define properties within an ADE that are to be... |
| [ADEOfSolitaryVegetationObject](ADEOfSolitaryVegetationObject.md) | ADEOfSolitaryVegetationObject acts as a hook to define properties within an A... |
| [ADEOfSquare](ADEOfSquare.md) | ADEOfSquare acts as a hook to define properties within an ADE that are to be ... |
| [ADEOfStandardFileTimeseries](ADEOfStandardFileTimeseries.md) | ADEOfStandardFileTimeseries acts as a hook to define properties within an ADE... |
| [ADEOfStorey](ADEOfStorey.md) | ADEOfStorey acts as a hook to define properties within an ADE that are to be ... |
| [ADEOfTabulatedFileTimeseries](ADEOfTabulatedFileTimeseries.md) | ADEOfTabulatedFileTimeseries acts as a hook to define properties within an AD... |
| [ADEOfTINRelief](ADEOfTINRelief.md) | ADEOfTINRelief acts as a hook to define properties within an ADE that are to ... |
| [ADEOfTrack](ADEOfTrack.md) | ADEOfTrack acts as a hook to define properties within an ADE that are to be a... |
| [ADEOfTrafficArea](ADEOfTrafficArea.md) | ADEOfTrafficArea acts as a hook to define properties within an ADE that are t... |
| [ADEOfTrafficSpace](ADEOfTrafficSpace.md) | ADEOfTrafficSpace acts as a hook to define properties within an ADE that are ... |
| [ADEOfTunnel](ADEOfTunnel.md) | ADEOfTunnel acts as a hook to define properties within an ADE that are to be ... |
| [ADEOfTunnelConstructiveElement](ADEOfTunnelConstructiveElement.md) | ADEOfTunnelConstructiveElement acts as a hook to define properties within an ... |
| [ADEOfTunnelFurniture](ADEOfTunnelFurniture.md) | ADEOfTunnelFurniture acts as a hook to define properties within an ADE that a... |
| [ADEOfTunnelInstallation](ADEOfTunnelInstallation.md) | ADEOfTunnelInstallation acts as a hook to define properties within an ADE tha... |
| [ADEOfTunnelPart](ADEOfTunnelPart.md) | ADEOfTunnelPart acts as a hook to define properties within an ADE that are to... |
| [ADEOfVersion](ADEOfVersion.md) | ADEOfVersion acts as a hook to define properties within an ADE that are to be... |
| [ADEOfVersionTransition](ADEOfVersionTransition.md) | ADEOfVersionTransition acts as a hook to define properties within an ADE that... |
| [ADEOfWallSurface](ADEOfWallSurface.md) | ADEOfWallSurface acts as a hook to define properties within an ADE that are t... |
| [ADEOfWaterBody](ADEOfWaterBody.md) | ADEOfWaterBody acts as a hook to define properties within an ADE that are to ... |
| [ADEOfWaterGroundSurface](ADEOfWaterGroundSurface.md) | ADEOfWaterGroundSurface acts as a hook to define properties within an ADE tha... |
| [ADEOfWaterSurface](ADEOfWaterSurface.md) | ADEOfWaterSurface acts as a hook to define properties within an ADE that are ... |
| [ADEOfWaterway](ADEOfWaterway.md) | ADEOfWaterway acts as a hook to define properties within an ADE that are to b... |
| [ADEOfWindow](ADEOfWindow.md) | ADEOfWindow acts as a hook to define properties within an ADE that are to be ... |
| [ADEOfWindowSurface](ADEOfWindowSurface.md) | ADEOfWindowSurface acts as a hook to define properties within an ADE that are... |
| [ADEOfX3DMaterial](ADEOfX3DMaterial.md) | ADEOfX3DMaterial acts as a hook to define properties within an ADE that are t... |
| [AuthenticationTypeValue](AuthenticationTypeValue.md) | CityGML class from package Dynamizer |
| [AuxiliaryTrafficAreaClassValue](AuxiliaryTrafficAreaClassValue.md) | CityGML class from package Transportation |
| [AuxiliaryTrafficAreaFunctionValue](AuxiliaryTrafficAreaFunctionValue.md) | CityGML class from package Transportation |
| [AuxiliaryTrafficAreaUsageValue](AuxiliaryTrafficAreaUsageValue.md) | CityGML class from package Transportation |
| [AuxiliaryTrafficSpaceClassValue](AuxiliaryTrafficSpaceClassValue.md) | CityGML class from package Transportation |
| [AuxiliaryTrafficSpaceFunctionValue](AuxiliaryTrafficSpaceFunctionValue.md) | CityGML class from package Transportation |
| [AuxiliaryTrafficSpaceUsageValue](AuxiliaryTrafficSpaceUsageValue.md) | CityGML class from package Transportation |
| [BridgeClassValue](BridgeClassValue.md) | CityGML class from package Bridge |
| [BridgeConstructiveElementClassValue](BridgeConstructiveElementClassValue.md) | CityGML class from package Bridge |
| [BridgeConstructiveElementFunctionValue](BridgeConstructiveElementFunctionValue.md) | CityGML class from package Bridge |
| [BridgeConstructiveElementUsageValue](BridgeConstructiveElementUsageValue.md) | CityGML class from package Bridge |
| [BridgeFunctionValue](BridgeFunctionValue.md) | CityGML class from package Bridge |
| [BridgeFurnitureClassValue](BridgeFurnitureClassValue.md) | CityGML class from package Bridge |
| [BridgeFurnitureFunctionValue](BridgeFurnitureFunctionValue.md) | CityGML class from package Bridge |
| [BridgeFurnitureUsageValue](BridgeFurnitureUsageValue.md) | CityGML class from package Bridge |
| [BridgeInstallationClassValue](BridgeInstallationClassValue.md) | CityGML class from package Bridge |
| [BridgeInstallationFunctionValue](BridgeInstallationFunctionValue.md) | CityGML class from package Bridge |
| [BridgeInstallationUsageValue](BridgeInstallationUsageValue.md) | CityGML class from package Bridge |
| [BridgeRoomClassValue](BridgeRoomClassValue.md) | CityGML class from package Bridge |
| [BridgeRoomFunctionValue](BridgeRoomFunctionValue.md) | CityGML class from package Bridge |
| [BridgeRoomUsageValue](BridgeRoomUsageValue.md) | CityGML class from package Bridge |
| [BridgeUsageValue](BridgeUsageValue.md) | CityGML class from package Bridge |
| [BuildingClassValue](BuildingClassValue.md) | CityGML class from package Building |
| [BuildingConstructiveElementClassValue](BuildingConstructiveElementClassValue.md) | CityGML class from package Building |
| [BuildingConstructiveElementFunctionValue](BuildingConstructiveElementFunctionValue.md) | CityGML class from package Building |
| [BuildingConstructiveElementUsageValue](BuildingConstructiveElementUsageValue.md) | CityGML class from package Building |
| [BuildingFunctionValue](BuildingFunctionValue.md) | CityGML class from package Building |
| [BuildingFurnitureClassValue](BuildingFurnitureClassValue.md) | CityGML class from package Building |
| [BuildingFurnitureFunctionValue](BuildingFurnitureFunctionValue.md) | CityGML class from package Building |
| [BuildingFurnitureUsageValue](BuildingFurnitureUsageValue.md) | CityGML class from package Building |
| [BuildingInstallationClassValue](BuildingInstallationClassValue.md) | CityGML class from package Building |
| [BuildingInstallationFunctionValue](BuildingInstallationFunctionValue.md) | CityGML class from package Building |
| [BuildingInstallationUsageValue](BuildingInstallationUsageValue.md) | CityGML class from package Building |
| [BuildingRoomClassValue](BuildingRoomClassValue.md) | CityGML class from package Building |
| [BuildingRoomFunctionValue](BuildingRoomFunctionValue.md) | CityGML class from package Building |
| [BuildingRoomUsageValue](BuildingRoomUsageValue.md) | CityGML class from package Building |
| [BuildingSubdivisionClassValue](BuildingSubdivisionClassValue.md) | CityGML class from package Building |
| [BuildingSubdivisionFunctionValue](BuildingSubdivisionFunctionValue.md) | CityGML class from package Building |
| [BuildingSubdivisionUsageValue](BuildingSubdivisionUsageValue.md) | CityGML class from package Building |
| [BuildingUsageValue](BuildingUsageValue.md) | CityGML class from package Building |
| [CityFurnitureClassValue](CityFurnitureClassValue.md) | CityGML class from package CityFurniture |
| [CityFurnitureFunctionValue](CityFurnitureFunctionValue.md) | CityGML class from package CityFurniture |
| [CityFurnitureUsageValue](CityFurnitureUsageValue.md) | CityGML class from package CityFurniture |
| [CityModelMember](CityModelMember.md) | CityGML class from package Core |
| [CityObjectGroupClassValue](CityObjectGroupClassValue.md) | CityGML class from package CityObjectGroup |
| [CityObjectGroupFunctionValue](CityObjectGroupFunctionValue.md) | CityGML class from package CityObjectGroup |
| [CityObjectGroupUsageValue](CityObjectGroupUsageValue.md) | CityGML class from package CityObjectGroup |
| [ClearanceSpaceClassValue](ClearanceSpaceClassValue.md) | CityGML class from package Transportation |
| [Code](Code.md) | CityGML class from package Core |
| [ConstructionEvent](ConstructionEvent.md) | A ConstructionEvent is a data type used to describe a specific event that is ... |
| [DoorClassValue](DoorClassValue.md) | CityGML class from package Construction |
| [DoorFunctionValue](DoorFunctionValue.md) | CityGML class from package Construction |
| [DoorUsageValue](DoorUsageValue.md) | CityGML class from package Construction |
| [DoubleBetween0and1](DoubleBetween0and1.md) | CityGML class from package Core |
| [DoubleBetween0and1List](DoubleBetween0and1List.md) | CityGML class from package Core |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Color](Color.md) | CityGML class from package Appearance |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ColorPlusOpacity](ColorPlusOpacity.md) | CityGML class from package Appearance |
| [DoubleList](DoubleList.md) | CityGML class from package Core |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TransformationMatrix2x2](TransformationMatrix2x2.md) | CityGML class from package Core |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TransformationMatrix3x4](TransformationMatrix3x4.md) | CityGML class from package Core |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TransformationMatrix4x4](TransformationMatrix4x4.md) | CityGML class from package Core |
| [DoubleOrNilReason](DoubleOrNilReason.md) | CityGML class from package Core |
| [DoubleOrNilReasonList](DoubleOrNilReasonList.md) | CityGML class from package Core |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeasureOrNilReasonList](MeasureOrNilReasonList.md) | CityGML class from package Core |
| [Elevation](Elevation.md) | Elevation is a data type that includes the elevation value itself and informa... |
| [ElevationReferenceValue](ElevationReferenceValue.md) | CityGML class from package Construction |
| [EventValue](EventValue.md) | CityGML class from package Construction |
| [ExternalReference](ExternalReference.md) | ExternalReference is a reference to a corresponding object in another informa... |
| [GenericLogicalSpaceClassValue](GenericLogicalSpaceClassValue.md) | CityGML class from package Generics |
| [GenericLogicalSpaceFunctionValue](GenericLogicalSpaceFunctionValue.md) | CityGML class from package Generics |
| [GenericLogicalSpaceUsageValue](GenericLogicalSpaceUsageValue.md) | CityGML class from package Generics |
| [GenericOccupiedSpaceClassValue](GenericOccupiedSpaceClassValue.md) | CityGML class from package Generics |
| [GenericOccupiedSpaceFunctionValue](GenericOccupiedSpaceFunctionValue.md) | CityGML class from package Generics |
| [GenericOccupiedSpaceUsageValue](GenericOccupiedSpaceUsageValue.md) | CityGML class from package Generics |
| [GenericThematicSurfaceClassValue](GenericThematicSurfaceClassValue.md) | CityGML class from package Generics |
| [GenericThematicSurfaceFunctionValue](GenericThematicSurfaceFunctionValue.md) | CityGML class from package Generics |
| [GenericThematicSurfaceUsageValue](GenericThematicSurfaceUsageValue.md) | CityGML class from package Generics |
| [GenericUnoccupiedSpaceClassValue](GenericUnoccupiedSpaceClassValue.md) | CityGML class from package Generics |
| [GenericUnoccupiedSpaceFunctionValue](GenericUnoccupiedSpaceFunctionValue.md) | CityGML class from package Generics |
| [GenericUnoccupiedSpaceUsageValue](GenericUnoccupiedSpaceUsageValue.md) | CityGML class from package Generics |
| [Height](Height.md) | Height represents a vertical distance (measured or estimated) between a low r... |
| [HoleClassValue](HoleClassValue.md) | CityGML class from package Transportation |
| [HollowSpaceClassValue](HollowSpaceClassValue.md) | CityGML class from package Tunnel |
| [HollowSpaceFunctionValue](HollowSpaceFunctionValue.md) | CityGML class from package Tunnel |
| [HollowSpaceUsageValue](HollowSpaceUsageValue.md) | CityGML class from package Tunnel |
| [ID](ID.md) | CityGML class from package Core |
| [ImplicitGeometry](ImplicitGeometry.md) | ImplicitGeometry is a geometry representation where the shape is stored only ... |
| [IntegerBetween0and3](IntegerBetween0and3.md) | CityGML class from package Core |
| [IntersectionClassValue](IntersectionClassValue.md) | CityGML class from package Transportation |
| [IntervalValue](IntervalValue.md) | CityGML class from package Core |
| [LandUseClassValue](LandUseClassValue.md) | CityGML class from package LandUse |
| [LandUseFunctionValue](LandUseFunctionValue.md) | CityGML class from package LandUse |
| [LandUseUsageValue](LandUseUsageValue.md) | CityGML class from package LandUse |
| [MarkingClassValue](MarkingClassValue.md) | CityGML class from package Transportation |
| [MimeTypeValue](MimeTypeValue.md) | CityGML class from package Core |
| [NilReason](NilReason.md) | CityGML class from package Core |
| [NilReasonEnumeration](NilReasonEnumeration.md) | CityGML class from package Core |
| [Occupancy](Occupancy.md) | Occupancy is an application-dependent indication of what is contained by a fe... |
| [OccupantTypeValue](OccupantTypeValue.md) | CityGML class from package Core |
| [OtherConstructionClassValue](OtherConstructionClassValue.md) | CityGML class from package Construction |
| [OtherConstructionFunctionValue](OtherConstructionFunctionValue.md) | CityGML class from package Construction |
| [OtherConstructionUsageValue](OtherConstructionUsageValue.md) | CityGML class from package Construction |
| [PlantCoverClassValue](PlantCoverClassValue.md) | CityGML class from package Vegetation |
| [PlantCoverFunctionValue](PlantCoverFunctionValue.md) | CityGML class from package Vegetation |
| [PlantCoverUsageValue](PlantCoverUsageValue.md) | CityGML class from package Vegetation |
| [QualifiedArea](QualifiedArea.md) | QualifiedArea is an application-dependent measure of the area of a space or o... |
| [QualifiedAreaTypeValue](QualifiedAreaTypeValue.md) | CityGML class from package Core |
| [QualifiedVolume](QualifiedVolume.md) | QualifiedVolume is an application-dependent measure of the volume of a space |
| [QualifiedVolumeTypeValue](QualifiedVolumeTypeValue.md) | CityGML class from package Core |
| [RailwayClassValue](RailwayClassValue.md) | CityGML class from package Transportation |
| [RailwayFunctionValue](RailwayFunctionValue.md) | CityGML class from package Transportation |
| [RailwayUsageValue](RailwayUsageValue.md) | CityGML class from package Transportation |
| [RelationTypeValue](RelationTypeValue.md) | CityGML class from package Core |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OtherRelationTypeValue](OtherRelationTypeValue.md) | CityGML class from package Core |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TemporalRelationTypeValue](TemporalRelationTypeValue.md) | CityGML class from package Core |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TopologicalRelationTypeValue](TopologicalRelationTypeValue.md) | CityGML class from package Core |
| [RoadClassValue](RoadClassValue.md) | CityGML class from package Transportation |
| [RoadFunctionValue](RoadFunctionValue.md) | CityGML class from package Transportation |
| [RoadUsageValue](RoadUsageValue.md) | CityGML class from package Transportation |
| [RoofTypeValue](RoofTypeValue.md) | CityGML class from package Building |
| [RoomElevationReferenceValue](RoomElevationReferenceValue.md) | CityGML class from package Building |
| [RoomHeight](RoomHeight.md) | The RoomHeight represents a vertical distance (measured or estimated) between... |
| [SectionClassValue](SectionClassValue.md) | CityGML class from package Transportation |
| [SensorConnection](SensorConnection.md) | A SensorConnection provides all details that are required to retrieve a speci... |
| [SensorConnectionTypeValue](SensorConnectionTypeValue.md) | CityGML class from package Dynamizer |
| [SolitaryVegetationObjectClassValue](SolitaryVegetationObjectClassValue.md) | CityGML class from package Vegetation |
| [SolitaryVegetationObjectFunctionValue](SolitaryVegetationObjectFunctionValue.md) | CityGML class from package Vegetation |
| [SolitaryVegetationObjectUsageValue](SolitaryVegetationObjectUsageValue.md) | CityGML class from package Vegetation |
| [SpeciesValue](SpeciesValue.md) | CityGML class from package Vegetation |
| [SquareClassValue](SquareClassValue.md) | CityGML class from package Transportation |
| [SquareFunctionValue](SquareFunctionValue.md) | CityGML class from package Transportation |
| [SquareUsageValue](SquareUsageValue.md) | CityGML class from package Transportation |
| [StandardFileTypeValue](StandardFileTypeValue.md) | CityGML class from package Dynamizer |
| [SurfaceMaterialValue](SurfaceMaterialValue.md) | CityGML class from package Transportation |
| [TabulatedFileTypeValue](TabulatedFileTypeValue.md) | CityGML class from package Dynamizer |
| [TimeseriesComponent](TimeseriesComponent.md) | TimeseriesComponent represents an element of a CompositeTimeseries |
| [TimeValuePair](TimeValuePair.md) | A TimeValuePair represents a value that is valid for a given timepoint |
| [TrackClassValue](TrackClassValue.md) | CityGML class from package Transportation |
| [TrackFunctionValue](TrackFunctionValue.md) | CityGML class from package Transportation |
| [TrackUsageValue](TrackUsageValue.md) | CityGML class from package Transportation |
| [TrafficAreaClassValue](TrafficAreaClassValue.md) | CityGML class from package Transportation |
| [TrafficAreaFunctionValue](TrafficAreaFunctionValue.md) | CityGML class from package Transportation |
| [TrafficAreaUsageValue](TrafficAreaUsageValue.md) | CityGML class from package Transportation |
| [TrafficSpaceClassValue](TrafficSpaceClassValue.md) | CityGML class from package Transportation |
| [TrafficSpaceFunctionValue](TrafficSpaceFunctionValue.md) | CityGML class from package Transportation |
| [TrafficSpaceUsageValue](TrafficSpaceUsageValue.md) | CityGML class from package Transportation |
| [Transaction](Transaction.md) | Transaction represents a modification of the city model by the creation, term... |
| [TunnelClassValue](TunnelClassValue.md) | CityGML class from package Tunnel |
| [TunnelConstructiveElementClassValue](TunnelConstructiveElementClassValue.md) | CityGML class from package Tunnel |
| [TunnelConstructiveElementFunctionValue](TunnelConstructiveElementFunctionValue.md) | CityGML class from package Tunnel |
| [TunnelConstructiveElementUsageValue](TunnelConstructiveElementUsageValue.md) | CityGML class from package Tunnel |
| [TunnelFunctionValue](TunnelFunctionValue.md) | CityGML class from package Tunnel |
| [TunnelFurnitureClassValue](TunnelFurnitureClassValue.md) | CityGML class from package Tunnel |
| [TunnelFurnitureFunctionValue](TunnelFurnitureFunctionValue.md) | CityGML class from package Tunnel |
| [TunnelFurnitureUsageValue](TunnelFurnitureUsageValue.md) | CityGML class from package Tunnel |
| [TunnelInstallationClassValue](TunnelInstallationClassValue.md) | CityGML class from package Tunnel |
| [TunnelInstallationFunctionValue](TunnelInstallationFunctionValue.md) | CityGML class from package Tunnel |
| [TunnelInstallationUsageValue](TunnelInstallationUsageValue.md) | CityGML class from package Tunnel |
| [TunnelUsageValue](TunnelUsageValue.md) | CityGML class from package Tunnel |
| [WaterBodyClassValue](WaterBodyClassValue.md) | CityGML class from package WaterBody |
| [WaterBodyFunctionValue](WaterBodyFunctionValue.md) | CityGML class from package WaterBody |
| [WaterBodyUsageValue](WaterBodyUsageValue.md) | CityGML class from package WaterBody |
| [WaterLevelValue](WaterLevelValue.md) | CityGML class from package WaterBody |
| [WaterwayClassValue](WaterwayClassValue.md) | CityGML class from package Transportation |
| [WaterwayFunctionValue](WaterwayFunctionValue.md) | CityGML class from package Transportation |
| [WaterwayUsageValue](WaterwayUsageValue.md) | CityGML class from package Transportation |
| [WindowClassValue](WindowClassValue.md) | CityGML class from package Construction |
| [WindowFunctionValue](WindowFunctionValue.md) | CityGML class from package Construction |
| [WindowUsageValue](WindowUsageValue.md) | CityGML class from package Construction |
| [XALAddress](XALAddress.md) | CityGML class from package Core |



## Slots

| Slot | Description |
| --- | --- |
| [additionalGap](additionalGap.md) | Specifies how much extra time is added after all repetitions as an additional... |
| [address](address.md) | Relates to the addresses that are assigned to the Door |
| [adeOfAbstractAppearance](adeOfAbstractAppearance.md) | Augments AbstractAppearance with properties defined in an ADE |
| [adeOfAbstractAtomicTimeseries](adeOfAbstractAtomicTimeseries.md) | Augments AbstractAtomicTimeseries with properties defined in an ADE |
| [adeOfAbstractBridge](adeOfAbstractBridge.md) | Augments AbstractBridge with properties defined in an ADE |
| [adeOfAbstractBuilding](adeOfAbstractBuilding.md) | Augments AbstractBuilding with properties defined in an ADE |
| [adeOfAbstractBuildingSubdivision](adeOfAbstractBuildingSubdivision.md) | Augments AbstractBuildingSubdivision with properties defined in an ADE |
| [adeOfAbstractCityObject](adeOfAbstractCityObject.md) | Augments AbstractCityObject with properties defined in an ADE |
| [adeOfAbstractConstruction](adeOfAbstractConstruction.md) | Augments AbstractConstruction with properties defined in an ADE |
| [adeOfAbstractConstructionSurface](adeOfAbstractConstructionSurface.md) | Augments AbstractConstructionSurface with properties defined in an ADE |
| [adeOfAbstractConstructiveElement](adeOfAbstractConstructiveElement.md) | Augments AbstractConstructiveElement with properties defined in an ADE |
| [adeOfAbstractDynamizer](adeOfAbstractDynamizer.md) | Augments AbstractDynamizer with properties defined in an ADE |
| [adeOfAbstractFeature](adeOfAbstractFeature.md) | Augments AbstractFeature with properties defined in an ADE |
| [adeOfAbstractFeatureWithLifespan](adeOfAbstractFeatureWithLifespan.md) | Augments AbstractFeatureWithLifespan with properties defined in an ADE |
| [adeOfAbstractFillingElement](adeOfAbstractFillingElement.md) | Augments AbstractFillingElement with properties defined in an ADE |
| [adeOfAbstractFillingSurface](adeOfAbstractFillingSurface.md) | Augments AbstractFillingSurface with properties defined in an ADE |
| [adeOfAbstractFurniture](adeOfAbstractFurniture.md) | Augments AbstractFurniture with properties defined in an ADE |
| [adeOfAbstractInstallation](adeOfAbstractInstallation.md) | Augments AbstractInstallation with properties defined in an ADE |
| [adeOfAbstractLogicalSpace](adeOfAbstractLogicalSpace.md) | Augments AbstractLogicalSpace with properties defined in an ADE |
| [adeOfAbstractOccupiedSpace](adeOfAbstractOccupiedSpace.md) | Augments AbstractOccupiedSpace with properties defined in an ADE |
| [adeOfAbstractPhysicalSpace](adeOfAbstractPhysicalSpace.md) | Augments AbstractPhysicalSpace with properties defined in an ADE |
| [adeOfAbstractPointCloud](adeOfAbstractPointCloud.md) | Augments AbstractPointCloud with properties defined in an ADE |
| [adeOfAbstractReliefComponent](adeOfAbstractReliefComponent.md) | Augments AbstractReliefComponent with properties defined in an ADE |
| [adeOfAbstractSpace](adeOfAbstractSpace.md) | Augments AbstractSpace with properties defined in an ADE |
| [adeOfAbstractSpaceBoundary](adeOfAbstractSpaceBoundary.md) | Augments AbstractSpaceBoundary with properties defined in an ADE |
| [adeOfAbstractSurfaceData](adeOfAbstractSurfaceData.md) | Augments AbstractSurfaceData with properties defined in an ADE |
| [adeOfAbstractTexture](adeOfAbstractTexture.md) | Augments AbstractTexture with properties defined in an ADE |
| [adeOfAbstractThematicSurface](adeOfAbstractThematicSurface.md) | Augments AbstractThematicSurface with properties defined in an ADE |
| [adeOfAbstractTimeseries](adeOfAbstractTimeseries.md) | Augments AbstractTimeseries with properties defined in an ADE |
| [adeOfAbstractTransportationSpace](adeOfAbstractTransportationSpace.md) | Augments AbstractTransportationSpace with properties defined in an ADE |
| [adeOfAbstractTunnel](adeOfAbstractTunnel.md) | Augments AbstractTunnel with properties defined in an ADE |
| [adeOfAbstractUnoccupiedSpace](adeOfAbstractUnoccupiedSpace.md) | Augments AbstractUnoccupiedSpace with properties defined in an ADE |
| [adeOfAbstractVegetationObject](adeOfAbstractVegetationObject.md) | Augments AbstractVegetationObject with properties defined in an ADE |
| [adeOfAbstractVersion](adeOfAbstractVersion.md) | Augments AbstractVersion with properties defined in an ADE |
| [adeOfAbstractVersionTransition](adeOfAbstractVersionTransition.md) | Augments AbstractVersionTransition with properties defined in an ADE |
| [adeOfAbstractWaterBoundarySurface](adeOfAbstractWaterBoundarySurface.md) | Augments AbstractWaterBoundarySurface with properties defined in an ADE |
| [adeOfAddress](adeOfAddress.md) | Augments the Address with properties defined in an ADE |
| [adeOfAppearance](adeOfAppearance.md) | Augments the Appearance with properties defined in an ADE |
| [adeOfAuxiliaryTrafficArea](adeOfAuxiliaryTrafficArea.md) | Augments the AuxiliaryTrafficArea with properties defined in an ADE |
| [adeOfAuxiliaryTrafficSpace](adeOfAuxiliaryTrafficSpace.md) | Augments the AuxiliaryTrafficSpace with properties defined in an ADE |
| [adeOfBreaklineRelief](adeOfBreaklineRelief.md) | Augments the BreaklineRelief with properties defined in an ADE |
| [adeOfBridge](adeOfBridge.md) | Augments the Bridge with properties defined in an ADE |
| [adeOfBridgeConstructiveElement](adeOfBridgeConstructiveElement.md) | Augments the BridgeConstructiveElement with properties defined in an ADE |
| [adeOfBridgeFurniture](adeOfBridgeFurniture.md) | Augments the BridgeFurniture with properties defined in an ADE |
| [adeOfBridgeInstallation](adeOfBridgeInstallation.md) | Augments the BridgeInstallation with properties defined in an ADE |
| [adeOfBridgePart](adeOfBridgePart.md) | Augments the BridgePart with properties defined in an ADE |
| [adeOfBridgeRoom](adeOfBridgeRoom.md) | Augments the BridgeRoom with properties defined in an ADE |
| [adeOfBuilding](adeOfBuilding.md) | Augments the Building with properties defined in an ADE |
| [adeOfBuildingConstructiveElement](adeOfBuildingConstructiveElement.md) | Augments the BuildingConstructiveElement with properties defined in an ADE |
| [adeOfBuildingFurniture](adeOfBuildingFurniture.md) | Augments the BuildingFurniture with properties defined in an ADE |
| [adeOfBuildingInstallation](adeOfBuildingInstallation.md) | Augments the BuildingInstallation with properties defined in an ADE |
| [adeOfBuildingPart](adeOfBuildingPart.md) | Augments the BuildingPart with properties defined in an ADE |
| [adeOfBuildingRoom](adeOfBuildingRoom.md) | Augments the BuildingRoom with properties defined in an ADE |
| [adeOfBuildingUnit](adeOfBuildingUnit.md) | Augments the BuildingUnit with properties defined in an ADE |
| [adeOfCeilingSurface](adeOfCeilingSurface.md) | Augments the CeilingSurface with properties defined in an ADE |
| [adeOfCityFurniture](adeOfCityFurniture.md) | Augments the CityFurniture with properties defined in an ADE |
| [adeOfCityModel](adeOfCityModel.md) | Augments the CityModel with properties defined in an ADE |
| [adeOfCityObjectGroup](adeOfCityObjectGroup.md) | Augments the CityObjectGroup with properties defined in an ADE |
| [adeOfClearanceSpace](adeOfClearanceSpace.md) | Augments the ClearanceSpace with properties defined in an ADE |
| [adeOfClosureSurface](adeOfClosureSurface.md) | Augments the ClosureSurface with properties defined in an ADE |
| [adeOfCompositeTimeseries](adeOfCompositeTimeseries.md) | Augments the CompositeTimeseries with properties defined in an ADE |
| [adeOfDoor](adeOfDoor.md) | Augments the Door with properties defined in an ADE |
| [adeOfDoorSurface](adeOfDoorSurface.md) | Augments the DoorSurface with properties defined in an ADE |
| [adeOfDynamizer](adeOfDynamizer.md) | Augments the Dynamizer with properties defined in an ADE |
| [adeOfFloorSurface](adeOfFloorSurface.md) | Augments the FloorSurface with properties defined in an ADE |
| [adeOfGenericLogicalSpace](adeOfGenericLogicalSpace.md) | Augments the GenericLogicalSpace with properties defined in an ADE |
| [adeOfGenericOccupiedSpace](adeOfGenericOccupiedSpace.md) | Augments the GenericOccupiedSpace with properties defined in an ADE |
| [adeOfGenericThematicSurface](adeOfGenericThematicSurface.md) | Augments the GenericThematicSurface with properties defined in an ADE |
| [adeOfGenericTimeseries](adeOfGenericTimeseries.md) | Augments the GenericTimeseries with properties defined in an ADE |
| [adeOfGenericUnoccupiedSpace](adeOfGenericUnoccupiedSpace.md) | Augments the GenericUnoccupiedSpace with properties defined in an ADE |
| [adeOfGeoreferencedTexture](adeOfGeoreferencedTexture.md) | Augments the GeoreferencedTexture with properties defined in an ADE |
| [adeOfGroundSurface](adeOfGroundSurface.md) | Augments the GroundSurface with properties defined in an ADE |
| [adeOfHole](adeOfHole.md) | Augments the Hole with properties defined in an ADE |
| [adeOfHoleSurface](adeOfHoleSurface.md) | Augments the HoleSurface with properties defined in an ADE |
| [adeOfHollowSpace](adeOfHollowSpace.md) | Augments the HollowSpace with properties defined in an ADE |
| [adeOfInteriorWallSurface](adeOfInteriorWallSurface.md) | Augments the InteriorWallSurface with properties defined in an ADE |
| [adeOfIntersection](adeOfIntersection.md) | Augments the Intersection with properties defined in an ADE |
| [adeOfLandUse](adeOfLandUse.md) | Augments the LandUse with properties defined in an ADE |
| [adeOfMarking](adeOfMarking.md) | Augments the Marking with properties defined in an ADE |
| [adeOfMassPointRelief](adeOfMassPointRelief.md) | Augments the MassPointRelief with properties defined in an ADE |
| [adeOfOtherConstruction](adeOfOtherConstruction.md) | Augments the OtherConstruction with properties defined in an ADE |
| [adeOfOuterCeilingSurface](adeOfOuterCeilingSurface.md) | Augments the OuterCeilingSurface with properties defined in an ADE |
| [adeOfOuterFloorSurface](adeOfOuterFloorSurface.md) | Augments the OuterFloorSurface with properties defined in an ADE |
| [adeOfParameterizedTexture](adeOfParameterizedTexture.md) | Augments the ParameterizedTexture with properties defined in an ADE |
| [adeOfPlantCover](adeOfPlantCover.md) | Augments the PlantCover with properties defined in an ADE |
| [adeOfPointCloud](adeOfPointCloud.md) | Augments the PointCloud with properties defined in an ADE |
| [adeOfRailway](adeOfRailway.md) | Augments the Railway with properties defined in an ADE |
| [adeOfRasterRelief](adeOfRasterRelief.md) | Augments the RasterRelief with properties defined in an ADE |
| [adeOfReliefFeature](adeOfReliefFeature.md) | Augments the ReliefFeature with properties defined in an ADE |
| [adeOfRoad](adeOfRoad.md) | Augments the Road with properties defined in an ADE |
| [adeOfRoofSurface](adeOfRoofSurface.md) | Augments the RoofSurface with properties defined in an ADE |
| [adeOfSection](adeOfSection.md) | Augments the Section with properties defined in an ADE |
| [adeOfSolitaryVegetationObject](adeOfSolitaryVegetationObject.md) | Augments the SolitaryVegetationObject with properties defined in an ADE |
| [adeOfSquare](adeOfSquare.md) | Augments the Square with properties defined in an ADE |
| [adeOfStandardFileTimeseries](adeOfStandardFileTimeseries.md) | Augments the StandardFileTimeseries with properties defined in an ADE |
| [adeOfStorey](adeOfStorey.md) | Augments the Storey with properties defined in an ADE |
| [adeOfTabulatedFileTimeseries](adeOfTabulatedFileTimeseries.md) | Augments the TabulatedFileTimeseries with properties defined in an ADE |
| [adeOfTINRelief](adeOfTINRelief.md) | Augments the TINRelief with properties defined in an ADE |
| [adeOfTrack](adeOfTrack.md) | Augments the Track with properties defined in an ADE |
| [adeOfTrafficArea](adeOfTrafficArea.md) | Augments the TrafficArea with properties defined in an ADE |
| [adeOfTrafficSpace](adeOfTrafficSpace.md) | Augments the TrafficSpace with properties defined in an ADE |
| [adeOfTunnel](adeOfTunnel.md) | Augments the Tunnel with properties defined in an ADE |
| [adeOfTunnelConstructiveElement](adeOfTunnelConstructiveElement.md) | Augments the TunnelConstructiveElement with properties defined in an ADE |
| [adeOfTunnelFurniture](adeOfTunnelFurniture.md) | Augments the TunnelFurniture with properties defined in an ADE |
| [adeOfTunnelInstallation](adeOfTunnelInstallation.md) | Augments the TunnelInstallation with properties defined in an ADE |
| [adeOfTunnelPart](adeOfTunnelPart.md) | Augments the TunnelPart with properties defined in an ADE |
| [adeOfVersion](adeOfVersion.md) | Augments the Version with properties defined in an ADE |
| [adeOfVersionTransition](adeOfVersionTransition.md) | Augments the VersionTransition with properties defined in an ADE |
| [adeOfWallSurface](adeOfWallSurface.md) | Augments the WallSurface with properties defined in an ADE |
| [adeOfWaterBody](adeOfWaterBody.md) | Augments the WaterBody with properties defined in an ADE |
| [adeOfWaterGroundSurface](adeOfWaterGroundSurface.md) | Augments the WaterGroundSurface with properties defined in an ADE |
| [adeOfWaterSurface](adeOfWaterSurface.md) | Augments the WaterSurface with properties defined in an ADE |
| [adeOfWaterway](adeOfWaterway.md) | Augments the Waterway with properties defined in an ADE |
| [adeOfWindow](adeOfWindow.md) | Augments the Window with properties defined in an ADE |
| [adeOfWindowSurface](adeOfWindowSurface.md) | Augments the WindowSurface with properties defined in an ADE |
| [adeOfX3DMaterial](adeOfX3DMaterial.md) | Augments the X3DMaterial with properties defined in an ADE |
| [ambientIntensity](ambientIntensity.md) | Specifies the minimum percentage of diffuseColor that is visible regardless o... |
| [appearance](appearance.md) | Relates appearances to the city object |
| [appearanceMember](appearanceMember.md) |  |
| [appearanceValue](appearanceValue.md) | Specifies the "Appearance" value of the TimeValuePair |
| [area](area.md) | Specifies the value of the QualifiedArea |
| [attributeRef](attributeRef.md) | Specifies the attribute of a CityGML feature whose value is overridden or rep... |
| [authType](authType.md) | Specifies the type of authentication required to be able to access the Sensor... |
| [auxiliaryTrafficSpace](auxiliaryTrafficSpace.md) | Relates to the auxiliary traffic spaces that are part of the transportation s... |
| [averageHeight](averageHeight.md) | Specifies the average height of the PlantCover |
| [baseURL](baseURL.md) | Specifies the base URL of the Sensor API request |
| [boolValue](boolValue.md) | Specifies the "Boolean" value of the TimeValuePair |
| [borderColor](borderColor.md) | Specifies the color of that part of the surface that is not covered by the te... |
| [boundary](boundary.md) |  |
| [breaklines](breaklines.md) | Relates to the 3D MultiCurve geometry of the MassPointRelief |
| [bridgeConstructiveElement](bridgeConstructiveElement.md) | Relates the constructive elements to the Bridge or BridgePart |
| [bridgeFurniture](bridgeFurniture.md) | Relates the furniture objects to the Bridge or BridgePart |
| [bridgeInstallation](bridgeInstallation.md) | Relates the installation objects to the Bridge or BridgePart |
| [bridgePart](bridgePart.md) | Relates the bridge parts to the Bridge |
| [bridgeRoom](bridgeRoom.md) | Relates the rooms to the Bridge or BridgePart |
| [buildingConstructiveElement](buildingConstructiveElement.md) | Relates the constructive elements to the Building or BuildingPart |
| [buildingFurniture](buildingFurniture.md) | Relates the furniture objects to the Building or BuildingPart |
| [buildingInstallation](buildingInstallation.md) | Relates the installation objects to the Building or BuildingPart |
| [buildingPart](buildingPart.md) | Relates the building parts to the Building |
| [buildingRoom](buildingRoom.md) | Relates the rooms to the Building or BuildingPart |
| [buildingSubdivision](buildingSubdivision.md) | Relates the logical subdivisions to the Building or BuildingPart |
| [buildingUnit](buildingUnit.md) | Relates to the building units that belong to the Storey |
| [cityModelMember](cityModelMember.md) |  |
| [cityObjectMember](cityObjectMember.md) |  |
| [class](class.md) | Indicates the specific type of the Door |
| [clearanceSpace](clearanceSpace.md) | Relates to the clearance spaces that are part of the TrafficSpace |
| [clonePredecessor](clonePredecessor.md) | Indicates whether the set of city object instances belonging to the successor... |
| [codeSpace](codeSpace.md) | Associates the GenericAttributeSet with an authority that maintains the colle... |
| [component](component.md) | Relates to the atomic and composite timeseries that are part of the Composite... |
| [conditionOfConstruction](conditionOfConstruction.md) | Indicates the life-cycle status of the construction |
| [connectionType](connectionType.md) | Indicates the type of Sensor API to which the SensorConnection refers |
| [constructionEvent](constructionEvent.md) | Describes specific events in the life-time of the construction |
| [creationDate](creationDate.md) | Indicates the date at which a CityGML feature was added to the CityModel |
| [crownDiameter](crownDiameter.md) | Specifies the diameter of the SolitaryCityObject's crown |
| [crs](crs.md) |  |
| [datastreamID](datastreamID.md) | Specifies the datastream that is retrieved by the SensorConnection |
| [dateOfConstruction](dateOfConstruction.md) | Indicates the date at which the construction was completed |
| [dateOfDemolition](dateOfDemolition.md) | Indicates the date at which the construction was demolished |
| [dateOfEvent](dateOfEvent.md) | Specifies the date at which the event took or will take place |
| [decimalSymbol](decimalSymbol.md) | Indicates which symbol is used to separate the integer part from the fraction... |
| [description](description.md) | Provides additional information on the event |
| [diffuseColor](diffuseColor.md) | Specifies the color of the light diffusely reflected by the surface geometry ... |
| [doubleValue](doubleValue.md) | Specifies the "Double" value of the TimeValuePair |
| [dynamicData](dynamicData.md) | Relates to the timeseries data that is given either inline within a CityGML d... |
| [dynamizer](dynamizer.md) | Relates Dynamizer objects to the city object |
| [elevation](elevation.md) | Specifies qualified elevations of the construction in relation to a well-defi... |
| [elevationReference](elevationReference.md) | Specifies the level from which the elevation was measured |
| [elevationValue](elevationValue.md) | Specifies the value of the elevation |
| [emissiveColor](emissiveColor.md) | Specifies the color of the light emitted by the surface geometry object |
| [endTime](endTime.md) | Specifies the end of the time span for which the Dynamizer provides dynamic v... |
| [engineeringCRS](engineeringCRS.md) | Specifies the local engineering coordinate reference system of the CityModel ... |
| [event](event.md) | Indicates the specific event type |
| [extent](extent.md) | Indicates the geometrical extent of the terrain component |
| [externalReference](externalReference.md) | References external objects in other information systems that have a relation... |
| [featureID](featureID.md) |  |
| [featureMember](featureMember.md) |  |
| [fieldSeparator](fieldSeparator.md) | Indicates which symbol is used to separate the individual values in the tabul... |
| [fileLocation](fileLocation.md) | Specifies the URI that points to the external timeseries file |
| [fileType](fileType.md) | Specifies the format used to represent the timeseries data |
| [filling](filling.md) | Relates to the elements that fill the opening of the constructive element |
| [fillingSurface](fillingSurface.md) | Relates to the surfaces that seal the openings of the construction surface |
| [firstTimestamp](firstTimestamp.md) | Specifies the beginning of the timeseries |
| [from](from.md) | Relates to the predecessor version of the VersionTransition |
| [function](function.md) | Specifies the intended purposes of the Door |
| [generalizesTo](generalizesTo.md) | Relates generalized representations of the same real-world object in differen... |
| [genericAttribute](genericAttribute.md) | Relates to the generic attributes that are part of the GenericAttributeSet |
| [geometryValue](geometryValue.md) | Specifies the geometry value of the TimeValuePair |
| [granularity](granularity.md) | Defines whether auxiliary traffic spaces are represented by individual ways o... |
| [grid](grid.md) | Relates to the DiscreteGridPointCoverage of the RasterRelief |
| [groupMember](groupMember.md) |  |
| [height](height.md) | Specifies qualified heights of the construction above ground or below ground |
| [highReference](highReference.md) | Indicates the high point used to calculate the value of the height |
| [hole](hole.md) | Relates to the holes that are part of the transportation space |
| [hollowSpace](hollowSpace.md) | Relates the hollow spaces to the Tunnel or TunnelPart |
| [idColumnName](idColumnName.md) | Specifies the name of the column that stores the identifier of the time-value... |
| [idColumnNo](idColumnNo.md) | Specifies the number of the column that stores the identifier of the time-val... |
| [identifier](identifier.md) |  |
| [idValue](idValue.md) | Specifies the value of the identifier for which the time-value-pairs are to b... |
| [imageURI](imageURI.md) | Specifies the URI that points to the external image data file |
| [implicitGeometryValue](implicitGeometryValue.md) | Specifies the "ImplicitGeometry" value of the TimeValuePair |
| [informationSystem](informationSystem.md) | Specifies the URI that points to the external information system |
| [intersection](intersection.md) | Relates to the intersections that are part of the Railway |
| [interval](interval.md) | Indicates the time period the occupants are contained by a feature |
| [intValue](intValue.md) | Specifies the "Integer" value of the TimeValuePair |
| [isFront](isFront.md) | Indicates whether the texture or material is assigned to the front side or th... |
| [isMovable](isMovable.md) | Indicates whether the Bridge or BridgePart can be moved to allow for watercra... |
| [isSmooth](isSmooth.md) | Specifies which interpolation method is used for the shading of the surface g... |
| [isStructuralElement](isStructuralElement.md) | Indicates whether the constructive element is essential from a structural poi... |
| [lastTimestamp](lastTimestamp.md) | Specifies the end of the timeseries |
| [libraryObject](libraryObject.md) | Specifies the URI that points to the prototypical geometry stored in an exter... |
| [linkToObservation](linkToObservation.md) | Specifies the complete URL to the observation request |
| [linkToSensorDescription](linkToSensorDescription.md) | Specifies the complete URL to the sensor description request |
| [list](list.md) |  |
| [lod](lod.md) | Indicates the Level of Detail of the terrain component |
| [lod0MultiCurve](lod0MultiCurve.md) | Relates to a 3D MultiCurve geometry that represents the space in Level of Det... |
| [lod0MultiSurface](lod0MultiSurface.md) | Relates to a 3D MultiSurface geometry that represents the space in Level of D... |
| [lod0Point](lod0Point.md) | Relates to a 3D Point geometry that represents the space in Level of Detail 0 |
| [lod1ImplicitRepresentation](lod1ImplicitRepresentation.md) | Relates to an implicit geometry that represents the occupied space in Level o... |
| [lod1MultiSurface](lod1MultiSurface.md) | Relates to a 3D MultiSurface geometry that represents the thematic surface in... |
| [lod1Solid](lod1Solid.md) | Relates to a 3D Solid geometry that represents the space in Level of Detail 1 |
| [lod1TerrainIntersectionCurve](lod1TerrainIntersectionCurve.md) | Relates to a 3D MultiCurve geometry that represents the terrain intersection ... |
| [lod2ImplicitRepresentation](lod2ImplicitRepresentation.md) | Relates to an implicit geometry that represents the occupied space in Level o... |
| [lod2MultiCurve](lod2MultiCurve.md) | Relates to a 3D MultiCurve geometry that represents the space in Level of Det... |
| [lod2MultiSurface](lod2MultiSurface.md) | Relates to a 3D MultiSurface geometry that represents the space in Level of D... |
| [lod2Solid](lod2Solid.md) | Relates to a 3D Solid geometry that represents the space in Level of Detail 2 |
| [lod2TerrainIntersectionCurve](lod2TerrainIntersectionCurve.md) | Relates to a 3D MultiCurve geometry that represents the terrain intersection ... |
| [lod3ImplicitRepresentation](lod3ImplicitRepresentation.md) | Relates to an implicit geometry that represents the occupied space in Level o... |
| [lod3MultiCurve](lod3MultiCurve.md) | Relates to a 3D MultiCurve geometry that represents the space in Level of Det... |
| [lod3MultiSurface](lod3MultiSurface.md) | Relates to a 3D MultiSurface geometry that represents the space in Level of D... |
| [lod3Solid](lod3Solid.md) | Relates to a 3D Solid geometry that represents the space in Level of Detail 3 |
| [lod3TerrainIntersectionCurve](lod3TerrainIntersectionCurve.md) | Relates to a 3D MultiCurve geometry that represents the terrain intersection ... |
| [lowReference](lowReference.md) | Indicates the low point used to calculate the value of the height |
| [marking](marking.md) | Relates to the markings that are part of the transportation space |
| [maxHeight](maxHeight.md) | Specifies the maximum height of the PlantCover |
| [maxRootBallDepth](maxRootBallDepth.md) | Specifies the vertical distance between the lowest point of the SolitaryVeget... |
| [mimeType](mimeType.md) | Specifies the MIME type of the external timeseries file |
| [minHeight](minHeight.md) | Specifies the minimum height of the PlantCover |
| [mqttServer](mqttServer.md) | Specifies the name of the MQTT Server |
| [mqttTopic](mqttTopic.md) | Names the specific datastream that is retrieved by the SensorConnection |
| [multiPoint](multiPoint.md) | Relates to the MultiPoint geometry of the Address |
| [name](name.md) | Specifies the name of the CodeAttribute |
| [newFeature](newFeature.md) | Relates to the version of the city object subsequent to the Transaction |
| [nilReason](nilReason.md) |  |
| [nilReasonEnumeration](nilReasonEnumeration.md) |  |
| [numberOfHeaderLines](numberOfHeaderLines.md) | Indicates the number of lines at the beginning of the tabulated file that rep... |
| [numberOfOccupants](numberOfOccupants.md) | Indicates the number of occupants contained by a feature |
| [objectID](objectID.md) |  |
| [observationID](observationID.md) | Specifies the unique identifier of the observation that is retrieved by the S... |
| [observationProperty](observationProperty.md) | Specifies the phenomenon for which the SensorConnection provides observations |
| [occupancy](occupancy.md) | Provides qualified information on the residency of persons, animals, or other... |
| [occupantType](occupantType.md) | Indicates the specific type of the occupants that are contained by a feature |
| [oldFeature](oldFeature.md) | Relates to the version of the city object prior to the Transaction |
| [orientation](orientation.md) | Specifies the rotation and scaling of the image in form of a 2x2 matrix |
| [parent](parent.md) | Relates to a city object to which the CityObjectGroup belongs |
| [pointCloud](pointCloud.md) | Relates to a 3D PointCloud that represents the physical space |
| [pointFile](pointFile.md) | Specifies the URI that points to the external point cloud file |
| [pointFileSrsName](pointFileSrsName.md) | Indicates the coordinate reference system used by the external point cloud fi... |
| [points](points.md) | Relates to the 3D MultiPoint geometry of the PointCloud stored inline with th... |
| [predecessor](predecessor.md) | Indicates the predecessor(s) of the TrafficSpace |
| [preferWorldFile](preferWorldFile.md) | Indicates whether the georeference from the image file or the accompanying wo... |
| [reason](reason.md) | Specifies why the VersionTransition has been carried out |
| [referencePoint](referencePoint.md) | Relates to the 2D Point geometry that represents the center of the upper left... |
| [relatedTo](relatedTo.md) |  |
| [relationToConstruction](relationToConstruction.md) | Indicates whether the installation is located inside and/or outside of the co... |
| [relationType](relationType.md) | Specifies a URI that additionally qualifies the ExternalReference |
| [relativeGeometry](relativeGeometry.md) | Relates to a prototypical geometry in a local coordinate system stored inline... |
| [relativeToTerrain](relativeToTerrain.md) | Describes the vertical position of the city object relative to the surroundin... |
| [relativeToWater](relativeToWater.md) | Describes the vertical position of the city object relative to the surroundin... |
| [reliefComponent](reliefComponent.md) | Relates to the terrain components that are part of the ReliefFeature |
| [reliefPoints](reliefPoints.md) | Relates to the 3D MultiPoint geometry of the MassPointRelief |
| [repetitions](repetitions.md) | Specifies how often the timeseries that is referenced by the TimeseriesCompon... |
| [ridgeOrValleyLines](ridgeOrValleyLines.md) | Relates to the 3D MultiCurve geometry of the MassPointRelief |
| [ring](ring.md) | Specifies the URIs that point to the LinearRings that are parameterized using... |
| [roofType](roofType.md) | Indicates the shape of the roof of the Building or BuildingPart |
| [roomHeight](roomHeight.md) | Specifies qualified heights of the BuildingRoom |
| [rootBallDiameter](rootBallDiameter.md) | Specifies the diameter of the SolitaryCityObject's root ball |
| [section](section.md) | Relates to the sections that are part of the Railway |
| [sensorConnection](sensorConnection.md) | Relates to the sensor API that delivers timeseries data |
| [sensorID](sensorID.md) | Specifies the unique identifier of the sensor from which the SensorConnection... |
| [sensorLocation](sensorLocation.md) | Relates the sensor to the city object where it is located |
| [sensorName](sensorName.md) | Specifies the name of the sensor from which the SensorConnection retrieves ob... |
| [shininess](shininess.md) | Specifies the sharpness of the specular highlight |
| [sortKey](sortKey.md) | Defines an order among the objects that belong to the building subdivision |
| [spaceType](spaceType.md) | Specifies the degree of openness of a space |
| [species](species.md) | Indicates the botanical name of the SolitaryVegetationObject |
| [specularColor](specularColor.md) | Specifies the color of the light directly reflected by the surface geometry o... |
| [startTime](startTime.md) | Specifies the beginning of the time span for which the Dynamizer provides dyn... |
| [status](status.md) | Indicates the way the height has been captured |
| [storey](storey.md) | Relates to the storeys on which the BuildingUnit is located |
| [storeyHeightsAboveGround](storeyHeightsAboveGround.md) | Lists the heights of each storey above ground |
| [storeyHeightsBelowGround](storeyHeightsBelowGround.md) | Lists the height of each storey below ground |
| [storeysAboveGround](storeysAboveGround.md) | Indicates the number of storeys positioned above ground level |
| [storeysBelowGround](storeysBelowGround.md) | Indicates the number of storeys positioned below ground level |
| [stringValue](stringValue.md) | Specifies the "String" value of the TimeValuePair |
| [successor](successor.md) | Indicates the successor(s) of the TrafficSpace |
| [surfaceData](surfaceData.md) | Relates to the surface data that are part of the Appearance |
| [surfaceMaterial](surfaceMaterial.md) | Specifies the type of pavement of the AuxiliaryTrafficArea |
| [tag](tag.md) | Allows for adding keywords to the city model version |
| [target](target.md) | Specifies the URI that points to the surface geometry objects to which the te... |
| [targetResource](targetResource.md) | Specifies the URI that points to the object in the external information syste... |
| [terminationDate](terminationDate.md) | Indicates the date at which a CityGML feature was removed from the CityModel |
| [textureCoordinates](textureCoordinates.md) | Specifies the coordinates of texture used for parameterization |
| [textureParameterization](textureParameterization.md) | Relates to the texture coordinates or transformation matrices used for parame... |
| [textureType](textureType.md) | Indicates the specific type of the texture |
| [theme](theme.md) | Specifies the topic of the Appearance |
| [timeColumnName](timeColumnName.md) | Specifies the name of the column that stores the timestamp of the time-value-... |
| [timeColumnNo](timeColumnNo.md) | Specifies the number of the column that stores the timestamp of the time-valu... |
| [timeseries](timeseries.md) | Relates a timeseries to the TimeseriesComponent |
| [timestamp](timestamp.md) | Specifies the timepoint at which the value of the TimeValuePair is valid |
| [timeValuePair](timeValuePair.md) | Relates to the time-value-pairs that are part of the GenericTimeseries |
| [tin](tin.md) | Relates to the triangulated surface of the TINRelief |
| [to](to.md) | Relates to the successor version of the VersionTransition |
| [trafficDirection](trafficDirection.md) | Indicates the direction of traffic flow relative to the corresponding linear ... |
| [trafficSpace](trafficSpace.md) | Relates to the traffic spaces that are part of the transportation space |
| [transaction](transaction.md) | Relates to all transactions that have been applied as part of the VersionTran... |
| [transformationMatrix](transformationMatrix.md) | Specifies the mathematical transformation (translation, rotation, and scaling... |
| [transparency](transparency.md) | Specifies the degree of transparency of the surface geometry object |
| [trunkDiameter](trunkDiameter.md) | Specifies the diameter of the SolitaryCityObject's trunk |
| [tunnelConstructiveElement](tunnelConstructiveElement.md) | Relates the constructive elements to the Tunnel or TunnelPart |
| [tunnelFurniture](tunnelFurniture.md) | Relates the furniture objects to the Tunnel or TunnelPart |
| [tunnelInstallation](tunnelInstallation.md) | Relates the installation objects to the Tunnel or TunnelPart |
| [tunnelPart](tunnelPart.md) | Relates the tunnel parts to the Tunnel |
| [type](type.md) | Indicates the specific type of the Transaction |
| [typeOfArea](typeOfArea.md) | Indicates the specific type of the QualifiedArea |
| [typeOfVolume](typeOfVolume.md) | Indicates the specific type of the QualifiedVolume |
| [uom](uom.md) | Specifies the unit of measurement of the observations |
| [URI](URI.md) |  |
| [uriValue](uriValue.md) | Specifies the "URI" value of the TimeValuePair |
| [usage](usage.md) | Specifies the actual uses of the Door |
| [validFrom](validFrom.md) | Indicates the date at which a CityGML feature started to exist in the real wo... |
| [validTo](validTo.md) | Indicates the date at which a CityGML feature ended to exist in the real worl... |
| [value](value.md) | Specifies the value of the height above or below ground |
| [valueColumnName](valueColumnName.md) | Specifies the name of the column that stores the value of the time-value-pair |
| [valueColumnNo](valueColumnNo.md) | Specifies the number of the column that stores the value of the time-value-pa... |
| [valueType](valueType.md) | Indicates the specific type of all time-value-pairs that are part of the Gene... |
| [versionMember](versionMember.md) |  |
| [versionTransitionMember](versionTransitionMember.md) |  |
| [volume](volume.md) | Specifies the value of the QualifiedVolume |
| [waterLevel](waterLevel.md) | Specifies the level of the WaterSurface |
| [worldToTexture](worldToTexture.md) | Specifies the 3x4 transformation matrix that defines the transformation betwe... |
| [wrapMode](wrapMode.md) | Specifies the behaviour of the texture when the texture is smaller than the s... |
| [xalAddress](xalAddress.md) | Relates an OASIS address object to the Address |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [ConditionOfConstructionValue](ConditionOfConstructionValue.md) | ConditionOfConstructionValue enumerates different conditions of a constructio... |
| [GranularityValue](GranularityValue.md) | GranularityValue enumerates the different levels of granularity in which tran... |
| [HeightStatusValue](HeightStatusValue.md) | HeightStatusValue enumerates the different methods used to capture a height |
| [RelationToConstruction](RelationToConstruction.md) | RelationToConstruction is an enumeration used to describe whether an installa... |
| [RelativeToTerrain](RelativeToTerrain.md) | RelativeToTerrain enumerates the spatial relations of a city object relative ... |
| [RelativeToWater](RelativeToWater.md) | RelativeToWater enumerates the spatial relations of a city object relative to... |
| [SpaceType](SpaceType.md) | SpaceType is an enumeration that characterises a space according to its closu... |
| [TextureType](TextureType.md) | TextureType enumerates the different texture types |
| [TimeseriesTypeValue](TimeseriesTypeValue.md) | TimeseriesTypeValue enumerates the possible value types for GenericTimeseries... |
| [TrafficDirectionValue](TrafficDirectionValue.md) | TrafficDirectionValue enumerates the allowed directions of travel of a mobile... |
| [TransactionTypeValue](TransactionTypeValue.md) | TransactionTypeValue enumerates the three possible types of transactions: ins... |
| [TransitionTypeValue](TransitionTypeValue.md) | TransitionTypeValue enumerates the different kinds of version transitions |
| [WrapMode](WrapMode.md) | WrapMode enumerates the different fill modes for textures |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
