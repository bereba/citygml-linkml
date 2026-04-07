

# Class: AbstractGenericAttribute 


_AbstractGenericAttribute is the abstract superclass for all types of generic attributes._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [citygml:AbstractGenericAttribute](https://www.ogc.org/standards/citygml/AbstractGenericAttribute)





```mermaid
 classDiagram
    class AbstractGenericAttribute
    click AbstractGenericAttribute href "../AbstractGenericAttribute/"
      AbstractGenericAttribute <|-- CodeAttribute
        click CodeAttribute href "../CodeAttribute/"
      AbstractGenericAttribute <|-- DateAttribute
        click DateAttribute href "../DateAttribute/"
      AbstractGenericAttribute <|-- DoubleAttribute
        click DoubleAttribute href "../DoubleAttribute/"
      AbstractGenericAttribute <|-- GenericAttributeSet
        click GenericAttributeSet href "../GenericAttributeSet/"
      AbstractGenericAttribute <|-- IntAttribute
        click IntAttribute href "../IntAttribute/"
      AbstractGenericAttribute <|-- MeasureAttribute
        click MeasureAttribute href "../MeasureAttribute/"
      AbstractGenericAttribute <|-- StringAttribute
        click StringAttribute href "../StringAttribute/"
      AbstractGenericAttribute <|-- UriAttribute
        click UriAttribute href "../UriAttribute/"
      
      
```





## Inheritance
* **AbstractGenericAttribute**
    * [CodeAttribute](CodeAttribute.md)
    * [DateAttribute](DateAttribute.md)
    * [DoubleAttribute](DoubleAttribute.md)
    * [GenericAttributeSet](GenericAttributeSet.md)
    * [IntAttribute](IntAttribute.md)
    * [MeasureAttribute](MeasureAttribute.md)
    * [StringAttribute](StringAttribute.md)
    * [UriAttribute](UriAttribute.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GenericAttributeSet](GenericAttributeSet.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractConstruction](AbstractConstruction.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractConstructionSurface](AbstractConstructionSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractConstructiveElement](AbstractConstructiveElement.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractFillingElement](AbstractFillingElement.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractFillingSurface](AbstractFillingSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractFurniture](AbstractFurniture.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractInstallation](AbstractInstallation.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [CeilingSurface](CeilingSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Door](Door.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [DoorSurface](DoorSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [FloorSurface](FloorSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [GroundSurface](GroundSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [InteriorWallSurface](InteriorWallSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [OtherConstruction](OtherConstruction.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [OuterCeilingSurface](OuterCeilingSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [OuterFloorSurface](OuterFloorSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [RoofSurface](RoofSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [WallSurface](WallSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Window](Window.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [WindowSurface](WindowSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractBridge](AbstractBridge.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Bridge](Bridge.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [BridgeConstructiveElement](BridgeConstructiveElement.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [BridgeFurniture](BridgeFurniture.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [BridgeInstallation](BridgeInstallation.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [BridgePart](BridgePart.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [BridgeRoom](BridgeRoom.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractBuilding](AbstractBuilding.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Building](Building.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [BuildingConstructiveElement](BuildingConstructiveElement.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [BuildingFurniture](BuildingFurniture.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [BuildingInstallation](BuildingInstallation.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [BuildingPart](BuildingPart.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [BuildingRoom](BuildingRoom.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [BuildingUnit](BuildingUnit.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Storey](Storey.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [CityFurniture](CityFurniture.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [CityObjectGroup](CityObjectGroup.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractCityObject](AbstractCityObject.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractLogicalSpace](AbstractLogicalSpace.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractOccupiedSpace](AbstractOccupiedSpace.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractPhysicalSpace](AbstractPhysicalSpace.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractSpace](AbstractSpace.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractSpaceBoundary](AbstractSpaceBoundary.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractThematicSurface](AbstractThematicSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractUnoccupiedSpace](AbstractUnoccupiedSpace.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [ClosureSurface](ClosureSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [GenericLogicalSpace](GenericLogicalSpace.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [GenericOccupiedSpace](GenericOccupiedSpace.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [GenericThematicSurface](GenericThematicSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [GenericUnoccupiedSpace](GenericUnoccupiedSpace.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [LandUse](LandUse.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractReliefComponent](AbstractReliefComponent.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [BreaklineRelief](BreaklineRelief.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [MassPointRelief](MassPointRelief.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [RasterRelief](RasterRelief.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [ReliefFeature](ReliefFeature.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [TINRelief](TINRelief.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractTransportationSpace](AbstractTransportationSpace.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AuxiliaryTrafficArea](AuxiliaryTrafficArea.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AuxiliaryTrafficSpace](AuxiliaryTrafficSpace.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [ClearanceSpace](ClearanceSpace.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Hole](Hole.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [HoleSurface](HoleSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Intersection](Intersection.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Marking](Marking.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Railway](Railway.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Road](Road.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Section](Section.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Square](Square.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Track](Track.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [TrafficArea](TrafficArea.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [TrafficSpace](TrafficSpace.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Waterway](Waterway.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractTunnel](AbstractTunnel.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [HollowSpace](HollowSpace.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [Tunnel](Tunnel.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [TunnelConstructiveElement](TunnelConstructiveElement.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [TunnelFurniture](TunnelFurniture.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [TunnelInstallation](TunnelInstallation.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [TunnelPart](TunnelPart.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractVegetationObject](AbstractVegetationObject.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [PlantCover](PlantCover.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [SolitaryVegetationObject](SolitaryVegetationObject.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [AbstractWaterBoundarySurface](AbstractWaterBoundarySurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [WaterBody](WaterBody.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [WaterGroundSurface](WaterGroundSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |
| [WaterSurface](WaterSurface.md) | [genericAttribute](genericAttribute.md) | range | [AbstractGenericAttribute](AbstractGenericAttribute.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:AbstractGenericAttribute |
| native | citygml:AbstractGenericAttribute |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AbstractGenericAttribute
description: AbstractGenericAttribute is the abstract superclass for all types of
  generic attributes.
from_schema: https://www.ogc.org/standards/citygml
abstract: true

```
</details>

### Induced

<details>
```yaml
name: AbstractGenericAttribute
description: AbstractGenericAttribute is the abstract superclass for all types of
  generic attributes.
from_schema: https://www.ogc.org/standards/citygml
abstract: true

```
</details>