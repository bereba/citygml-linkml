

# Class: QualifiedVolume 


_QualifiedVolume is an application-dependent measure of the volume of a space._





URI: [citygml:QualifiedVolume](https://www.ogc.org/standards/citygml/QualifiedVolume)





```mermaid
 classDiagram
    class QualifiedVolume
    click QualifiedVolume href "../QualifiedVolume/"
      QualifiedVolume : typeOfVolume
        
          
    
        
        
        QualifiedVolume --> "1" QualifiedVolumeTypeValue : typeOfVolume
        click QualifiedVolumeTypeValue href "../QualifiedVolumeTypeValue/"
    

        
      QualifiedVolume : volume
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [volume](volume.md) | 1 <br/> [Float](Float.md) | Specifies the value of the QualifiedVolume | direct |
| [typeOfVolume](typeOfVolume.md) | 1 <br/> [QualifiedVolumeTypeValue](QualifiedVolumeTypeValue.md) | Indicates the specific type of the QualifiedVolume | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AbstractConstruction](AbstractConstruction.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractConstructiveElement](AbstractConstructiveElement.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractFillingElement](AbstractFillingElement.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractFurniture](AbstractFurniture.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractInstallation](AbstractInstallation.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [Door](Door.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [OtherConstruction](OtherConstruction.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [Window](Window.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractBridge](AbstractBridge.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [Bridge](Bridge.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [BridgeConstructiveElement](BridgeConstructiveElement.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [BridgeFurniture](BridgeFurniture.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [BridgeInstallation](BridgeInstallation.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [BridgePart](BridgePart.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [BridgeRoom](BridgeRoom.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractBuilding](AbstractBuilding.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [Building](Building.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [BuildingConstructiveElement](BuildingConstructiveElement.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [BuildingFurniture](BuildingFurniture.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [BuildingInstallation](BuildingInstallation.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [BuildingPart](BuildingPart.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [BuildingRoom](BuildingRoom.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [BuildingUnit](BuildingUnit.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [Storey](Storey.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [CityFurniture](CityFurniture.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [CityObjectGroup](CityObjectGroup.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractLogicalSpace](AbstractLogicalSpace.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractOccupiedSpace](AbstractOccupiedSpace.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractPhysicalSpace](AbstractPhysicalSpace.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractSpace](AbstractSpace.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractUnoccupiedSpace](AbstractUnoccupiedSpace.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [GenericLogicalSpace](GenericLogicalSpace.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [GenericOccupiedSpace](GenericOccupiedSpace.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [GenericUnoccupiedSpace](GenericUnoccupiedSpace.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractTransportationSpace](AbstractTransportationSpace.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AuxiliaryTrafficSpace](AuxiliaryTrafficSpace.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [ClearanceSpace](ClearanceSpace.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [Hole](Hole.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [Intersection](Intersection.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [Railway](Railway.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [Road](Road.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [Section](Section.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [Square](Square.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [Track](Track.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [TrafficSpace](TrafficSpace.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [Waterway](Waterway.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractTunnel](AbstractTunnel.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [HollowSpace](HollowSpace.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [Tunnel](Tunnel.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [TunnelConstructiveElement](TunnelConstructiveElement.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [TunnelFurniture](TunnelFurniture.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [TunnelInstallation](TunnelInstallation.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [TunnelPart](TunnelPart.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [AbstractVegetationObject](AbstractVegetationObject.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [PlantCover](PlantCover.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [SolitaryVegetationObject](SolitaryVegetationObject.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |
| [WaterBody](WaterBody.md) | [volume](volume.md) | range | [QualifiedVolume](QualifiedVolume.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:QualifiedVolume |
| native | citygml:QualifiedVolume |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: QualifiedVolume
description: QualifiedVolume is an application-dependent measure of the volume of
  a space.
from_schema: https://www.ogc.org/standards/citygml
abstract: false
attributes:
  volume:
    name: volume
    description: Specifies the value of the QualifiedVolume.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - QualifiedVolume
    - AbstractSpace
    range: float
    required: true
    multivalued: false
  typeOfVolume:
    name: typeOfVolume
    description: Indicates the specific type of the QualifiedVolume.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - QualifiedVolume
    range: QualifiedVolumeTypeValue
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: QualifiedVolume
description: QualifiedVolume is an application-dependent measure of the volume of
  a space.
from_schema: https://www.ogc.org/standards/citygml
abstract: false
attributes:
  volume:
    name: volume
    description: Specifies the value of the QualifiedVolume.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: volume
    owner: QualifiedVolume
    domain_of:
    - QualifiedVolume
    - AbstractSpace
    range: float
    required: true
    multivalued: false
  typeOfVolume:
    name: typeOfVolume
    description: Indicates the specific type of the QualifiedVolume.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: typeOfVolume
    owner: QualifiedVolume
    domain_of:
    - QualifiedVolume
    range: QualifiedVolumeTypeValue
    required: true
    multivalued: false

```
</details>