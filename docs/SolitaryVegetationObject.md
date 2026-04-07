

# Class: SolitaryVegetationObject 


_A SolitaryVegetationObject represents individual vegetation objects, e.g., trees or bushes._





URI: [citygml:SolitaryVegetationObject](https://www.ogc.org/standards/citygml/SolitaryVegetationObject)





```mermaid
 classDiagram
    class SolitaryVegetationObject
    click SolitaryVegetationObject href "../SolitaryVegetationObject/"
      AbstractVegetationObject <|-- SolitaryVegetationObject
        click AbstractVegetationObject href "../AbstractVegetationObject/"
      
      SolitaryVegetationObject : adeOfAbstractCityObject
        
          
    
        
        
        SolitaryVegetationObject --> "*" ADEOfAbstractCityObject : adeOfAbstractCityObject
        click ADEOfAbstractCityObject href "../ADEOfAbstractCityObject/"
    

        
      SolitaryVegetationObject : adeOfAbstractFeature
        
          
    
        
        
        SolitaryVegetationObject --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      SolitaryVegetationObject : adeOfAbstractFeatureWithLifespan
        
          
    
        
        
        SolitaryVegetationObject --> "*" ADEOfAbstractFeatureWithLifespan : adeOfAbstractFeatureWithLifespan
        click ADEOfAbstractFeatureWithLifespan href "../ADEOfAbstractFeatureWithLifespan/"
    

        
      SolitaryVegetationObject : adeOfAbstractOccupiedSpace
        
          
    
        
        
        SolitaryVegetationObject --> "*" ADEOfAbstractOccupiedSpace : adeOfAbstractOccupiedSpace
        click ADEOfAbstractOccupiedSpace href "../ADEOfAbstractOccupiedSpace/"
    

        
      SolitaryVegetationObject : adeOfAbstractPhysicalSpace
        
          
    
        
        
        SolitaryVegetationObject --> "*" ADEOfAbstractPhysicalSpace : adeOfAbstractPhysicalSpace
        click ADEOfAbstractPhysicalSpace href "../ADEOfAbstractPhysicalSpace/"
    

        
      SolitaryVegetationObject : adeOfAbstractSpace
        
          
    
        
        
        SolitaryVegetationObject --> "*" ADEOfAbstractSpace : adeOfAbstractSpace
        click ADEOfAbstractSpace href "../ADEOfAbstractSpace/"
    

        
      SolitaryVegetationObject : adeOfAbstractVegetationObject
        
          
    
        
        
        SolitaryVegetationObject --> "*" ADEOfAbstractVegetationObject : adeOfAbstractVegetationObject
        click ADEOfAbstractVegetationObject href "../ADEOfAbstractVegetationObject/"
    

        
      SolitaryVegetationObject : adeOfSolitaryVegetationObject
        
          
    
        
        
        SolitaryVegetationObject --> "*" ADEOfSolitaryVegetationObject : adeOfSolitaryVegetationObject
        click ADEOfSolitaryVegetationObject href "../ADEOfSolitaryVegetationObject/"
    

        
      SolitaryVegetationObject : appearance
        
          
    
        
        
        SolitaryVegetationObject --> "*" AbstractAppearance : appearance
        click AbstractAppearance href "../AbstractAppearance/"
    

        
      SolitaryVegetationObject : area
        
          
    
        
        
        SolitaryVegetationObject --> "*" QualifiedArea : area
        click QualifiedArea href "../QualifiedArea/"
    

        
      SolitaryVegetationObject : boundary
        
          
    
        
        
        SolitaryVegetationObject --> "*" AbstractSpaceBoundary : boundary
        click AbstractSpaceBoundary href "../AbstractSpaceBoundary/"
    

        
      SolitaryVegetationObject : class
        
          
    
        
        
        SolitaryVegetationObject --> "0..1" SolitaryVegetationObjectClassValue : class
        click SolitaryVegetationObjectClassValue href "../SolitaryVegetationObjectClassValue/"
    

        
      SolitaryVegetationObject : creationDate
        
      SolitaryVegetationObject : crownDiameter
        
      SolitaryVegetationObject : description
        
      SolitaryVegetationObject : dynamizer
        
          
    
        
        
        SolitaryVegetationObject --> "*" AbstractDynamizer : dynamizer
        click AbstractDynamizer href "../AbstractDynamizer/"
    

        
      SolitaryVegetationObject : externalReference
        
          
    
        
        
        SolitaryVegetationObject --> "*" ExternalReference : externalReference
        click ExternalReference href "../ExternalReference/"
    

        
      SolitaryVegetationObject : featureID
        
          
    
        
        
        SolitaryVegetationObject --> "1" ID : featureID
        click ID href "../ID/"
    

        
      SolitaryVegetationObject : function
        
          
    
        
        
        SolitaryVegetationObject --> "*" SolitaryVegetationObjectFunctionValue : function
        click SolitaryVegetationObjectFunctionValue href "../SolitaryVegetationObjectFunctionValue/"
    

        
      SolitaryVegetationObject : generalizesTo
        
          
    
        
        
        SolitaryVegetationObject --> "*" AbstractCityObject : generalizesTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      SolitaryVegetationObject : genericAttribute
        
          
    
        
        
        SolitaryVegetationObject --> "*" AbstractGenericAttribute : genericAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
    

        
      SolitaryVegetationObject : height
        
      SolitaryVegetationObject : identifier
        
      SolitaryVegetationObject : lod0MultiCurve
        
      SolitaryVegetationObject : lod0MultiSurface
        
      SolitaryVegetationObject : lod0Point
        
      SolitaryVegetationObject : lod1ImplicitRepresentation
        
          
    
        
        
        SolitaryVegetationObject --> "0..1" ImplicitGeometry : lod1ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      SolitaryVegetationObject : lod1Solid
        
      SolitaryVegetationObject : lod1TerrainIntersectionCurve
        
      SolitaryVegetationObject : lod2ImplicitRepresentation
        
          
    
        
        
        SolitaryVegetationObject --> "0..1" ImplicitGeometry : lod2ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      SolitaryVegetationObject : lod2MultiCurve
        
      SolitaryVegetationObject : lod2MultiSurface
        
      SolitaryVegetationObject : lod2Solid
        
      SolitaryVegetationObject : lod2TerrainIntersectionCurve
        
      SolitaryVegetationObject : lod3ImplicitRepresentation
        
          
    
        
        
        SolitaryVegetationObject --> "0..1" ImplicitGeometry : lod3ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      SolitaryVegetationObject : lod3MultiCurve
        
      SolitaryVegetationObject : lod3MultiSurface
        
      SolitaryVegetationObject : lod3Solid
        
      SolitaryVegetationObject : lod3TerrainIntersectionCurve
        
      SolitaryVegetationObject : maxRootBallDepth
        
      SolitaryVegetationObject : name
        
      SolitaryVegetationObject : pointCloud
        
          
    
        
        
        SolitaryVegetationObject --> "0..1" AbstractPointCloud : pointCloud
        click AbstractPointCloud href "../AbstractPointCloud/"
    

        
      SolitaryVegetationObject : relatedTo
        
          
    
        
        
        SolitaryVegetationObject --> "*" AbstractCityObject : relatedTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      SolitaryVegetationObject : relativeToTerrain
        
          
    
        
        
        SolitaryVegetationObject --> "0..1" RelativeToTerrain : relativeToTerrain
        click RelativeToTerrain href "../RelativeToTerrain/"
    

        
      SolitaryVegetationObject : relativeToWater
        
          
    
        
        
        SolitaryVegetationObject --> "0..1" RelativeToWater : relativeToWater
        click RelativeToWater href "../RelativeToWater/"
    

        
      SolitaryVegetationObject : rootBallDiameter
        
      SolitaryVegetationObject : spaceType
        
          
    
        
        
        SolitaryVegetationObject --> "0..1" SpaceType : spaceType
        click SpaceType href "../SpaceType/"
    

        
      SolitaryVegetationObject : species
        
          
    
        
        
        SolitaryVegetationObject --> "0..1" SpeciesValue : species
        click SpeciesValue href "../SpeciesValue/"
    

        
      SolitaryVegetationObject : terminationDate
        
      SolitaryVegetationObject : trunkDiameter
        
      SolitaryVegetationObject : usage
        
          
    
        
        
        SolitaryVegetationObject --> "*" SolitaryVegetationObjectUsageValue : usage
        click SolitaryVegetationObjectUsageValue href "../SolitaryVegetationObjectUsageValue/"
    

        
      SolitaryVegetationObject : validFrom
        
      SolitaryVegetationObject : validTo
        
      SolitaryVegetationObject : volume
        
          
    
        
        
        SolitaryVegetationObject --> "*" QualifiedVolume : volume
        click QualifiedVolume href "../QualifiedVolume/"
    

        
      
```





## Inheritance
* [AbstractFeature](AbstractFeature.md)
    * [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md)
        * [AbstractCityObject](AbstractCityObject.md)
            * [AbstractSpace](AbstractSpace.md)
                * [AbstractPhysicalSpace](AbstractPhysicalSpace.md)
                    * [AbstractOccupiedSpace](AbstractOccupiedSpace.md)
                        * [AbstractVegetationObject](AbstractVegetationObject.md)
                            * **SolitaryVegetationObject**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [class](class.md) | 0..1 <br/> [SolitaryVegetationObjectClassValue](SolitaryVegetationObjectClassValue.md) | Indicates the specific type of the SolitaryVegetationObject | direct |
| [function](function.md) | * <br/> [SolitaryVegetationObjectFunctionValue](SolitaryVegetationObjectFunctionValue.md) | Specifies the intended purposes of the SolitaryVegetationObject | direct |
| [usage](usage.md) | * <br/> [SolitaryVegetationObjectUsageValue](SolitaryVegetationObjectUsageValue.md) | Specifies the actual uses of the SolitaryVegetationObject | direct |
| [species](species.md) | 0..1 <br/> [SpeciesValue](SpeciesValue.md) | Indicates the botanical name of the SolitaryVegetationObject | direct |
| [height](height.md) | 0..1 <br/> [Float](Float.md) | Distance between the highest point of the vegetation object and the lowest po... | direct |
| [trunkDiameter](trunkDiameter.md) | 0..1 <br/> [Float](Float.md) | Specifies the diameter of the SolitaryCityObject's trunk | direct |
| [crownDiameter](crownDiameter.md) | 0..1 <br/> [Float](Float.md) | Specifies the diameter of the SolitaryCityObject's crown | direct |
| [rootBallDiameter](rootBallDiameter.md) | 0..1 <br/> [Float](Float.md) | Specifies the diameter of the SolitaryCityObject's root ball | direct |
| [maxRootBallDepth](maxRootBallDepth.md) | 0..1 <br/> [Float](Float.md) | Specifies the vertical distance between the lowest point of the SolitaryVeget... | direct |
| [adeOfSolitaryVegetationObject](adeOfSolitaryVegetationObject.md) | * <br/> [ADEOfSolitaryVegetationObject](ADEOfSolitaryVegetationObject.md) | Augments the SolitaryVegetationObject with properties defined in an ADE | direct |
| [adeOfAbstractVegetationObject](adeOfAbstractVegetationObject.md) | * <br/> [ADEOfAbstractVegetationObject](ADEOfAbstractVegetationObject.md) | Augments AbstractVegetationObject with properties defined in an ADE | [AbstractVegetationObject](AbstractVegetationObject.md) |
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
| [boundary](boundary.md) | * <br/> [AbstractSpaceBoundary](AbstractSpaceBoundary.md) | Relates to surfaces that bound the space | [AbstractSpace](AbstractSpace.md) |
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
| self | citygml:SolitaryVegetationObject |
| native | citygml:SolitaryVegetationObject |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SolitaryVegetationObject
description: A SolitaryVegetationObject represents individual vegetation objects,
  e.g., trees or bushes.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractVegetationObject
abstract: false
attributes:
  class:
    name: class
    description: Indicates the specific type of the SolitaryVegetationObject.
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
    range: SolitaryVegetationObjectClassValue
    required: false
    multivalued: false
  function:
    name: function
    description: Specifies the intended purposes of the SolitaryVegetationObject.
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
    range: SolitaryVegetationObjectFunctionValue
    required: false
    multivalued: true
  usage:
    name: usage
    description: Specifies the actual uses of the SolitaryVegetationObject.
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
    range: SolitaryVegetationObjectUsageValue
    required: false
    multivalued: true
  species:
    name: species
    description: Indicates the botanical name of the SolitaryVegetationObject.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - SolitaryVegetationObject
    range: SpeciesValue
    required: false
    multivalued: false
  height:
    name: height
    description: Distance between the highest point of the vegetation object and the
      lowest point of the terrain at the bottom of the object.
    from_schema: https://www.ogc.org/standards/citygml
    domain_of:
    - AbstractConstruction
    - SolitaryVegetationObject
    range: float
    required: false
    multivalued: false
  trunkDiameter:
    name: trunkDiameter
    description: Specifies the diameter of the SolitaryCityObject's trunk.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - SolitaryVegetationObject
    range: float
    required: false
    multivalued: false
  crownDiameter:
    name: crownDiameter
    description: Specifies the diameter of the SolitaryCityObject's crown.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - SolitaryVegetationObject
    range: float
    required: false
    multivalued: false
  rootBallDiameter:
    name: rootBallDiameter
    description: Specifies the diameter of the SolitaryCityObject's root ball.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - SolitaryVegetationObject
    range: float
    required: false
    multivalued: false
  maxRootBallDepth:
    name: maxRootBallDepth
    description: Specifies the vertical distance between the lowest point of the SolitaryVegetationObject's
      root ball and the terrain surface.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - SolitaryVegetationObject
    range: float
    required: false
    multivalued: false
  adeOfSolitaryVegetationObject:
    name: adeOfSolitaryVegetationObject
    description: Augments the SolitaryVegetationObject with properties defined in
      an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - SolitaryVegetationObject
    range: ADEOfSolitaryVegetationObject
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: SolitaryVegetationObject
description: A SolitaryVegetationObject represents individual vegetation objects,
  e.g., trees or bushes.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractVegetationObject
abstract: false
attributes:
  class:
    name: class
    description: Indicates the specific type of the SolitaryVegetationObject.
    from_schema: https://www.ogc.org/standards/citygml
    alias: class
    owner: SolitaryVegetationObject
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
    range: SolitaryVegetationObjectClassValue
    required: false
    multivalued: false
  function:
    name: function
    description: Specifies the intended purposes of the SolitaryVegetationObject.
    from_schema: https://www.ogc.org/standards/citygml
    alias: function
    owner: SolitaryVegetationObject
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
    range: SolitaryVegetationObjectFunctionValue
    required: false
    multivalued: true
  usage:
    name: usage
    description: Specifies the actual uses of the SolitaryVegetationObject.
    from_schema: https://www.ogc.org/standards/citygml
    alias: usage
    owner: SolitaryVegetationObject
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
    range: SolitaryVegetationObjectUsageValue
    required: false
    multivalued: true
  species:
    name: species
    description: Indicates the botanical name of the SolitaryVegetationObject.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: species
    owner: SolitaryVegetationObject
    domain_of:
    - SolitaryVegetationObject
    range: SpeciesValue
    required: false
    multivalued: false
  height:
    name: height
    description: Distance between the highest point of the vegetation object and the
      lowest point of the terrain at the bottom of the object.
    from_schema: https://www.ogc.org/standards/citygml
    alias: height
    owner: SolitaryVegetationObject
    domain_of:
    - AbstractConstruction
    - SolitaryVegetationObject
    range: float
    required: false
    multivalued: false
  trunkDiameter:
    name: trunkDiameter
    description: Specifies the diameter of the SolitaryCityObject's trunk.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: trunkDiameter
    owner: SolitaryVegetationObject
    domain_of:
    - SolitaryVegetationObject
    range: float
    required: false
    multivalued: false
  crownDiameter:
    name: crownDiameter
    description: Specifies the diameter of the SolitaryCityObject's crown.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: crownDiameter
    owner: SolitaryVegetationObject
    domain_of:
    - SolitaryVegetationObject
    range: float
    required: false
    multivalued: false
  rootBallDiameter:
    name: rootBallDiameter
    description: Specifies the diameter of the SolitaryCityObject's root ball.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: rootBallDiameter
    owner: SolitaryVegetationObject
    domain_of:
    - SolitaryVegetationObject
    range: float
    required: false
    multivalued: false
  maxRootBallDepth:
    name: maxRootBallDepth
    description: Specifies the vertical distance between the lowest point of the SolitaryVegetationObject's
      root ball and the terrain surface.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: maxRootBallDepth
    owner: SolitaryVegetationObject
    domain_of:
    - SolitaryVegetationObject
    range: float
    required: false
    multivalued: false
  adeOfSolitaryVegetationObject:
    name: adeOfSolitaryVegetationObject
    description: Augments the SolitaryVegetationObject with properties defined in
      an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfSolitaryVegetationObject
    owner: SolitaryVegetationObject
    domain_of:
    - SolitaryVegetationObject
    range: ADEOfSolitaryVegetationObject
    required: false
    multivalued: true
  adeOfAbstractVegetationObject:
    name: adeOfAbstractVegetationObject
    description: Augments AbstractVegetationObject with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractVegetationObject
    owner: SolitaryVegetationObject
    domain_of:
    - AbstractVegetationObject
    range: ADEOfAbstractVegetationObject
    required: false
    multivalued: true
  adeOfAbstractOccupiedSpace:
    name: adeOfAbstractOccupiedSpace
    description: Augments AbstractOccupiedSpace with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractOccupiedSpace
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
    domain_of:
    - AbstractSpace
    range: string
    required: false
    multivalued: false
  boundary:
    name: boundary
    description: Relates to surfaces that bound the space.
    from_schema: https://www.ogc.org/standards/citygml
    alias: boundary
    owner: SolitaryVegetationObject
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
    range: AbstractSpaceBoundary
    required: false
    multivalued: true
  lod0MultiCurve:
    name: lod0MultiCurve
    description: Relates to a 3D MultiCurve geometry that represents the space in
      Level of Detail 0.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod0MultiCurve
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
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
    owner: SolitaryVegetationObject
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>