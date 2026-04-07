

# Class: QualifiedArea 


_QualifiedArea is an application-dependent measure of the area of a space or of a thematic surface._





URI: [citygml:QualifiedArea](https://www.ogc.org/standards/citygml/QualifiedArea)





```mermaid
 classDiagram
    class QualifiedArea
    click QualifiedArea href "../QualifiedArea/"
      QualifiedArea : area
        
      QualifiedArea : typeOfArea
        
          
    
        
        
        QualifiedArea --> "1" QualifiedAreaTypeValue : typeOfArea
        click QualifiedAreaTypeValue href "../QualifiedAreaTypeValue/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [area](area.md) | 1 <br/> [Float](Float.md) | Specifies the value of the QualifiedArea | direct |
| [typeOfArea](typeOfArea.md) | 1 <br/> [QualifiedAreaTypeValue](QualifiedAreaTypeValue.md) | Indicates the specific type of the QualifiedArea | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AbstractConstruction](AbstractConstruction.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractConstructionSurface](AbstractConstructionSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractConstructiveElement](AbstractConstructiveElement.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractFillingElement](AbstractFillingElement.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractFillingSurface](AbstractFillingSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractFurniture](AbstractFurniture.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractInstallation](AbstractInstallation.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [CeilingSurface](CeilingSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Door](Door.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [DoorSurface](DoorSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [FloorSurface](FloorSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [GroundSurface](GroundSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [InteriorWallSurface](InteriorWallSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [OtherConstruction](OtherConstruction.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [OuterCeilingSurface](OuterCeilingSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [OuterFloorSurface](OuterFloorSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [RoofSurface](RoofSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [WallSurface](WallSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Window](Window.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [WindowSurface](WindowSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractBridge](AbstractBridge.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Bridge](Bridge.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [BridgeConstructiveElement](BridgeConstructiveElement.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [BridgeFurniture](BridgeFurniture.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [BridgeInstallation](BridgeInstallation.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [BridgePart](BridgePart.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [BridgeRoom](BridgeRoom.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractBuilding](AbstractBuilding.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Building](Building.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [BuildingConstructiveElement](BuildingConstructiveElement.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [BuildingFurniture](BuildingFurniture.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [BuildingInstallation](BuildingInstallation.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [BuildingPart](BuildingPart.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [BuildingRoom](BuildingRoom.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [BuildingUnit](BuildingUnit.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Storey](Storey.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [CityFurniture](CityFurniture.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [CityObjectGroup](CityObjectGroup.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractLogicalSpace](AbstractLogicalSpace.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractOccupiedSpace](AbstractOccupiedSpace.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractPhysicalSpace](AbstractPhysicalSpace.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractSpace](AbstractSpace.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractThematicSurface](AbstractThematicSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractUnoccupiedSpace](AbstractUnoccupiedSpace.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [ClosureSurface](ClosureSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [GenericLogicalSpace](GenericLogicalSpace.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [GenericOccupiedSpace](GenericOccupiedSpace.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [GenericThematicSurface](GenericThematicSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [GenericUnoccupiedSpace](GenericUnoccupiedSpace.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [LandUse](LandUse.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractTransportationSpace](AbstractTransportationSpace.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AuxiliaryTrafficArea](AuxiliaryTrafficArea.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AuxiliaryTrafficSpace](AuxiliaryTrafficSpace.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [ClearanceSpace](ClearanceSpace.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Hole](Hole.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [HoleSurface](HoleSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Intersection](Intersection.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Marking](Marking.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Railway](Railway.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Road](Road.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Section](Section.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Square](Square.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Track](Track.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [TrafficArea](TrafficArea.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [TrafficSpace](TrafficSpace.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Waterway](Waterway.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractTunnel](AbstractTunnel.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [HollowSpace](HollowSpace.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [Tunnel](Tunnel.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [TunnelConstructiveElement](TunnelConstructiveElement.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [TunnelFurniture](TunnelFurniture.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [TunnelInstallation](TunnelInstallation.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [TunnelPart](TunnelPart.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractVegetationObject](AbstractVegetationObject.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [PlantCover](PlantCover.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [SolitaryVegetationObject](SolitaryVegetationObject.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [AbstractWaterBoundarySurface](AbstractWaterBoundarySurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [WaterBody](WaterBody.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [WaterGroundSurface](WaterGroundSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |
| [WaterSurface](WaterSurface.md) | [area](area.md) | range | [QualifiedArea](QualifiedArea.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:QualifiedArea |
| native | citygml:QualifiedArea |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: QualifiedArea
description: QualifiedArea is an application-dependent measure of the area of a space
  or of a thematic surface.
from_schema: https://www.ogc.org/standards/citygml
abstract: false
attributes:
  area:
    name: area
    description: Specifies the value of the QualifiedArea.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - QualifiedArea
    - AbstractSpace
    - AbstractThematicSurface
    range: float
    required: true
    multivalued: false
  typeOfArea:
    name: typeOfArea
    description: Indicates the specific type of the QualifiedArea.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - QualifiedArea
    range: QualifiedAreaTypeValue
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: QualifiedArea
description: QualifiedArea is an application-dependent measure of the area of a space
  or of a thematic surface.
from_schema: https://www.ogc.org/standards/citygml
abstract: false
attributes:
  area:
    name: area
    description: Specifies the value of the QualifiedArea.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: area
    owner: QualifiedArea
    domain_of:
    - QualifiedArea
    - AbstractSpace
    - AbstractThematicSurface
    range: float
    required: true
    multivalued: false
  typeOfArea:
    name: typeOfArea
    description: Indicates the specific type of the QualifiedArea.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: typeOfArea
    owner: QualifiedArea
    domain_of:
    - QualifiedArea
    range: QualifiedAreaTypeValue
    required: true
    multivalued: false

```
</details>