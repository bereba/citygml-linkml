

# Class: AbstractCityObject 


_AbstractCityObject is the abstract superclass of all thematic classes within the CityGML Conceptual Model._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [citygml:AbstractCityObject](https://www.ogc.org/standards/citygml/AbstractCityObject)





```mermaid
 classDiagram
    class AbstractCityObject
    click AbstractCityObject href "../AbstractCityObject/"
      AbstractFeatureWithLifespan <|-- AbstractCityObject
        click AbstractFeatureWithLifespan href "../AbstractFeatureWithLifespan/"
      

      AbstractCityObject <|-- AbstractSpace
        click AbstractSpace href "../AbstractSpace/"
      AbstractCityObject <|-- AbstractSpaceBoundary
        click AbstractSpaceBoundary href "../AbstractSpaceBoundary/"
      

      AbstractCityObject : adeOfAbstractCityObject
        
          
    
        
        
        AbstractCityObject --> "*" ADEOfAbstractCityObject : adeOfAbstractCityObject
        click ADEOfAbstractCityObject href "../ADEOfAbstractCityObject/"
    

        
      AbstractCityObject : adeOfAbstractFeature
        
          
    
        
        
        AbstractCityObject --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      AbstractCityObject : adeOfAbstractFeatureWithLifespan
        
          
    
        
        
        AbstractCityObject --> "*" ADEOfAbstractFeatureWithLifespan : adeOfAbstractFeatureWithLifespan
        click ADEOfAbstractFeatureWithLifespan href "../ADEOfAbstractFeatureWithLifespan/"
    

        
      AbstractCityObject : appearance
        
          
    
        
        
        AbstractCityObject --> "*" AbstractAppearance : appearance
        click AbstractAppearance href "../AbstractAppearance/"
    

        
      AbstractCityObject : creationDate
        
      AbstractCityObject : description
        
      AbstractCityObject : dynamizer
        
          
    
        
        
        AbstractCityObject --> "*" AbstractDynamizer : dynamizer
        click AbstractDynamizer href "../AbstractDynamizer/"
    

        
      AbstractCityObject : externalReference
        
          
    
        
        
        AbstractCityObject --> "*" ExternalReference : externalReference
        click ExternalReference href "../ExternalReference/"
    

        
      AbstractCityObject : featureID
        
          
    
        
        
        AbstractCityObject --> "1" ID : featureID
        click ID href "../ID/"
    

        
      AbstractCityObject : generalizesTo
        
          
    
        
        
        AbstractCityObject --> "*" AbstractCityObject : generalizesTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      AbstractCityObject : genericAttribute
        
          
    
        
        
        AbstractCityObject --> "*" AbstractGenericAttribute : genericAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
    

        
      AbstractCityObject : identifier
        
      AbstractCityObject : name
        
      AbstractCityObject : relatedTo
        
          
    
        
        
        AbstractCityObject --> "*" AbstractCityObject : relatedTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      AbstractCityObject : relativeToTerrain
        
          
    
        
        
        AbstractCityObject --> "0..1" RelativeToTerrain : relativeToTerrain
        click RelativeToTerrain href "../RelativeToTerrain/"
    

        
      AbstractCityObject : relativeToWater
        
          
    
        
        
        AbstractCityObject --> "0..1" RelativeToWater : relativeToWater
        click RelativeToWater href "../RelativeToWater/"
    

        
      AbstractCityObject : terminationDate
        
      AbstractCityObject : validFrom
        
      AbstractCityObject : validTo
        
      
```





## Inheritance
* [AbstractFeature](AbstractFeature.md)
    * [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md)
        * **AbstractCityObject**
            * [AbstractSpace](AbstractSpace.md)
            * [AbstractSpaceBoundary](AbstractSpaceBoundary.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [relativeToTerrain](relativeToTerrain.md) | 0..1 <br/> [RelativeToTerrain](RelativeToTerrain.md) | Describes the vertical position of the city object relative to the surroundin... | direct |
| [relativeToWater](relativeToWater.md) | 0..1 <br/> [RelativeToWater](RelativeToWater.md) | Describes the vertical position of the city object relative to the surroundin... | direct |
| [adeOfAbstractCityObject](adeOfAbstractCityObject.md) | * <br/> [ADEOfAbstractCityObject](ADEOfAbstractCityObject.md) | Augments AbstractCityObject with properties defined in an ADE | direct |
| [appearance](appearance.md) | * <br/> [AbstractAppearance](AbstractAppearance.md) | Relates appearances to the city object | direct |
| [genericAttribute](genericAttribute.md) | * <br/> [AbstractGenericAttribute](AbstractGenericAttribute.md) | Relates generic attributes to the city object | direct |
| [generalizesTo](generalizesTo.md) | * <br/> [AbstractCityObject](AbstractCityObject.md) | Relates generalized representations of the same real-world object in differen... | direct |
| [externalReference](externalReference.md) | * <br/> [ExternalReference](ExternalReference.md) | References external objects in other information systems that have a relation... | direct |
| [relatedTo](relatedTo.md) | * <br/> [AbstractCityObject](AbstractCityObject.md) |  | direct |
| [dynamizer](dynamizer.md) | * <br/> [AbstractDynamizer](AbstractDynamizer.md) | Relates Dynamizer objects to the city object | direct |
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
| [SensorConnection](SensorConnection.md) | [sensorLocation](sensorLocation.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [CityModelMember](CityModelMember.md) | [cityObjectMember](cityObjectMember.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractConstruction](AbstractConstruction.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractConstruction](AbstractConstruction.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractConstructionSurface](AbstractConstructionSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractConstructionSurface](AbstractConstructionSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractConstructiveElement](AbstractConstructiveElement.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractConstructiveElement](AbstractConstructiveElement.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractFillingElement](AbstractFillingElement.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractFillingElement](AbstractFillingElement.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractFillingSurface](AbstractFillingSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractFillingSurface](AbstractFillingSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractFurniture](AbstractFurniture.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractFurniture](AbstractFurniture.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractInstallation](AbstractInstallation.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractInstallation](AbstractInstallation.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [CeilingSurface](CeilingSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [CeilingSurface](CeilingSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Door](Door.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Door](Door.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [DoorSurface](DoorSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [DoorSurface](DoorSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [FloorSurface](FloorSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [FloorSurface](FloorSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [GroundSurface](GroundSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [GroundSurface](GroundSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [InteriorWallSurface](InteriorWallSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [InteriorWallSurface](InteriorWallSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [OtherConstruction](OtherConstruction.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [OtherConstruction](OtherConstruction.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [OuterCeilingSurface](OuterCeilingSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [OuterCeilingSurface](OuterCeilingSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [OuterFloorSurface](OuterFloorSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [OuterFloorSurface](OuterFloorSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [RoofSurface](RoofSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [RoofSurface](RoofSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [WallSurface](WallSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [WallSurface](WallSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Window](Window.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Window](Window.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [WindowSurface](WindowSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [WindowSurface](WindowSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractBridge](AbstractBridge.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractBridge](AbstractBridge.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Bridge](Bridge.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Bridge](Bridge.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BridgeConstructiveElement](BridgeConstructiveElement.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BridgeConstructiveElement](BridgeConstructiveElement.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BridgeFurniture](BridgeFurniture.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BridgeFurniture](BridgeFurniture.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BridgeInstallation](BridgeInstallation.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BridgeInstallation](BridgeInstallation.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BridgePart](BridgePart.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BridgePart](BridgePart.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BridgeRoom](BridgeRoom.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BridgeRoom](BridgeRoom.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractBuilding](AbstractBuilding.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractBuilding](AbstractBuilding.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Building](Building.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Building](Building.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BuildingConstructiveElement](BuildingConstructiveElement.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BuildingConstructiveElement](BuildingConstructiveElement.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BuildingFurniture](BuildingFurniture.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BuildingFurniture](BuildingFurniture.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BuildingInstallation](BuildingInstallation.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BuildingInstallation](BuildingInstallation.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BuildingPart](BuildingPart.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BuildingPart](BuildingPart.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BuildingRoom](BuildingRoom.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BuildingRoom](BuildingRoom.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BuildingUnit](BuildingUnit.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BuildingUnit](BuildingUnit.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Storey](Storey.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Storey](Storey.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [CityFurniture](CityFurniture.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [CityFurniture](CityFurniture.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [CityObjectGroup](CityObjectGroup.md) | [parent](parent.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [CityObjectGroup](CityObjectGroup.md) | [groupMember](groupMember.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [CityObjectGroup](CityObjectGroup.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [CityObjectGroup](CityObjectGroup.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractCityObject](AbstractCityObject.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractCityObject](AbstractCityObject.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractLogicalSpace](AbstractLogicalSpace.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractLogicalSpace](AbstractLogicalSpace.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractOccupiedSpace](AbstractOccupiedSpace.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractOccupiedSpace](AbstractOccupiedSpace.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractPhysicalSpace](AbstractPhysicalSpace.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractPhysicalSpace](AbstractPhysicalSpace.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractSpace](AbstractSpace.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractSpace](AbstractSpace.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractSpaceBoundary](AbstractSpaceBoundary.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractSpaceBoundary](AbstractSpaceBoundary.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractThematicSurface](AbstractThematicSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractThematicSurface](AbstractThematicSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractUnoccupiedSpace](AbstractUnoccupiedSpace.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractUnoccupiedSpace](AbstractUnoccupiedSpace.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [ClosureSurface](ClosureSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [ClosureSurface](ClosureSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [GenericLogicalSpace](GenericLogicalSpace.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [GenericLogicalSpace](GenericLogicalSpace.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [GenericOccupiedSpace](GenericOccupiedSpace.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [GenericOccupiedSpace](GenericOccupiedSpace.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [GenericThematicSurface](GenericThematicSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [GenericThematicSurface](GenericThematicSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [GenericUnoccupiedSpace](GenericUnoccupiedSpace.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [GenericUnoccupiedSpace](GenericUnoccupiedSpace.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [LandUse](LandUse.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [LandUse](LandUse.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractReliefComponent](AbstractReliefComponent.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractReliefComponent](AbstractReliefComponent.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BreaklineRelief](BreaklineRelief.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [BreaklineRelief](BreaklineRelief.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [MassPointRelief](MassPointRelief.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [MassPointRelief](MassPointRelief.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [RasterRelief](RasterRelief.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [RasterRelief](RasterRelief.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [ReliefFeature](ReliefFeature.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [ReliefFeature](ReliefFeature.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [TINRelief](TINRelief.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [TINRelief](TINRelief.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractTransportationSpace](AbstractTransportationSpace.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractTransportationSpace](AbstractTransportationSpace.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AuxiliaryTrafficArea](AuxiliaryTrafficArea.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AuxiliaryTrafficArea](AuxiliaryTrafficArea.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AuxiliaryTrafficSpace](AuxiliaryTrafficSpace.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AuxiliaryTrafficSpace](AuxiliaryTrafficSpace.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [ClearanceSpace](ClearanceSpace.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [ClearanceSpace](ClearanceSpace.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Hole](Hole.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Hole](Hole.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [HoleSurface](HoleSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [HoleSurface](HoleSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Intersection](Intersection.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Intersection](Intersection.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Marking](Marking.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Marking](Marking.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Railway](Railway.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Railway](Railway.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Road](Road.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Road](Road.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Section](Section.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Section](Section.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Square](Square.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Square](Square.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Track](Track.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Track](Track.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [TrafficArea](TrafficArea.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [TrafficArea](TrafficArea.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [TrafficSpace](TrafficSpace.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [TrafficSpace](TrafficSpace.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Waterway](Waterway.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Waterway](Waterway.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractTunnel](AbstractTunnel.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractTunnel](AbstractTunnel.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [HollowSpace](HollowSpace.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [HollowSpace](HollowSpace.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Tunnel](Tunnel.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [Tunnel](Tunnel.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [TunnelConstructiveElement](TunnelConstructiveElement.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [TunnelConstructiveElement](TunnelConstructiveElement.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [TunnelFurniture](TunnelFurniture.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [TunnelFurniture](TunnelFurniture.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [TunnelInstallation](TunnelInstallation.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [TunnelInstallation](TunnelInstallation.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [TunnelPart](TunnelPart.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [TunnelPart](TunnelPart.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractVegetationObject](AbstractVegetationObject.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractVegetationObject](AbstractVegetationObject.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [PlantCover](PlantCover.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [PlantCover](PlantCover.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [SolitaryVegetationObject](SolitaryVegetationObject.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [SolitaryVegetationObject](SolitaryVegetationObject.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractWaterBoundarySurface](AbstractWaterBoundarySurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [AbstractWaterBoundarySurface](AbstractWaterBoundarySurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [WaterBody](WaterBody.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [WaterBody](WaterBody.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [WaterGroundSurface](WaterGroundSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [WaterGroundSurface](WaterGroundSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [WaterSurface](WaterSurface.md) | [generalizesTo](generalizesTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |
| [WaterSurface](WaterSurface.md) | [relatedTo](relatedTo.md) | range | [AbstractCityObject](AbstractCityObject.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:AbstractCityObject |
| native | citygml:AbstractCityObject |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AbstractCityObject
description: AbstractCityObject is the abstract superclass of all thematic classes
  within the CityGML Conceptual Model.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractFeatureWithLifespan
abstract: true
attributes:
  relativeToTerrain:
    name: relativeToTerrain
    description: Describes the vertical position of the city object relative to the
      surrounding terrain.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractCityObject
    range: RelativeToTerrain
    required: false
    multivalued: false
  relativeToWater:
    name: relativeToWater
    description: Describes the vertical position of the city object relative to the
      surrounding water surface.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractCityObject
    range: RelativeToWater
    required: false
    multivalued: false
  adeOfAbstractCityObject:
    name: adeOfAbstractCityObject
    description: Augments AbstractCityObject with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractCityObject
    range: ADEOfAbstractCityObject
    required: false
    multivalued: true
  appearance:
    name: appearance
    description: Relates appearances to the city object.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractCityObject
    - ImplicitGeometry
    range: AbstractAppearance
    required: false
    multivalued: true
  genericAttribute:
    name: genericAttribute
    description: Relates generic attributes to the city object.
    from_schema: https://www.ogc.org/standards/citygml
    domain_of:
    - GenericAttributeSet
    - AbstractCityObject
    range: AbstractGenericAttribute
    required: false
    multivalued: true
  generalizesTo:
    name: generalizesTo
    description: Relates generalized representations of the same real-world object
      in different Levels of Detail to the city object. The direction of this relation
      is from the city object to the corresponding generalized city objects.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractCityObject
    range: AbstractCityObject
    required: false
    multivalued: true
  externalReference:
    name: externalReference
    description: References external objects in other information systems that have
      a relation to the city object.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractCityObject
    range: ExternalReference
    required: false
    multivalued: true
  relatedTo:
    name: relatedTo
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractCityObject
    range: AbstractCityObject
    required: false
    multivalued: true
  dynamizer:
    name: dynamizer
    description: Relates Dynamizer objects to the city object. These allow timeseries
      data to override static attribute values of the city object.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractCityObject
    range: AbstractDynamizer
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: AbstractCityObject
description: AbstractCityObject is the abstract superclass of all thematic classes
  within the CityGML Conceptual Model.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractFeatureWithLifespan
abstract: true
attributes:
  relativeToTerrain:
    name: relativeToTerrain
    description: Describes the vertical position of the city object relative to the
      surrounding terrain.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: relativeToTerrain
    owner: AbstractCityObject
    domain_of:
    - AbstractCityObject
    range: RelativeToTerrain
    required: false
    multivalued: false
  relativeToWater:
    name: relativeToWater
    description: Describes the vertical position of the city object relative to the
      surrounding water surface.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: relativeToWater
    owner: AbstractCityObject
    domain_of:
    - AbstractCityObject
    range: RelativeToWater
    required: false
    multivalued: false
  adeOfAbstractCityObject:
    name: adeOfAbstractCityObject
    description: Augments AbstractCityObject with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractCityObject
    owner: AbstractCityObject
    domain_of:
    - AbstractCityObject
    range: ADEOfAbstractCityObject
    required: false
    multivalued: true
  appearance:
    name: appearance
    description: Relates appearances to the city object.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: appearance
    owner: AbstractCityObject
    domain_of:
    - AbstractCityObject
    - ImplicitGeometry
    range: AbstractAppearance
    required: false
    multivalued: true
  genericAttribute:
    name: genericAttribute
    description: Relates generic attributes to the city object.
    from_schema: https://www.ogc.org/standards/citygml
    alias: genericAttribute
    owner: AbstractCityObject
    domain_of:
    - GenericAttributeSet
    - AbstractCityObject
    range: AbstractGenericAttribute
    required: false
    multivalued: true
  generalizesTo:
    name: generalizesTo
    description: Relates generalized representations of the same real-world object
      in different Levels of Detail to the city object. The direction of this relation
      is from the city object to the corresponding generalized city objects.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: generalizesTo
    owner: AbstractCityObject
    domain_of:
    - AbstractCityObject
    range: AbstractCityObject
    required: false
    multivalued: true
  externalReference:
    name: externalReference
    description: References external objects in other information systems that have
      a relation to the city object.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: externalReference
    owner: AbstractCityObject
    domain_of:
    - AbstractCityObject
    range: ExternalReference
    required: false
    multivalued: true
  relatedTo:
    name: relatedTo
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: relatedTo
    owner: AbstractCityObject
    domain_of:
    - AbstractCityObject
    range: AbstractCityObject
    required: false
    multivalued: true
  dynamizer:
    name: dynamizer
    description: Relates Dynamizer objects to the city object. These allow timeseries
      data to override static attribute values of the city object.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: dynamizer
    owner: AbstractCityObject
    domain_of:
    - AbstractCityObject
    range: AbstractDynamizer
    required: false
    multivalued: true
  creationDate:
    name: creationDate
    description: Indicates the date at which a CityGML feature was added to the CityModel.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: creationDate
    owner: AbstractCityObject
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
    owner: AbstractCityObject
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
    owner: AbstractCityObject
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
    owner: AbstractCityObject
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
    owner: AbstractCityObject
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
    owner: AbstractCityObject
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
    owner: AbstractCityObject
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: AbstractCityObject
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
    owner: AbstractCityObject
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
    owner: AbstractCityObject
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>