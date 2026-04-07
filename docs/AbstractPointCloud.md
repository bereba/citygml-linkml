

# Class: AbstractPointCloud 


_AbstractPointCloud is the abstract superclass to represent PointCloud objects._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [citygml:AbstractPointCloud](https://www.ogc.org/standards/citygml/AbstractPointCloud)





```mermaid
 classDiagram
    class AbstractPointCloud
    click AbstractPointCloud href "../AbstractPointCloud/"
      AbstractFeature <|-- AbstractPointCloud
        click AbstractFeature href "../AbstractFeature/"
      

      AbstractPointCloud <|-- PointCloud
        click PointCloud href "../PointCloud/"
      

      AbstractPointCloud : adeOfAbstractFeature
        
          
    
        
        
        AbstractPointCloud --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      AbstractPointCloud : adeOfAbstractPointCloud
        
          
    
        
        
        AbstractPointCloud --> "*" ADEOfAbstractPointCloud : adeOfAbstractPointCloud
        click ADEOfAbstractPointCloud href "../ADEOfAbstractPointCloud/"
    

        
      AbstractPointCloud : description
        
      AbstractPointCloud : featureID
        
          
    
        
        
        AbstractPointCloud --> "1" ID : featureID
        click ID href "../ID/"
    

        
      AbstractPointCloud : identifier
        
      AbstractPointCloud : name
        
      
```





## Inheritance
* [AbstractFeature](AbstractFeature.md)
    * **AbstractPointCloud**
        * [PointCloud](PointCloud.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [adeOfAbstractPointCloud](adeOfAbstractPointCloud.md) | * <br/> [ADEOfAbstractPointCloud](ADEOfAbstractPointCloud.md) | Augments AbstractPointCloud with properties defined in an ADE | direct |
| [featureID](featureID.md) | 1 <br/> [ID](ID.md) |  | [AbstractFeature](AbstractFeature.md) |
| [identifier](identifier.md) | 0..1 <br/> [String](String.md) |  | [AbstractFeature](AbstractFeature.md) |
| [name](name.md) | * <br/> [String](String.md) |  | [AbstractFeature](AbstractFeature.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [AbstractFeature](AbstractFeature.md) |
| [adeOfAbstractFeature](adeOfAbstractFeature.md) | * <br/> [ADEOfAbstractFeature](ADEOfAbstractFeature.md) | Augments AbstractFeature with properties defined in an ADE | [AbstractFeature](AbstractFeature.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AbstractConstruction](AbstractConstruction.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractConstructionSurface](AbstractConstructionSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractConstructiveElement](AbstractConstructiveElement.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractFillingElement](AbstractFillingElement.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractFillingSurface](AbstractFillingSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractFurniture](AbstractFurniture.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractInstallation](AbstractInstallation.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [CeilingSurface](CeilingSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [Door](Door.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [DoorSurface](DoorSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [FloorSurface](FloorSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [GroundSurface](GroundSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [InteriorWallSurface](InteriorWallSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [OtherConstruction](OtherConstruction.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [OuterCeilingSurface](OuterCeilingSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [OuterFloorSurface](OuterFloorSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [RoofSurface](RoofSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [WallSurface](WallSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [Window](Window.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [WindowSurface](WindowSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractBridge](AbstractBridge.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [Bridge](Bridge.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [BridgeConstructiveElement](BridgeConstructiveElement.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [BridgeFurniture](BridgeFurniture.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [BridgeInstallation](BridgeInstallation.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [BridgePart](BridgePart.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [BridgeRoom](BridgeRoom.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractBuilding](AbstractBuilding.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [Building](Building.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [BuildingConstructiveElement](BuildingConstructiveElement.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [BuildingFurniture](BuildingFurniture.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [BuildingInstallation](BuildingInstallation.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [BuildingPart](BuildingPart.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [BuildingRoom](BuildingRoom.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [CityFurniture](CityFurniture.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractOccupiedSpace](AbstractOccupiedSpace.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractPhysicalSpace](AbstractPhysicalSpace.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractThematicSurface](AbstractThematicSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractUnoccupiedSpace](AbstractUnoccupiedSpace.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [ClosureSurface](ClosureSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [GenericOccupiedSpace](GenericOccupiedSpace.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [GenericThematicSurface](GenericThematicSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [GenericUnoccupiedSpace](GenericUnoccupiedSpace.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [LandUse](LandUse.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [MassPointRelief](MassPointRelief.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractTransportationSpace](AbstractTransportationSpace.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AuxiliaryTrafficArea](AuxiliaryTrafficArea.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AuxiliaryTrafficSpace](AuxiliaryTrafficSpace.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [ClearanceSpace](ClearanceSpace.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [Hole](Hole.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [HoleSurface](HoleSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [Intersection](Intersection.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [Marking](Marking.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [Railway](Railway.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [Road](Road.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [Section](Section.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [Square](Square.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [Track](Track.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [TrafficArea](TrafficArea.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [TrafficSpace](TrafficSpace.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [Waterway](Waterway.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractTunnel](AbstractTunnel.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [HollowSpace](HollowSpace.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [Tunnel](Tunnel.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [TunnelConstructiveElement](TunnelConstructiveElement.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [TunnelFurniture](TunnelFurniture.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [TunnelInstallation](TunnelInstallation.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [TunnelPart](TunnelPart.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractVegetationObject](AbstractVegetationObject.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [PlantCover](PlantCover.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [SolitaryVegetationObject](SolitaryVegetationObject.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [AbstractWaterBoundarySurface](AbstractWaterBoundarySurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [WaterBody](WaterBody.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [WaterGroundSurface](WaterGroundSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |
| [WaterSurface](WaterSurface.md) | [pointCloud](pointCloud.md) | range | [AbstractPointCloud](AbstractPointCloud.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:AbstractPointCloud |
| native | citygml:AbstractPointCloud |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AbstractPointCloud
description: AbstractPointCloud is the abstract superclass to represent PointCloud
  objects.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractFeature
abstract: true
attributes:
  adeOfAbstractPointCloud:
    name: adeOfAbstractPointCloud
    description: Augments AbstractPointCloud with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractPointCloud
    range: ADEOfAbstractPointCloud
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: AbstractPointCloud
description: AbstractPointCloud is the abstract superclass to represent PointCloud
  objects.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractFeature
abstract: true
attributes:
  adeOfAbstractPointCloud:
    name: adeOfAbstractPointCloud
    description: Augments AbstractPointCloud with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractPointCloud
    owner: AbstractPointCloud
    domain_of:
    - AbstractPointCloud
    range: ADEOfAbstractPointCloud
    required: false
    multivalued: true
  featureID:
    name: featureID
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: featureID
    owner: AbstractPointCloud
    domain_of:
    - AbstractFeature
    range: ID
    required: true
    multivalued: false
  identifier:
    name: identifier
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: identifier
    owner: AbstractPointCloud
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: AbstractPointCloud
    domain_of:
    - CodeAttribute
    - DateAttribute
    - DoubleAttribute
    - GenericAttributeSet
    - IntAttribute
    - MeasureAttribute
    - StringAttribute
    - UriAttribute
    - AbstractFeature
    range: string
    required: false
    multivalued: true
  description:
    name: description
    from_schema: https://www.ogc.org/standards/citygml
    alias: description
    owner: AbstractPointCloud
    domain_of:
    - ConstructionEvent
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  adeOfAbstractFeature:
    name: adeOfAbstractFeature
    description: Augments AbstractFeature with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractFeature
    owner: AbstractPointCloud
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>