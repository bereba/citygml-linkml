

# Class: AbstractAppearance 


_AbstractAppearance is the abstract superclass to represent any kind of appearance objects._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [citygml:AbstractAppearance](https://www.ogc.org/standards/citygml/AbstractAppearance)





```mermaid
 classDiagram
    class AbstractAppearance
    click AbstractAppearance href "../AbstractAppearance/"
      AbstractFeatureWithLifespan <|-- AbstractAppearance
        click AbstractFeatureWithLifespan href "../AbstractFeatureWithLifespan/"
      

      AbstractAppearance <|-- Appearance
        click Appearance href "../Appearance/"
      

      AbstractAppearance : adeOfAbstractAppearance
        
          
    
        
        
        AbstractAppearance --> "*" ADEOfAbstractAppearance : adeOfAbstractAppearance
        click ADEOfAbstractAppearance href "../ADEOfAbstractAppearance/"
    

        
      AbstractAppearance : adeOfAbstractFeature
        
          
    
        
        
        AbstractAppearance --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      AbstractAppearance : adeOfAbstractFeatureWithLifespan
        
          
    
        
        
        AbstractAppearance --> "*" ADEOfAbstractFeatureWithLifespan : adeOfAbstractFeatureWithLifespan
        click ADEOfAbstractFeatureWithLifespan href "../ADEOfAbstractFeatureWithLifespan/"
    

        
      AbstractAppearance : creationDate
        
      AbstractAppearance : description
        
      AbstractAppearance : featureID
        
          
    
        
        
        AbstractAppearance --> "1" ID : featureID
        click ID href "../ID/"
    

        
      AbstractAppearance : identifier
        
      AbstractAppearance : name
        
      AbstractAppearance : terminationDate
        
      AbstractAppearance : validFrom
        
      AbstractAppearance : validTo
        
      
```





## Inheritance
* [AbstractFeature](AbstractFeature.md)
    * [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md)
        * **AbstractAppearance**
            * [Appearance](Appearance.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [adeOfAbstractAppearance](adeOfAbstractAppearance.md) | * <br/> [ADEOfAbstractAppearance](ADEOfAbstractAppearance.md) | Augments AbstractAppearance with properties defined in an ADE | direct |
| [creationDate](creationDate.md) | 0..1 <br/> [Datetime](Datetime.md) | Indicates the date at which a CityGML feature was added to the CityModel | [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md) |
| [terminationDate](terminationDate.md) | 0..1 <br/> [Datetime](Datetime.md) | Indicates the date at which a CityGML feature was removed from the CityModel | [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md) |
| [validFrom](validFrom.md) | 0..1 <br/> [Datetime](Datetime.md) | Indicates the date at which a CityGML feature started to exist in the real wo... | [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md) |
| [validTo](validTo.md) | 0..1 <br/> [Datetime](Datetime.md) | Indicates the date at which a CityGML feature ended to exist in the real worl... | [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md) |
| [adeOfAbstractFeatureWithLifespan](adeOfAbstractFeatureWithLifespan.md) | * <br/> [ADEOfAbstractFeatureWithLifespan](ADEOfAbstractFeatureWithLifespan.md) | Augments AbstractFeatureWithLifespan with properties defined in an ADE | [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md) |
| [featureID](featureID.md) | 1 <br/> [ID](ID.md) |  | [AbstractFeature](AbstractFeature.md) |
| [identifier](identifier.md) | 0..1 <br/> [String](String.md) |  | [AbstractFeature](AbstractFeature.md) |
| [name](name.md) | * <br/> [String](String.md) |  | [AbstractFeature](AbstractFeature.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [AbstractFeature](AbstractFeature.md) |
| [adeOfAbstractFeature](adeOfAbstractFeature.md) | * <br/> [ADEOfAbstractFeature](ADEOfAbstractFeature.md) | Augments AbstractFeature with properties defined in an ADE | [AbstractFeature](AbstractFeature.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TimeValuePair](TimeValuePair.md) | [appearanceValue](appearanceValue.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [CityModelMember](CityModelMember.md) | [appearanceMember](appearanceMember.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractConstruction](AbstractConstruction.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractConstructionSurface](AbstractConstructionSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractConstructiveElement](AbstractConstructiveElement.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractFillingElement](AbstractFillingElement.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractFillingSurface](AbstractFillingSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractFurniture](AbstractFurniture.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractInstallation](AbstractInstallation.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [CeilingSurface](CeilingSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Door](Door.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [DoorSurface](DoorSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [FloorSurface](FloorSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [GroundSurface](GroundSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [InteriorWallSurface](InteriorWallSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [OtherConstruction](OtherConstruction.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [OuterCeilingSurface](OuterCeilingSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [OuterFloorSurface](OuterFloorSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [RoofSurface](RoofSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [WallSurface](WallSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Window](Window.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [WindowSurface](WindowSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractBridge](AbstractBridge.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Bridge](Bridge.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [BridgeConstructiveElement](BridgeConstructiveElement.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [BridgeFurniture](BridgeFurniture.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [BridgeInstallation](BridgeInstallation.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [BridgePart](BridgePart.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [BridgeRoom](BridgeRoom.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractBuilding](AbstractBuilding.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Building](Building.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [BuildingConstructiveElement](BuildingConstructiveElement.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [BuildingFurniture](BuildingFurniture.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [BuildingInstallation](BuildingInstallation.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [BuildingPart](BuildingPart.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [BuildingRoom](BuildingRoom.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [BuildingUnit](BuildingUnit.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Storey](Storey.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [CityFurniture](CityFurniture.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [CityObjectGroup](CityObjectGroup.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractCityObject](AbstractCityObject.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractLogicalSpace](AbstractLogicalSpace.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractOccupiedSpace](AbstractOccupiedSpace.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractPhysicalSpace](AbstractPhysicalSpace.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractSpace](AbstractSpace.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractSpaceBoundary](AbstractSpaceBoundary.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractThematicSurface](AbstractThematicSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractUnoccupiedSpace](AbstractUnoccupiedSpace.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [ClosureSurface](ClosureSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [ImplicitGeometry](ImplicitGeometry.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [GenericLogicalSpace](GenericLogicalSpace.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [GenericOccupiedSpace](GenericOccupiedSpace.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [GenericThematicSurface](GenericThematicSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [GenericUnoccupiedSpace](GenericUnoccupiedSpace.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [LandUse](LandUse.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractReliefComponent](AbstractReliefComponent.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [BreaklineRelief](BreaklineRelief.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [MassPointRelief](MassPointRelief.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [RasterRelief](RasterRelief.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [ReliefFeature](ReliefFeature.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [TINRelief](TINRelief.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractTransportationSpace](AbstractTransportationSpace.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AuxiliaryTrafficArea](AuxiliaryTrafficArea.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AuxiliaryTrafficSpace](AuxiliaryTrafficSpace.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [ClearanceSpace](ClearanceSpace.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Hole](Hole.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [HoleSurface](HoleSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Intersection](Intersection.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Marking](Marking.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Railway](Railway.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Road](Road.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Section](Section.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Square](Square.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Track](Track.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [TrafficArea](TrafficArea.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [TrafficSpace](TrafficSpace.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Waterway](Waterway.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractTunnel](AbstractTunnel.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [HollowSpace](HollowSpace.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [Tunnel](Tunnel.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [TunnelConstructiveElement](TunnelConstructiveElement.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [TunnelFurniture](TunnelFurniture.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [TunnelInstallation](TunnelInstallation.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [TunnelPart](TunnelPart.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractVegetationObject](AbstractVegetationObject.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [PlantCover](PlantCover.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [SolitaryVegetationObject](SolitaryVegetationObject.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [AbstractWaterBoundarySurface](AbstractWaterBoundarySurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [WaterBody](WaterBody.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [WaterGroundSurface](WaterGroundSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |
| [WaterSurface](WaterSurface.md) | [appearance](appearance.md) | range | [AbstractAppearance](AbstractAppearance.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:AbstractAppearance |
| native | citygml:AbstractAppearance |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AbstractAppearance
description: AbstractAppearance is the abstract superclass to represent any kind of
  appearance objects.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractFeatureWithLifespan
abstract: true
attributes:
  adeOfAbstractAppearance:
    name: adeOfAbstractAppearance
    description: Augments AbstractAppearance with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractAppearance
    range: ADEOfAbstractAppearance
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: AbstractAppearance
description: AbstractAppearance is the abstract superclass to represent any kind of
  appearance objects.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractFeatureWithLifespan
abstract: true
attributes:
  adeOfAbstractAppearance:
    name: adeOfAbstractAppearance
    description: Augments AbstractAppearance with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractAppearance
    owner: AbstractAppearance
    domain_of:
    - AbstractAppearance
    range: ADEOfAbstractAppearance
    required: false
    multivalued: true
  creationDate:
    name: creationDate
    description: Indicates the date at which a CityGML feature was added to the CityModel.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: creationDate
    owner: AbstractAppearance
    domain_of:
    - AbstractFeatureWithLifespan
    range: datetime
    required: false
    multivalued: false
  terminationDate:
    name: terminationDate
    description: Indicates the date at which a CityGML feature was removed from the
      CityModel.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: terminationDate
    owner: AbstractAppearance
    domain_of:
    - AbstractFeatureWithLifespan
    range: datetime
    required: false
    multivalued: false
  validFrom:
    name: validFrom
    description: Indicates the date at which a CityGML feature started to exist in
      the real world.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: validFrom
    owner: AbstractAppearance
    domain_of:
    - AbstractFeatureWithLifespan
    range: datetime
    required: false
    multivalued: false
  validTo:
    name: validTo
    description: Indicates the date at which a CityGML feature ended to exist in the
      real world.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: validTo
    owner: AbstractAppearance
    domain_of:
    - AbstractFeatureWithLifespan
    range: datetime
    required: false
    multivalued: false
  adeOfAbstractFeatureWithLifespan:
    name: adeOfAbstractFeatureWithLifespan
    description: Augments AbstractFeatureWithLifespan with properties defined in an
      ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractFeatureWithLifespan
    owner: AbstractAppearance
    domain_of:
    - AbstractFeatureWithLifespan
    range: ADEOfAbstractFeatureWithLifespan
    required: false
    multivalued: true
  featureID:
    name: featureID
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: featureID
    owner: AbstractAppearance
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
    owner: AbstractAppearance
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: AbstractAppearance
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
    owner: AbstractAppearance
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
    owner: AbstractAppearance
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>