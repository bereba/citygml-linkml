

# Class: Bridge 


_A Bridge represents a structure that affords the passage of pedestrians, animals, vehicles, and service(s) above obstacles or between two points at a height above ground. [cf. ISO 6707-1]_





URI: [citygml:Bridge](https://www.ogc.org/standards/citygml/Bridge)





```mermaid
 classDiagram
    class Bridge
    click Bridge href "../Bridge/"
      AbstractBridge <|-- Bridge
        click AbstractBridge href "../AbstractBridge/"
      
      Bridge : address
        
          
    
        
        
        Bridge --> "*" Address : address
        click Address href "../Address/"
    

        
      Bridge : adeOfAbstractBridge
        
          
    
        
        
        Bridge --> "*" ADEOfAbstractBridge : adeOfAbstractBridge
        click ADEOfAbstractBridge href "../ADEOfAbstractBridge/"
    

        
      Bridge : adeOfAbstractCityObject
        
          
    
        
        
        Bridge --> "*" ADEOfAbstractCityObject : adeOfAbstractCityObject
        click ADEOfAbstractCityObject href "../ADEOfAbstractCityObject/"
    

        
      Bridge : adeOfAbstractConstruction
        
          
    
        
        
        Bridge --> "*" ADEOfAbstractConstruction : adeOfAbstractConstruction
        click ADEOfAbstractConstruction href "../ADEOfAbstractConstruction/"
    

        
      Bridge : adeOfAbstractFeature
        
          
    
        
        
        Bridge --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      Bridge : adeOfAbstractFeatureWithLifespan
        
          
    
        
        
        Bridge --> "*" ADEOfAbstractFeatureWithLifespan : adeOfAbstractFeatureWithLifespan
        click ADEOfAbstractFeatureWithLifespan href "../ADEOfAbstractFeatureWithLifespan/"
    

        
      Bridge : adeOfAbstractOccupiedSpace
        
          
    
        
        
        Bridge --> "*" ADEOfAbstractOccupiedSpace : adeOfAbstractOccupiedSpace
        click ADEOfAbstractOccupiedSpace href "../ADEOfAbstractOccupiedSpace/"
    

        
      Bridge : adeOfAbstractPhysicalSpace
        
          
    
        
        
        Bridge --> "*" ADEOfAbstractPhysicalSpace : adeOfAbstractPhysicalSpace
        click ADEOfAbstractPhysicalSpace href "../ADEOfAbstractPhysicalSpace/"
    

        
      Bridge : adeOfAbstractSpace
        
          
    
        
        
        Bridge --> "*" ADEOfAbstractSpace : adeOfAbstractSpace
        click ADEOfAbstractSpace href "../ADEOfAbstractSpace/"
    

        
      Bridge : adeOfBridge
        
          
    
        
        
        Bridge --> "*" ADEOfBridge : adeOfBridge
        click ADEOfBridge href "../ADEOfBridge/"
    

        
      Bridge : appearance
        
          
    
        
        
        Bridge --> "*" AbstractAppearance : appearance
        click AbstractAppearance href "../AbstractAppearance/"
    

        
      Bridge : area
        
          
    
        
        
        Bridge --> "*" QualifiedArea : area
        click QualifiedArea href "../QualifiedArea/"
    

        
      Bridge : boundary
        
          
    
        
        
        Bridge --> "*" AbstractThematicSurface : boundary
        click AbstractThematicSurface href "../AbstractThematicSurface/"
    

        
      Bridge : bridgeConstructiveElement
        
          
    
        
        
        Bridge --> "*" BridgeConstructiveElement : bridgeConstructiveElement
        click BridgeConstructiveElement href "../BridgeConstructiveElement/"
    

        
      Bridge : bridgeFurniture
        
          
    
        
        
        Bridge --> "*" BridgeFurniture : bridgeFurniture
        click BridgeFurniture href "../BridgeFurniture/"
    

        
      Bridge : bridgeInstallation
        
          
    
        
        
        Bridge --> "*" BridgeInstallation : bridgeInstallation
        click BridgeInstallation href "../BridgeInstallation/"
    

        
      Bridge : bridgePart
        
          
    
        
        
        Bridge --> "*" BridgePart : bridgePart
        click BridgePart href "../BridgePart/"
    

        
      Bridge : bridgeRoom
        
          
    
        
        
        Bridge --> "*" BridgeRoom : bridgeRoom
        click BridgeRoom href "../BridgeRoom/"
    

        
      Bridge : class
        
          
    
        
        
        Bridge --> "0..1" BridgeClassValue : class
        click BridgeClassValue href "../BridgeClassValue/"
    

        
      Bridge : conditionOfConstruction
        
          
    
        
        
        Bridge --> "0..1" ConditionOfConstructionValue : conditionOfConstruction
        click ConditionOfConstructionValue href "../ConditionOfConstructionValue/"
    

        
      Bridge : constructionEvent
        
          
    
        
        
        Bridge --> "*" ConstructionEvent : constructionEvent
        click ConstructionEvent href "../ConstructionEvent/"
    

        
      Bridge : creationDate
        
      Bridge : dateOfConstruction
        
      Bridge : dateOfDemolition
        
      Bridge : description
        
      Bridge : dynamizer
        
          
    
        
        
        Bridge --> "*" AbstractDynamizer : dynamizer
        click AbstractDynamizer href "../AbstractDynamizer/"
    

        
      Bridge : elevation
        
          
    
        
        
        Bridge --> "*" Elevation : elevation
        click Elevation href "../Elevation/"
    

        
      Bridge : externalReference
        
          
    
        
        
        Bridge --> "*" ExternalReference : externalReference
        click ExternalReference href "../ExternalReference/"
    

        
      Bridge : featureID
        
          
    
        
        
        Bridge --> "1" ID : featureID
        click ID href "../ID/"
    

        
      Bridge : function
        
          
    
        
        
        Bridge --> "*" BridgeFunctionValue : function
        click BridgeFunctionValue href "../BridgeFunctionValue/"
    

        
      Bridge : generalizesTo
        
          
    
        
        
        Bridge --> "*" AbstractCityObject : generalizesTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      Bridge : genericAttribute
        
          
    
        
        
        Bridge --> "*" AbstractGenericAttribute : genericAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
    

        
      Bridge : height
        
          
    
        
        
        Bridge --> "*" Height : height
        click Height href "../Height/"
    

        
      Bridge : identifier
        
      Bridge : isMovable
        
      Bridge : lod0MultiCurve
        
      Bridge : lod0MultiSurface
        
      Bridge : lod0Point
        
      Bridge : lod1ImplicitRepresentation
        
          
    
        
        
        Bridge --> "0..1" ImplicitGeometry : lod1ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      Bridge : lod1Solid
        
      Bridge : lod1TerrainIntersectionCurve
        
      Bridge : lod2ImplicitRepresentation
        
          
    
        
        
        Bridge --> "0..1" ImplicitGeometry : lod2ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      Bridge : lod2MultiCurve
        
      Bridge : lod2MultiSurface
        
      Bridge : lod2Solid
        
      Bridge : lod2TerrainIntersectionCurve
        
      Bridge : lod3ImplicitRepresentation
        
          
    
        
        
        Bridge --> "0..1" ImplicitGeometry : lod3ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      Bridge : lod3MultiCurve
        
      Bridge : lod3MultiSurface
        
      Bridge : lod3Solid
        
      Bridge : lod3TerrainIntersectionCurve
        
      Bridge : name
        
      Bridge : occupancy
        
          
    
        
        
        Bridge --> "*" Occupancy : occupancy
        click Occupancy href "../Occupancy/"
    

        
      Bridge : pointCloud
        
          
    
        
        
        Bridge --> "0..1" AbstractPointCloud : pointCloud
        click AbstractPointCloud href "../AbstractPointCloud/"
    

        
      Bridge : relatedTo
        
          
    
        
        
        Bridge --> "*" AbstractCityObject : relatedTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      Bridge : relativeToTerrain
        
          
    
        
        
        Bridge --> "0..1" RelativeToTerrain : relativeToTerrain
        click RelativeToTerrain href "../RelativeToTerrain/"
    

        
      Bridge : relativeToWater
        
          
    
        
        
        Bridge --> "0..1" RelativeToWater : relativeToWater
        click RelativeToWater href "../RelativeToWater/"
    

        
      Bridge : spaceType
        
          
    
        
        
        Bridge --> "0..1" SpaceType : spaceType
        click SpaceType href "../SpaceType/"
    

        
      Bridge : terminationDate
        
      Bridge : usage
        
          
    
        
        
        Bridge --> "*" BridgeUsageValue : usage
        click BridgeUsageValue href "../BridgeUsageValue/"
    

        
      Bridge : validFrom
        
      Bridge : validTo
        
      Bridge : volume
        
          
    
        
        
        Bridge --> "*" QualifiedVolume : volume
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
                            * [AbstractBridge](AbstractBridge.md)
                                * **Bridge**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [adeOfBridge](adeOfBridge.md) | * <br/> [ADEOfBridge](ADEOfBridge.md) | Augments the Bridge with properties defined in an ADE | direct |
| [bridgePart](bridgePart.md) | * <br/> [BridgePart](BridgePart.md) | Relates the bridge parts to the Bridge | direct |
| [class](class.md) | 0..1 <br/> [BridgeClassValue](BridgeClassValue.md) | Indicates the specific type of the Bridge or BridgePart | [AbstractBridge](AbstractBridge.md) |
| [function](function.md) | * <br/> [BridgeFunctionValue](BridgeFunctionValue.md) | Specifies the intended purposes of the Bridge or BridgePart | [AbstractBridge](AbstractBridge.md) |
| [usage](usage.md) | * <br/> [BridgeUsageValue](BridgeUsageValue.md) | Specifies the actual uses of the Bridge or BridgePart | [AbstractBridge](AbstractBridge.md) |
| [isMovable](isMovable.md) | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the Bridge or BridgePart can be moved to allow for watercra... | [AbstractBridge](AbstractBridge.md) |
| [adeOfAbstractBridge](adeOfAbstractBridge.md) | * <br/> [ADEOfAbstractBridge](ADEOfAbstractBridge.md) | Augments AbstractBridge with properties defined in an ADE | [AbstractBridge](AbstractBridge.md) |
| [bridgeRoom](bridgeRoom.md) | * <br/> [BridgeRoom](BridgeRoom.md) | Relates the rooms to the Bridge or BridgePart | [AbstractBridge](AbstractBridge.md) |
| [bridgeFurniture](bridgeFurniture.md) | * <br/> [BridgeFurniture](BridgeFurniture.md) | Relates the furniture objects to the Bridge or BridgePart | [AbstractBridge](AbstractBridge.md) |
| [bridgeConstructiveElement](bridgeConstructiveElement.md) | * <br/> [BridgeConstructiveElement](BridgeConstructiveElement.md) | Relates the constructive elements to the Bridge or BridgePart | [AbstractBridge](AbstractBridge.md) |
| [address](address.md) | * <br/> [Address](Address.md) | Relates the addresses to the Bridge or BridgePart | [AbstractBridge](AbstractBridge.md) |
| [bridgeInstallation](bridgeInstallation.md) | * <br/> [BridgeInstallation](BridgeInstallation.md) | Relates the installation objects to the Bridge or BridgePart | [AbstractBridge](AbstractBridge.md) |
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
| self | citygml:Bridge |
| native | citygml:Bridge |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Bridge
description: A Bridge represents a structure that affords the passage of pedestrians,
  animals, vehicles, and service(s) above obstacles or between two points at a height
  above ground. [cf. ISO 6707-1]
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractBridge
abstract: false
attributes:
  adeOfBridge:
    name: adeOfBridge
    description: Augments the Bridge with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - Bridge
    range: ADEOfBridge
    required: false
    multivalued: true
  bridgePart:
    name: bridgePart
    description: Relates the bridge parts to the Bridge.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - Bridge
    range: BridgePart
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: Bridge
description: A Bridge represents a structure that affords the passage of pedestrians,
  animals, vehicles, and service(s) above obstacles or between two points at a height
  above ground. [cf. ISO 6707-1]
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractBridge
abstract: false
attributes:
  adeOfBridge:
    name: adeOfBridge
    description: Augments the Bridge with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfBridge
    owner: Bridge
    domain_of:
    - Bridge
    range: ADEOfBridge
    required: false
    multivalued: true
  bridgePart:
    name: bridgePart
    description: Relates the bridge parts to the Bridge.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: bridgePart
    owner: Bridge
    domain_of:
    - Bridge
    range: BridgePart
    required: false
    multivalued: true
  class:
    name: class
    description: Indicates the specific type of the Bridge or BridgePart.
    from_schema: https://www.ogc.org/standards/citygml
    alias: class
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: Bridge
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
    owner: Bridge
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
    owner: Bridge
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>