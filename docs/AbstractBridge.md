

# Class: AbstractBridge 


_AbstractBridge is an abstract superclass representing the common attributes and associations of the classes Bridge and BridgePart._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [citygml:AbstractBridge](https://www.ogc.org/standards/citygml/AbstractBridge)





```mermaid
 classDiagram
    class AbstractBridge
    click AbstractBridge href "../AbstractBridge/"
      AbstractConstruction <|-- AbstractBridge
        click AbstractConstruction href "../AbstractConstruction/"
      

      AbstractBridge <|-- Bridge
        click Bridge href "../Bridge/"
      AbstractBridge <|-- BridgePart
        click BridgePart href "../BridgePart/"
      

      AbstractBridge : address
        
          
    
        
        
        AbstractBridge --> "*" Address : address
        click Address href "../Address/"
    

        
      AbstractBridge : adeOfAbstractBridge
        
          
    
        
        
        AbstractBridge --> "*" ADEOfAbstractBridge : adeOfAbstractBridge
        click ADEOfAbstractBridge href "../ADEOfAbstractBridge/"
    

        
      AbstractBridge : adeOfAbstractCityObject
        
          
    
        
        
        AbstractBridge --> "*" ADEOfAbstractCityObject : adeOfAbstractCityObject
        click ADEOfAbstractCityObject href "../ADEOfAbstractCityObject/"
    

        
      AbstractBridge : adeOfAbstractConstruction
        
          
    
        
        
        AbstractBridge --> "*" ADEOfAbstractConstruction : adeOfAbstractConstruction
        click ADEOfAbstractConstruction href "../ADEOfAbstractConstruction/"
    

        
      AbstractBridge : adeOfAbstractFeature
        
          
    
        
        
        AbstractBridge --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      AbstractBridge : adeOfAbstractFeatureWithLifespan
        
          
    
        
        
        AbstractBridge --> "*" ADEOfAbstractFeatureWithLifespan : adeOfAbstractFeatureWithLifespan
        click ADEOfAbstractFeatureWithLifespan href "../ADEOfAbstractFeatureWithLifespan/"
    

        
      AbstractBridge : adeOfAbstractOccupiedSpace
        
          
    
        
        
        AbstractBridge --> "*" ADEOfAbstractOccupiedSpace : adeOfAbstractOccupiedSpace
        click ADEOfAbstractOccupiedSpace href "../ADEOfAbstractOccupiedSpace/"
    

        
      AbstractBridge : adeOfAbstractPhysicalSpace
        
          
    
        
        
        AbstractBridge --> "*" ADEOfAbstractPhysicalSpace : adeOfAbstractPhysicalSpace
        click ADEOfAbstractPhysicalSpace href "../ADEOfAbstractPhysicalSpace/"
    

        
      AbstractBridge : adeOfAbstractSpace
        
          
    
        
        
        AbstractBridge --> "*" ADEOfAbstractSpace : adeOfAbstractSpace
        click ADEOfAbstractSpace href "../ADEOfAbstractSpace/"
    

        
      AbstractBridge : appearance
        
          
    
        
        
        AbstractBridge --> "*" AbstractAppearance : appearance
        click AbstractAppearance href "../AbstractAppearance/"
    

        
      AbstractBridge : area
        
          
    
        
        
        AbstractBridge --> "*" QualifiedArea : area
        click QualifiedArea href "../QualifiedArea/"
    

        
      AbstractBridge : boundary
        
          
    
        
        
        AbstractBridge --> "*" AbstractThematicSurface : boundary
        click AbstractThematicSurface href "../AbstractThematicSurface/"
    

        
      AbstractBridge : bridgeConstructiveElement
        
          
    
        
        
        AbstractBridge --> "*" BridgeConstructiveElement : bridgeConstructiveElement
        click BridgeConstructiveElement href "../BridgeConstructiveElement/"
    

        
      AbstractBridge : bridgeFurniture
        
          
    
        
        
        AbstractBridge --> "*" BridgeFurniture : bridgeFurniture
        click BridgeFurniture href "../BridgeFurniture/"
    

        
      AbstractBridge : bridgeInstallation
        
          
    
        
        
        AbstractBridge --> "*" BridgeInstallation : bridgeInstallation
        click BridgeInstallation href "../BridgeInstallation/"
    

        
      AbstractBridge : bridgeRoom
        
          
    
        
        
        AbstractBridge --> "*" BridgeRoom : bridgeRoom
        click BridgeRoom href "../BridgeRoom/"
    

        
      AbstractBridge : class
        
          
    
        
        
        AbstractBridge --> "0..1" BridgeClassValue : class
        click BridgeClassValue href "../BridgeClassValue/"
    

        
      AbstractBridge : conditionOfConstruction
        
          
    
        
        
        AbstractBridge --> "0..1" ConditionOfConstructionValue : conditionOfConstruction
        click ConditionOfConstructionValue href "../ConditionOfConstructionValue/"
    

        
      AbstractBridge : constructionEvent
        
          
    
        
        
        AbstractBridge --> "*" ConstructionEvent : constructionEvent
        click ConstructionEvent href "../ConstructionEvent/"
    

        
      AbstractBridge : creationDate
        
      AbstractBridge : dateOfConstruction
        
      AbstractBridge : dateOfDemolition
        
      AbstractBridge : description
        
      AbstractBridge : dynamizer
        
          
    
        
        
        AbstractBridge --> "*" AbstractDynamizer : dynamizer
        click AbstractDynamizer href "../AbstractDynamizer/"
    

        
      AbstractBridge : elevation
        
          
    
        
        
        AbstractBridge --> "*" Elevation : elevation
        click Elevation href "../Elevation/"
    

        
      AbstractBridge : externalReference
        
          
    
        
        
        AbstractBridge --> "*" ExternalReference : externalReference
        click ExternalReference href "../ExternalReference/"
    

        
      AbstractBridge : featureID
        
          
    
        
        
        AbstractBridge --> "1" ID : featureID
        click ID href "../ID/"
    

        
      AbstractBridge : function
        
          
    
        
        
        AbstractBridge --> "*" BridgeFunctionValue : function
        click BridgeFunctionValue href "../BridgeFunctionValue/"
    

        
      AbstractBridge : generalizesTo
        
          
    
        
        
        AbstractBridge --> "*" AbstractCityObject : generalizesTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      AbstractBridge : genericAttribute
        
          
    
        
        
        AbstractBridge --> "*" AbstractGenericAttribute : genericAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
    

        
      AbstractBridge : height
        
          
    
        
        
        AbstractBridge --> "*" Height : height
        click Height href "../Height/"
    

        
      AbstractBridge : identifier
        
      AbstractBridge : isMovable
        
      AbstractBridge : lod0MultiCurve
        
      AbstractBridge : lod0MultiSurface
        
      AbstractBridge : lod0Point
        
      AbstractBridge : lod1ImplicitRepresentation
        
          
    
        
        
        AbstractBridge --> "0..1" ImplicitGeometry : lod1ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      AbstractBridge : lod1Solid
        
      AbstractBridge : lod1TerrainIntersectionCurve
        
      AbstractBridge : lod2ImplicitRepresentation
        
          
    
        
        
        AbstractBridge --> "0..1" ImplicitGeometry : lod2ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      AbstractBridge : lod2MultiCurve
        
      AbstractBridge : lod2MultiSurface
        
      AbstractBridge : lod2Solid
        
      AbstractBridge : lod2TerrainIntersectionCurve
        
      AbstractBridge : lod3ImplicitRepresentation
        
          
    
        
        
        AbstractBridge --> "0..1" ImplicitGeometry : lod3ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      AbstractBridge : lod3MultiCurve
        
      AbstractBridge : lod3MultiSurface
        
      AbstractBridge : lod3Solid
        
      AbstractBridge : lod3TerrainIntersectionCurve
        
      AbstractBridge : name
        
      AbstractBridge : occupancy
        
          
    
        
        
        AbstractBridge --> "*" Occupancy : occupancy
        click Occupancy href "../Occupancy/"
    

        
      AbstractBridge : pointCloud
        
          
    
        
        
        AbstractBridge --> "0..1" AbstractPointCloud : pointCloud
        click AbstractPointCloud href "../AbstractPointCloud/"
    

        
      AbstractBridge : relatedTo
        
          
    
        
        
        AbstractBridge --> "*" AbstractCityObject : relatedTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      AbstractBridge : relativeToTerrain
        
          
    
        
        
        AbstractBridge --> "0..1" RelativeToTerrain : relativeToTerrain
        click RelativeToTerrain href "../RelativeToTerrain/"
    

        
      AbstractBridge : relativeToWater
        
          
    
        
        
        AbstractBridge --> "0..1" RelativeToWater : relativeToWater
        click RelativeToWater href "../RelativeToWater/"
    

        
      AbstractBridge : spaceType
        
          
    
        
        
        AbstractBridge --> "0..1" SpaceType : spaceType
        click SpaceType href "../SpaceType/"
    

        
      AbstractBridge : terminationDate
        
      AbstractBridge : usage
        
          
    
        
        
        AbstractBridge --> "*" BridgeUsageValue : usage
        click BridgeUsageValue href "../BridgeUsageValue/"
    

        
      AbstractBridge : validFrom
        
      AbstractBridge : validTo
        
      AbstractBridge : volume
        
          
    
        
        
        AbstractBridge --> "*" QualifiedVolume : volume
        click QualifiedVolume href "../QualifiedVolume/"
    

        
      
```





## Inheritance
* [AbstractFeature](AbstractFeature.md)
    * [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md)
        * [AbstractCityObject](AbstractCityObject.md)
            * [AbstractSpace](AbstractSpace.md)
                * [AbstractPhysicalSpace](AbstractPhysicalSpace.md)
                    * [AbstractOccupiedSpace](AbstractOccupiedSpace.md)
                        * [AbstractConstruction](AbstractConstruction.md)
                            * **AbstractBridge**
                                * [Bridge](Bridge.md)
                                * [BridgePart](BridgePart.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [class](class.md) | 0..1 <br/> [BridgeClassValue](BridgeClassValue.md) | Indicates the specific type of the Bridge or BridgePart | direct |
| [function](function.md) | * <br/> [BridgeFunctionValue](BridgeFunctionValue.md) | Specifies the intended purposes of the Bridge or BridgePart | direct |
| [usage](usage.md) | * <br/> [BridgeUsageValue](BridgeUsageValue.md) | Specifies the actual uses of the Bridge or BridgePart | direct |
| [isMovable](isMovable.md) | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the Bridge or BridgePart can be moved to allow for watercra... | direct |
| [adeOfAbstractBridge](adeOfAbstractBridge.md) | * <br/> [ADEOfAbstractBridge](ADEOfAbstractBridge.md) | Augments AbstractBridge with properties defined in an ADE | direct |
| [bridgeRoom](bridgeRoom.md) | * <br/> [BridgeRoom](BridgeRoom.md) | Relates the rooms to the Bridge or BridgePart | direct |
| [bridgeFurniture](bridgeFurniture.md) | * <br/> [BridgeFurniture](BridgeFurniture.md) | Relates the furniture objects to the Bridge or BridgePart | direct |
| [bridgeConstructiveElement](bridgeConstructiveElement.md) | * <br/> [BridgeConstructiveElement](BridgeConstructiveElement.md) | Relates the constructive elements to the Bridge or BridgePart | direct |
| [address](address.md) | * <br/> [Address](Address.md) | Relates the addresses to the Bridge or BridgePart | direct |
| [bridgeInstallation](bridgeInstallation.md) | * <br/> [BridgeInstallation](BridgeInstallation.md) | Relates the installation objects to the Bridge or BridgePart | direct |
| [conditionOfConstruction](conditionOfConstruction.md) | 0..1 <br/> [ConditionOfConstructionValue](ConditionOfConstructionValue.md) | Indicates the life-cycle status of the construction | [AbstractConstruction](AbstractConstruction.md) |
| [dateOfConstruction](dateOfConstruction.md) | 0..1 <br/> [Date](Date.md) | Indicates the date at which the construction was completed | [AbstractConstruction](AbstractConstruction.md) |
| [dateOfDemolition](dateOfDemolition.md) | 0..1 <br/> [Date](Date.md) | Indicates the date at which the construction was demolished | [AbstractConstruction](AbstractConstruction.md) |
| [constructionEvent](constructionEvent.md) | * <br/> [ConstructionEvent](ConstructionEvent.md) | Describes specific events in the life-time of the construction | [AbstractConstruction](AbstractConstruction.md) |
| [elevation](elevation.md) | * <br/> [Elevation](Elevation.md) | Specifies qualified elevations of the construction in relation to a well-defi... | [AbstractConstruction](AbstractConstruction.md) |
| [height](height.md) | * <br/> [Height](Height.md) | Specifies qualified heights of the construction above ground or below ground | [AbstractConstruction](AbstractConstruction.md) |
| [occupancy](occupancy.md) | * <br/> [Occupancy](Occupancy.md) | Provides qualified information on the residency of persons, animals, or other... | [AbstractConstruction](AbstractConstruction.md) |
| [adeOfAbstractConstruction](adeOfAbstractConstruction.md) | * <br/> [ADEOfAbstractConstruction](ADEOfAbstractConstruction.md) | Augments AbstractConstruction with properties defined in an ADE | [AbstractConstruction](AbstractConstruction.md) |
| [boundary](boundary.md) | * <br/> [AbstractThematicSurface](AbstractThematicSurface.md) |  | [AbstractSpace](AbstractSpace.md), [AbstractConstruction](AbstractConstruction.md) |
| [adeOfAbstractOccupiedSpace](adeOfAbstractOccupiedSpace.md) | * <br/> [ADEOfAbstractOccupiedSpace](ADEOfAbstractOccupiedSpace.md) | Augments AbstractOccupiedSpace with properties defined in an ADE | [AbstractOccupiedSpace](AbstractOccupiedSpace.md) |
| [lod3ImplicitRepresentation](lod3ImplicitRepresentation.md) | 0..1 <br/> [ImplicitGeometry](ImplicitGeometry.md) | Relates to an implicit geometry that represents the occupied space in Level o... | [AbstractOccupiedSpace](AbstractOccupiedSpace.md) |
| [lod2ImplicitRepresentation](lod2ImplicitRepresentation.md) | 0..1 <br/> [ImplicitGeometry](ImplicitGeometry.md) | Relates to an implicit geometry that represents the occupied space in Level o... | [AbstractOccupiedSpace](AbstractOccupiedSpace.md) |
| [lod1ImplicitRepresentation](lod1ImplicitRepresentation.md) | 0..1 <br/> [ImplicitGeometry](ImplicitGeometry.md) | Relates to an implicit geometry that represents the occupied space in Level o... | [AbstractOccupiedSpace](AbstractOccupiedSpace.md) |
| [adeOfAbstractPhysicalSpace](adeOfAbstractPhysicalSpace.md) | * <br/> [ADEOfAbstractPhysicalSpace](ADEOfAbstractPhysicalSpace.md) | Augments AbstractPhysicalSpace with properties defined in an ADE | [AbstractPhysicalSpace](AbstractPhysicalSpace.md) |
| [lod3TerrainIntersectionCurve](lod3TerrainIntersectionCurve.md) | 0..1 <br/> [String](String.md) | Relates to a 3D MultiCurve geometry that represents the terrain intersection ... | [AbstractPhysicalSpace](AbstractPhysicalSpace.md) |
| [pointCloud](pointCloud.md) | 0..1 <br/> [AbstractPointCloud](AbstractPointCloud.md) | Relates to a 3D PointCloud that represents the physical space | [AbstractPhysicalSpace](AbstractPhysicalSpace.md) |
| [lod1TerrainIntersectionCurve](lod1TerrainIntersectionCurve.md) | 0..1 <br/> [String](String.md) | Relates to a 3D MultiCurve geometry that represents the terrain intersection ... | [AbstractPhysicalSpace](AbstractPhysicalSpace.md) |
| [lod2TerrainIntersectionCurve](lod2TerrainIntersectionCurve.md) | 0..1 <br/> [String](String.md) | Relates to a 3D MultiCurve geometry that represents the terrain intersection ... | [AbstractPhysicalSpace](AbstractPhysicalSpace.md) |
| [spaceType](spaceType.md) | 0..1 <br/> [SpaceType](SpaceType.md) | Specifies the degree of openness of a space | [AbstractSpace](AbstractSpace.md) |
| [volume](volume.md) | * <br/> [QualifiedVolume](QualifiedVolume.md) | Specifies qualified volumes related to the space | [AbstractSpace](AbstractSpace.md) |
| [area](area.md) | * <br/> [QualifiedArea](QualifiedArea.md) | Specifies qualified areas related to the space | [AbstractSpace](AbstractSpace.md) |
| [adeOfAbstractSpace](adeOfAbstractSpace.md) | * <br/> [ADEOfAbstractSpace](ADEOfAbstractSpace.md) | Augments AbstractSpace with properties defined in an ADE | [AbstractSpace](AbstractSpace.md) |
| [lod2MultiCurve](lod2MultiCurve.md) | 0..1 <br/> [String](String.md) | Relates to a 3D MultiCurve geometry that represents the space in Level of Det... | [AbstractSpace](AbstractSpace.md) |
| [lod3MultiSurface](lod3MultiSurface.md) | 0..1 <br/> [String](String.md) | Relates to a 3D MultiSurface geometry that represents the space in Level of D... | [AbstractSpace](AbstractSpace.md) |
| [lod0MultiSurface](lod0MultiSurface.md) | 0..1 <br/> [String](String.md) | Relates to a 3D MultiSurface geometry that represents the space in Level of D... | [AbstractSpace](AbstractSpace.md) |
| [lod1Solid](lod1Solid.md) | 0..1 <br/> [String](String.md) | Relates to a 3D Solid geometry that represents the space in Level of Detail 1 | [AbstractSpace](AbstractSpace.md) |
| [lod3Solid](lod3Solid.md) | 0..1 <br/> [String](String.md) | Relates to a 3D Solid geometry that represents the space in Level of Detail 3 | [AbstractSpace](AbstractSpace.md) |
| [lod0MultiCurve](lod0MultiCurve.md) | 0..1 <br/> [String](String.md) | Relates to a 3D MultiCurve geometry that represents the space in Level of Det... | [AbstractSpace](AbstractSpace.md) |
| [lod2Solid](lod2Solid.md) | 0..1 <br/> [String](String.md) | Relates to a 3D Solid geometry that represents the space in Level of Detail 2 | [AbstractSpace](AbstractSpace.md) |
| [lod0Point](lod0Point.md) | 0..1 <br/> [String](String.md) | Relates to a 3D Point geometry that represents the space in Level of Detail 0 | [AbstractSpace](AbstractSpace.md) |
| [lod3MultiCurve](lod3MultiCurve.md) | 0..1 <br/> [String](String.md) | Relates to a 3D MultiCurve geometry that represents the space in Level of Det... | [AbstractSpace](AbstractSpace.md) |
| [lod2MultiSurface](lod2MultiSurface.md) | 0..1 <br/> [String](String.md) | Relates to a 3D MultiSurface geometry that represents the space in Level of D... | [AbstractSpace](AbstractSpace.md) |
| [relativeToTerrain](relativeToTerrain.md) | 0..1 <br/> [RelativeToTerrain](RelativeToTerrain.md) | Describes the vertical position of the city object relative to the surroundin... | [AbstractCityObject](AbstractCityObject.md) |
| [relativeToWater](relativeToWater.md) | 0..1 <br/> [RelativeToWater](RelativeToWater.md) | Describes the vertical position of the city object relative to the surroundin... | [AbstractCityObject](AbstractCityObject.md) |
| [adeOfAbstractCityObject](adeOfAbstractCityObject.md) | * <br/> [ADEOfAbstractCityObject](ADEOfAbstractCityObject.md) | Augments AbstractCityObject with properties defined in an ADE | [AbstractCityObject](AbstractCityObject.md) |
| [appearance](appearance.md) | * <br/> [AbstractAppearance](AbstractAppearance.md) | Relates appearances to the city object | [AbstractCityObject](AbstractCityObject.md) |
| [genericAttribute](genericAttribute.md) | * <br/> [AbstractGenericAttribute](AbstractGenericAttribute.md) | Relates generic attributes to the city object | [AbstractCityObject](AbstractCityObject.md) |
| [generalizesTo](generalizesTo.md) | * <br/> [AbstractCityObject](AbstractCityObject.md) | Relates generalized representations of the same real-world object in differen... | [AbstractCityObject](AbstractCityObject.md) |
| [externalReference](externalReference.md) | * <br/> [ExternalReference](ExternalReference.md) | References external objects in other information systems that have a relation... | [AbstractCityObject](AbstractCityObject.md) |
| [relatedTo](relatedTo.md) | * <br/> [AbstractCityObject](AbstractCityObject.md) |  | [AbstractCityObject](AbstractCityObject.md) |
| [dynamizer](dynamizer.md) | * <br/> [AbstractDynamizer](AbstractDynamizer.md) | Relates Dynamizer objects to the city object | [AbstractCityObject](AbstractCityObject.md) |
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















## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:AbstractBridge |
| native | citygml:AbstractBridge |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AbstractBridge
description: AbstractBridge is an abstract superclass representing the common attributes
  and associations of the classes Bridge and BridgePart.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractConstruction
abstract: true
attributes:
  class:
    name: class
    description: Indicates the specific type of the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    domain_of:
    - Door
    - OtherConstruction
    - Window
    - AbstractBridge
    - BridgeConstructiveElement
    - BridgeFurniture
    - BridgeInstallation
    - BridgeRoom
    - AbstractBuilding
    - AbstractBuildingSubdivision
    - BuildingConstructiveElement
    - BuildingFurniture
    - BuildingInstallation
    - BuildingRoom
    - CityFurniture
    - CityObjectGroup
    - GenericLogicalSpace
    - GenericOccupiedSpace
    - GenericThematicSurface
    - GenericUnoccupiedSpace
    - LandUse
    - AuxiliaryTrafficArea
    - AuxiliaryTrafficSpace
    - ClearanceSpace
    - Hole
    - Intersection
    - Marking
    - Railway
    - Road
    - Section
    - Square
    - Track
    - TrafficArea
    - TrafficSpace
    - Waterway
    - AbstractTunnel
    - HollowSpace
    - TunnelConstructiveElement
    - TunnelFurniture
    - TunnelInstallation
    - PlantCover
    - SolitaryVegetationObject
    - WaterBody
    range: BridgeClassValue
    required: false
    multivalued: false
  function:
    name: function
    description: Specifies the intended purposes of the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    domain_of:
    - Door
    - OtherConstruction
    - Window
    - AbstractBridge
    - BridgeConstructiveElement
    - BridgeFurniture
    - BridgeInstallation
    - BridgeRoom
    - AbstractBuilding
    - AbstractBuildingSubdivision
    - BuildingConstructiveElement
    - BuildingFurniture
    - BuildingInstallation
    - BuildingRoom
    - CityFurniture
    - CityObjectGroup
    - GenericLogicalSpace
    - GenericOccupiedSpace
    - GenericThematicSurface
    - GenericUnoccupiedSpace
    - LandUse
    - AuxiliaryTrafficArea
    - AuxiliaryTrafficSpace
    - Railway
    - Road
    - Square
    - Track
    - TrafficArea
    - TrafficSpace
    - Waterway
    - AbstractTunnel
    - HollowSpace
    - TunnelConstructiveElement
    - TunnelFurniture
    - TunnelInstallation
    - PlantCover
    - SolitaryVegetationObject
    - WaterBody
    range: BridgeFunctionValue
    required: false
    multivalued: true
  usage:
    name: usage
    description: Specifies the actual uses of the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    domain_of:
    - Door
    - OtherConstruction
    - Window
    - AbstractBridge
    - BridgeConstructiveElement
    - BridgeFurniture
    - BridgeInstallation
    - BridgeRoom
    - AbstractBuilding
    - AbstractBuildingSubdivision
    - BuildingConstructiveElement
    - BuildingFurniture
    - BuildingInstallation
    - BuildingRoom
    - CityFurniture
    - CityObjectGroup
    - GenericLogicalSpace
    - GenericOccupiedSpace
    - GenericThematicSurface
    - GenericUnoccupiedSpace
    - LandUse
    - AuxiliaryTrafficArea
    - AuxiliaryTrafficSpace
    - Railway
    - Road
    - Square
    - Track
    - TrafficArea
    - TrafficSpace
    - Waterway
    - AbstractTunnel
    - HollowSpace
    - TunnelConstructiveElement
    - TunnelFurniture
    - TunnelInstallation
    - PlantCover
    - SolitaryVegetationObject
    - WaterBody
    range: BridgeUsageValue
    required: false
    multivalued: true
  isMovable:
    name: isMovable
    description: Indicates whether the Bridge or BridgePart can be moved to allow
      for watercraft to pass.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractBridge
    range: boolean
    required: false
    multivalued: false
  adeOfAbstractBridge:
    name: adeOfAbstractBridge
    description: Augments AbstractBridge with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractBridge
    range: ADEOfAbstractBridge
    required: false
    multivalued: true
  bridgeRoom:
    name: bridgeRoom
    description: Relates the rooms to the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractBridge
    range: BridgeRoom
    required: false
    multivalued: true
  bridgeFurniture:
    name: bridgeFurniture
    description: Relates the furniture objects to the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractBridge
    - BridgeRoom
    range: BridgeFurniture
    required: false
    multivalued: true
  bridgeConstructiveElement:
    name: bridgeConstructiveElement
    description: Relates the constructive elements to the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractBridge
    range: BridgeConstructiveElement
    required: false
    multivalued: true
  address:
    name: address
    description: Relates the addresses to the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    domain_of:
    - Door
    - DoorSurface
    - AbstractBridge
    - AbstractBuilding
    - BuildingUnit
    range: Address
    required: false
    multivalued: true
  bridgeInstallation:
    name: bridgeInstallation
    description: Relates the installation objects to the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractBridge
    - BridgeRoom
    range: BridgeInstallation
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: AbstractBridge
description: AbstractBridge is an abstract superclass representing the common attributes
  and associations of the classes Bridge and BridgePart.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractConstruction
abstract: true
attributes:
  class:
    name: class
    description: Indicates the specific type of the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    alias: class
    owner: AbstractBridge
    domain_of:
    - Door
    - OtherConstruction
    - Window
    - AbstractBridge
    - BridgeConstructiveElement
    - BridgeFurniture
    - BridgeInstallation
    - BridgeRoom
    - AbstractBuilding
    - AbstractBuildingSubdivision
    - BuildingConstructiveElement
    - BuildingFurniture
    - BuildingInstallation
    - BuildingRoom
    - CityFurniture
    - CityObjectGroup
    - GenericLogicalSpace
    - GenericOccupiedSpace
    - GenericThematicSurface
    - GenericUnoccupiedSpace
    - LandUse
    - AuxiliaryTrafficArea
    - AuxiliaryTrafficSpace
    - ClearanceSpace
    - Hole
    - Intersection
    - Marking
    - Railway
    - Road
    - Section
    - Square
    - Track
    - TrafficArea
    - TrafficSpace
    - Waterway
    - AbstractTunnel
    - HollowSpace
    - TunnelConstructiveElement
    - TunnelFurniture
    - TunnelInstallation
    - PlantCover
    - SolitaryVegetationObject
    - WaterBody
    range: BridgeClassValue
    required: false
    multivalued: false
  function:
    name: function
    description: Specifies the intended purposes of the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    alias: function
    owner: AbstractBridge
    domain_of:
    - Door
    - OtherConstruction
    - Window
    - AbstractBridge
    - BridgeConstructiveElement
    - BridgeFurniture
    - BridgeInstallation
    - BridgeRoom
    - AbstractBuilding
    - AbstractBuildingSubdivision
    - BuildingConstructiveElement
    - BuildingFurniture
    - BuildingInstallation
    - BuildingRoom
    - CityFurniture
    - CityObjectGroup
    - GenericLogicalSpace
    - GenericOccupiedSpace
    - GenericThematicSurface
    - GenericUnoccupiedSpace
    - LandUse
    - AuxiliaryTrafficArea
    - AuxiliaryTrafficSpace
    - Railway
    - Road
    - Square
    - Track
    - TrafficArea
    - TrafficSpace
    - Waterway
    - AbstractTunnel
    - HollowSpace
    - TunnelConstructiveElement
    - TunnelFurniture
    - TunnelInstallation
    - PlantCover
    - SolitaryVegetationObject
    - WaterBody
    range: BridgeFunctionValue
    required: false
    multivalued: true
  usage:
    name: usage
    description: Specifies the actual uses of the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    alias: usage
    owner: AbstractBridge
    domain_of:
    - Door
    - OtherConstruction
    - Window
    - AbstractBridge
    - BridgeConstructiveElement
    - BridgeFurniture
    - BridgeInstallation
    - BridgeRoom
    - AbstractBuilding
    - AbstractBuildingSubdivision
    - BuildingConstructiveElement
    - BuildingFurniture
    - BuildingInstallation
    - BuildingRoom
    - CityFurniture
    - CityObjectGroup
    - GenericLogicalSpace
    - GenericOccupiedSpace
    - GenericThematicSurface
    - GenericUnoccupiedSpace
    - LandUse
    - AuxiliaryTrafficArea
    - AuxiliaryTrafficSpace
    - Railway
    - Road
    - Square
    - Track
    - TrafficArea
    - TrafficSpace
    - Waterway
    - AbstractTunnel
    - HollowSpace
    - TunnelConstructiveElement
    - TunnelFurniture
    - TunnelInstallation
    - PlantCover
    - SolitaryVegetationObject
    - WaterBody
    range: BridgeUsageValue
    required: false
    multivalued: true
  isMovable:
    name: isMovable
    description: Indicates whether the Bridge or BridgePart can be moved to allow
      for watercraft to pass.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: isMovable
    owner: AbstractBridge
    domain_of:
    - AbstractBridge
    range: boolean
    required: false
    multivalued: false
  adeOfAbstractBridge:
    name: adeOfAbstractBridge
    description: Augments AbstractBridge with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractBridge
    owner: AbstractBridge
    domain_of:
    - AbstractBridge
    range: ADEOfAbstractBridge
    required: false
    multivalued: true
  bridgeRoom:
    name: bridgeRoom
    description: Relates the rooms to the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: bridgeRoom
    owner: AbstractBridge
    domain_of:
    - AbstractBridge
    range: BridgeRoom
    required: false
    multivalued: true
  bridgeFurniture:
    name: bridgeFurniture
    description: Relates the furniture objects to the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: bridgeFurniture
    owner: AbstractBridge
    domain_of:
    - AbstractBridge
    - BridgeRoom
    range: BridgeFurniture
    required: false
    multivalued: true
  bridgeConstructiveElement:
    name: bridgeConstructiveElement
    description: Relates the constructive elements to the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: bridgeConstructiveElement
    owner: AbstractBridge
    domain_of:
    - AbstractBridge
    range: BridgeConstructiveElement
    required: false
    multivalued: true
  address:
    name: address
    description: Relates the addresses to the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    alias: address
    owner: AbstractBridge
    domain_of:
    - Door
    - DoorSurface
    - AbstractBridge
    - AbstractBuilding
    - BuildingUnit
    range: Address
    required: false
    multivalued: true
  bridgeInstallation:
    name: bridgeInstallation
    description: Relates the installation objects to the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: bridgeInstallation
    owner: AbstractBridge
    domain_of:
    - AbstractBridge
    - BridgeRoom
    range: BridgeInstallation
    required: false
    multivalued: true
  conditionOfConstruction:
    name: conditionOfConstruction
    description: Indicates the life-cycle status of the construction. [cf. INSPIRE]
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: conditionOfConstruction
    owner: AbstractBridge
    domain_of:
    - AbstractConstruction
    range: ConditionOfConstructionValue
    required: false
    multivalued: false
  dateOfConstruction:
    name: dateOfConstruction
    description: Indicates the date at which the construction was completed.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: dateOfConstruction
    owner: AbstractBridge
    domain_of:
    - AbstractConstruction
    range: date
    required: false
    multivalued: false
  dateOfDemolition:
    name: dateOfDemolition
    description: Indicates the date at which the construction was demolished.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: dateOfDemolition
    owner: AbstractBridge
    domain_of:
    - AbstractConstruction
    range: date
    required: false
    multivalued: false
  constructionEvent:
    name: constructionEvent
    description: Describes specific events in the life-time of the construction.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: constructionEvent
    owner: AbstractBridge
    domain_of:
    - AbstractConstruction
    range: ConstructionEvent
    required: false
    multivalued: true
  elevation:
    name: elevation
    description: Specifies qualified elevations of the construction in relation to
      a well-defined surface which is commonly taken as origin (e.g., geoid or water
      level). [cf. INSPIRE]
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: elevation
    owner: AbstractBridge
    domain_of:
    - AbstractConstruction
    - AbstractBuildingSubdivision
    range: Elevation
    required: false
    multivalued: true
  height:
    name: height
    description: Specifies qualified heights of the construction above ground or below
      ground. [cf. INSPIRE]
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: height
    owner: AbstractBridge
    domain_of:
    - AbstractConstruction
    - SolitaryVegetationObject
    range: Height
    required: false
    multivalued: true
  occupancy:
    name: occupancy
    description: Provides qualified information on the residency of persons, animals,
      or other moveable objects in the construction.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: occupancy
    owner: AbstractBridge
    domain_of:
    - AbstractConstruction
    - AbstractTransportationSpace
    - TrafficSpace
    range: Occupancy
    required: false
    multivalued: true
  adeOfAbstractConstruction:
    name: adeOfAbstractConstruction
    description: Augments AbstractConstruction with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractConstruction
    owner: AbstractBridge
    domain_of:
    - AbstractConstruction
    range: ADEOfAbstractConstruction
    required: false
    multivalued: true
  boundary:
    name: boundary
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: boundary
    owner: AbstractBridge
    domain_of:
    - AbstractConstruction
    - AbstractConstructiveElement
    - AbstractInstallation
    - Door
    - Window
    - BridgeRoom
    - BuildingRoom
    - Storey
    - AbstractSpace
    - AuxiliaryTrafficSpace
    - Hole
    - TrafficSpace
    - HollowSpace
    - WaterBody
    range: AbstractThematicSurface
    required: false
    multivalued: true
  adeOfAbstractOccupiedSpace:
    name: adeOfAbstractOccupiedSpace
    description: Augments AbstractOccupiedSpace with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractOccupiedSpace
    owner: AbstractBridge
    domain_of:
    - AbstractOccupiedSpace
    range: ADEOfAbstractOccupiedSpace
    required: false
    multivalued: true
  lod3ImplicitRepresentation:
    name: lod3ImplicitRepresentation
    description: Relates to an implicit geometry that represents the occupied space
      in Level of Detail 3.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod3ImplicitRepresentation
    owner: AbstractBridge
    domain_of:
    - AbstractOccupiedSpace
    range: ImplicitGeometry
    required: false
    multivalued: false
  lod2ImplicitRepresentation:
    name: lod2ImplicitRepresentation
    description: Relates to an implicit geometry that represents the occupied space
      in Level of Detail 2.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod2ImplicitRepresentation
    owner: AbstractBridge
    domain_of:
    - AbstractOccupiedSpace
    range: ImplicitGeometry
    required: false
    multivalued: false
  lod1ImplicitRepresentation:
    name: lod1ImplicitRepresentation
    description: Relates to an implicit geometry that represents the occupied space
      in Level of Detail 1.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod1ImplicitRepresentation
    owner: AbstractBridge
    domain_of:
    - AbstractOccupiedSpace
    range: ImplicitGeometry
    required: false
    multivalued: false
  adeOfAbstractPhysicalSpace:
    name: adeOfAbstractPhysicalSpace
    description: Augments AbstractPhysicalSpace with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractPhysicalSpace
    owner: AbstractBridge
    domain_of:
    - AbstractPhysicalSpace
    range: ADEOfAbstractPhysicalSpace
    required: false
    multivalued: true
  lod3TerrainIntersectionCurve:
    name: lod3TerrainIntersectionCurve
    description: Relates to a 3D MultiCurve geometry that represents the terrain intersection
      curve of the physical space in Level of Detail 3.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod3TerrainIntersectionCurve
    owner: AbstractBridge
    domain_of:
    - AbstractPhysicalSpace
    range: string
    required: false
    multivalued: false
  pointCloud:
    name: pointCloud
    description: Relates to a 3D PointCloud that represents the physical space.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: pointCloud
    owner: AbstractBridge
    domain_of:
    - AbstractPhysicalSpace
    - AbstractThematicSurface
    - MassPointRelief
    range: AbstractPointCloud
    required: false
    multivalued: false
  lod1TerrainIntersectionCurve:
    name: lod1TerrainIntersectionCurve
    description: Relates to a 3D MultiCurve geometry that represents the terrain intersection
      curve of the physical space in Level of Detail 1.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod1TerrainIntersectionCurve
    owner: AbstractBridge
    domain_of:
    - AbstractPhysicalSpace
    range: string
    required: false
    multivalued: false
  lod2TerrainIntersectionCurve:
    name: lod2TerrainIntersectionCurve
    description: Relates to a 3D MultiCurve geometry that represents the terrain intersection
      curve of the physical space in Level of Detail 2.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod2TerrainIntersectionCurve
    owner: AbstractBridge
    domain_of:
    - AbstractPhysicalSpace
    range: string
    required: false
    multivalued: false
  spaceType:
    name: spaceType
    description: Specifies the degree of openness of a space.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: spaceType
    owner: AbstractBridge
    domain_of:
    - AbstractSpace
    range: SpaceType
    required: false
    multivalued: false
  volume:
    name: volume
    description: Specifies qualified volumes related to the space.
    from_schema: https://www.ogc.org/standards/citygml
    alias: volume
    owner: AbstractBridge
    domain_of:
    - QualifiedVolume
    - AbstractSpace
    range: QualifiedVolume
    required: false
    multivalued: true
  area:
    name: area
    description: Specifies qualified areas related to the space.
    from_schema: https://www.ogc.org/standards/citygml
    alias: area
    owner: AbstractBridge
    domain_of:
    - QualifiedArea
    - AbstractSpace
    - AbstractThematicSurface
    range: QualifiedArea
    required: false
    multivalued: true
  adeOfAbstractSpace:
    name: adeOfAbstractSpace
    description: Augments AbstractSpace with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractSpace
    owner: AbstractBridge
    domain_of:
    - AbstractSpace
    range: ADEOfAbstractSpace
    required: false
    multivalued: true
  lod2MultiCurve:
    name: lod2MultiCurve
    description: Relates to a 3D MultiCurve geometry that represents the space in
      Level of Detail 2.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod2MultiCurve
    owner: AbstractBridge
    domain_of:
    - AbstractSpace
    range: string
    required: false
    multivalued: false
  lod3MultiSurface:
    name: lod3MultiSurface
    description: Relates to a 3D MultiSurface geometry that represents the space in
      Level of Detail 3.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod3MultiSurface
    owner: AbstractBridge
    domain_of:
    - AbstractSpace
    - AbstractThematicSurface
    range: string
    required: false
    multivalued: false
  lod0MultiSurface:
    name: lod0MultiSurface
    description: Relates to a 3D MultiSurface geometry that represents the space in
      Level of Detail 0.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod0MultiSurface
    owner: AbstractBridge
    domain_of:
    - AbstractSpace
    - AbstractThematicSurface
    range: string
    required: false
    multivalued: false
  lod1Solid:
    name: lod1Solid
    description: Relates to a 3D Solid geometry that represents the space in Level
      of Detail 1.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod1Solid
    owner: AbstractBridge
    domain_of:
    - AbstractSpace
    range: string
    required: false
    multivalued: false
  lod3Solid:
    name: lod3Solid
    description: Relates to a 3D Solid geometry that represents the space in Level
      of Detail 3.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod3Solid
    owner: AbstractBridge
    domain_of:
    - AbstractSpace
    range: string
    required: false
    multivalued: false
  lod0MultiCurve:
    name: lod0MultiCurve
    description: Relates to a 3D MultiCurve geometry that represents the space in
      Level of Detail 0.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod0MultiCurve
    owner: AbstractBridge
    domain_of:
    - AbstractSpace
    - AbstractThematicSurface
    range: string
    required: false
    multivalued: false
  lod2Solid:
    name: lod2Solid
    description: Relates to a 3D Solid geometry that represents the space in Level
      of Detail 2.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod2Solid
    owner: AbstractBridge
    domain_of:
    - AbstractSpace
    range: string
    required: false
    multivalued: false
  lod0Point:
    name: lod0Point
    description: Relates to a 3D Point geometry that represents the space in Level
      of Detail 0.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod0Point
    owner: AbstractBridge
    domain_of:
    - AbstractSpace
    range: string
    required: false
    multivalued: false
  lod3MultiCurve:
    name: lod3MultiCurve
    description: Relates to a 3D MultiCurve geometry that represents the space in
      Level of Detail 3.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod3MultiCurve
    owner: AbstractBridge
    domain_of:
    - AbstractSpace
    range: string
    required: false
    multivalued: false
  lod2MultiSurface:
    name: lod2MultiSurface
    description: Relates to a 3D MultiSurface geometry that represents the space in
      Level of Detail 2.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod2MultiSurface
    owner: AbstractBridge
    domain_of:
    - AbstractSpace
    - AbstractThematicSurface
    range: string
    required: false
    multivalued: false
  relativeToTerrain:
    name: relativeToTerrain
    description: Describes the vertical position of the city object relative to the
      surrounding terrain.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: relativeToTerrain
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: AbstractBridge
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
    owner: AbstractBridge
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
    owner: AbstractBridge
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>