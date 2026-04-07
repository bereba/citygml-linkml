

# Class: CityFurniture 


_CityFurniture is an object or piece of equipment installed in the outdoor environment for various purposes. Examples include street signs, traffic signals, street lamps, benches, fountains._





URI: [citygml:CityFurniture](https://www.ogc.org/standards/citygml/CityFurniture)





```mermaid
 classDiagram
    class CityFurniture
    click CityFurniture href "../CityFurniture/"
      AbstractOccupiedSpace <|-- CityFurniture
        click AbstractOccupiedSpace href "../AbstractOccupiedSpace/"
      
      CityFurniture : adeOfAbstractCityObject
        
          
    
        
        
        CityFurniture --> "*" ADEOfAbstractCityObject : adeOfAbstractCityObject
        click ADEOfAbstractCityObject href "../ADEOfAbstractCityObject/"
    

        
      CityFurniture : adeOfAbstractFeature
        
          
    
        
        
        CityFurniture --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      CityFurniture : adeOfAbstractFeatureWithLifespan
        
          
    
        
        
        CityFurniture --> "*" ADEOfAbstractFeatureWithLifespan : adeOfAbstractFeatureWithLifespan
        click ADEOfAbstractFeatureWithLifespan href "../ADEOfAbstractFeatureWithLifespan/"
    

        
      CityFurniture : adeOfAbstractOccupiedSpace
        
          
    
        
        
        CityFurniture --> "*" ADEOfAbstractOccupiedSpace : adeOfAbstractOccupiedSpace
        click ADEOfAbstractOccupiedSpace href "../ADEOfAbstractOccupiedSpace/"
    

        
      CityFurniture : adeOfAbstractPhysicalSpace
        
          
    
        
        
        CityFurniture --> "*" ADEOfAbstractPhysicalSpace : adeOfAbstractPhysicalSpace
        click ADEOfAbstractPhysicalSpace href "../ADEOfAbstractPhysicalSpace/"
    

        
      CityFurniture : adeOfAbstractSpace
        
          
    
        
        
        CityFurniture --> "*" ADEOfAbstractSpace : adeOfAbstractSpace
        click ADEOfAbstractSpace href "../ADEOfAbstractSpace/"
    

        
      CityFurniture : adeOfCityFurniture
        
          
    
        
        
        CityFurniture --> "*" ADEOfCityFurniture : adeOfCityFurniture
        click ADEOfCityFurniture href "../ADEOfCityFurniture/"
    

        
      CityFurniture : appearance
        
          
    
        
        
        CityFurniture --> "*" AbstractAppearance : appearance
        click AbstractAppearance href "../AbstractAppearance/"
    

        
      CityFurniture : area
        
          
    
        
        
        CityFurniture --> "*" QualifiedArea : area
        click QualifiedArea href "../QualifiedArea/"
    

        
      CityFurniture : boundary
        
          
    
        
        
        CityFurniture --> "*" AbstractSpaceBoundary : boundary
        click AbstractSpaceBoundary href "../AbstractSpaceBoundary/"
    

        
      CityFurniture : class
        
          
    
        
        
        CityFurniture --> "0..1" CityFurnitureClassValue : class
        click CityFurnitureClassValue href "../CityFurnitureClassValue/"
    

        
      CityFurniture : creationDate
        
      CityFurniture : description
        
      CityFurniture : dynamizer
        
          
    
        
        
        CityFurniture --> "*" AbstractDynamizer : dynamizer
        click AbstractDynamizer href "../AbstractDynamizer/"
    

        
      CityFurniture : externalReference
        
          
    
        
        
        CityFurniture --> "*" ExternalReference : externalReference
        click ExternalReference href "../ExternalReference/"
    

        
      CityFurniture : featureID
        
          
    
        
        
        CityFurniture --> "1" ID : featureID
        click ID href "../ID/"
    

        
      CityFurniture : function
        
          
    
        
        
        CityFurniture --> "*" CityFurnitureFunctionValue : function
        click CityFurnitureFunctionValue href "../CityFurnitureFunctionValue/"
    

        
      CityFurniture : generalizesTo
        
          
    
        
        
        CityFurniture --> "*" AbstractCityObject : generalizesTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      CityFurniture : genericAttribute
        
          
    
        
        
        CityFurniture --> "*" AbstractGenericAttribute : genericAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
    

        
      CityFurniture : identifier
        
      CityFurniture : lod0MultiCurve
        
      CityFurniture : lod0MultiSurface
        
      CityFurniture : lod0Point
        
      CityFurniture : lod1ImplicitRepresentation
        
          
    
        
        
        CityFurniture --> "0..1" ImplicitGeometry : lod1ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      CityFurniture : lod1Solid
        
      CityFurniture : lod1TerrainIntersectionCurve
        
      CityFurniture : lod2ImplicitRepresentation
        
          
    
        
        
        CityFurniture --> "0..1" ImplicitGeometry : lod2ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      CityFurniture : lod2MultiCurve
        
      CityFurniture : lod2MultiSurface
        
      CityFurniture : lod2Solid
        
      CityFurniture : lod2TerrainIntersectionCurve
        
      CityFurniture : lod3ImplicitRepresentation
        
          
    
        
        
        CityFurniture --> "0..1" ImplicitGeometry : lod3ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      CityFurniture : lod3MultiCurve
        
      CityFurniture : lod3MultiSurface
        
      CityFurniture : lod3Solid
        
      CityFurniture : lod3TerrainIntersectionCurve
        
      CityFurniture : name
        
      CityFurniture : pointCloud
        
          
    
        
        
        CityFurniture --> "0..1" AbstractPointCloud : pointCloud
        click AbstractPointCloud href "../AbstractPointCloud/"
    

        
      CityFurniture : relatedTo
        
          
    
        
        
        CityFurniture --> "*" AbstractCityObject : relatedTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      CityFurniture : relativeToTerrain
        
          
    
        
        
        CityFurniture --> "0..1" RelativeToTerrain : relativeToTerrain
        click RelativeToTerrain href "../RelativeToTerrain/"
    

        
      CityFurniture : relativeToWater
        
          
    
        
        
        CityFurniture --> "0..1" RelativeToWater : relativeToWater
        click RelativeToWater href "../RelativeToWater/"
    

        
      CityFurniture : spaceType
        
          
    
        
        
        CityFurniture --> "0..1" SpaceType : spaceType
        click SpaceType href "../SpaceType/"
    

        
      CityFurniture : terminationDate
        
      CityFurniture : usage
        
          
    
        
        
        CityFurniture --> "*" CityFurnitureUsageValue : usage
        click CityFurnitureUsageValue href "../CityFurnitureUsageValue/"
    

        
      CityFurniture : validFrom
        
      CityFurniture : validTo
        
      CityFurniture : volume
        
          
    
        
        
        CityFurniture --> "*" QualifiedVolume : volume
        click QualifiedVolume href "../QualifiedVolume/"
    

        
      
```





## Inheritance
* [AbstractFeature](AbstractFeature.md)
    * [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md)
        * [AbstractCityObject](AbstractCityObject.md)
            * [AbstractSpace](AbstractSpace.md)
                * [AbstractPhysicalSpace](AbstractPhysicalSpace.md)
                    * [AbstractOccupiedSpace](AbstractOccupiedSpace.md)
                        * **CityFurniture**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [class](class.md) | 0..1 <br/> [CityFurnitureClassValue](CityFurnitureClassValue.md) | Indicates the specific type of the CityFurniture | direct |
| [function](function.md) | * <br/> [CityFurnitureFunctionValue](CityFurnitureFunctionValue.md) | Specifies the intended purposes of the CityFurniture | direct |
| [usage](usage.md) | * <br/> [CityFurnitureUsageValue](CityFurnitureUsageValue.md) | Specifies the actual uses of the CityFurniture | direct |
| [adeOfCityFurniture](adeOfCityFurniture.md) | * <br/> [ADEOfCityFurniture](ADEOfCityFurniture.md) | Augments the CityFurniture with properties defined in an ADE | direct |
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
| self | citygml:CityFurniture |
| native | citygml:CityFurniture |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CityFurniture
description: CityFurniture is an object or piece of equipment installed in the outdoor
  environment for various purposes. Examples include street signs, traffic signals,
  street lamps, benches, fountains.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractOccupiedSpace
abstract: false
attributes:
  class:
    name: class
    description: Indicates the specific type of the CityFurniture.
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
    range: CityFurnitureClassValue
    required: false
    multivalued: false
  function:
    name: function
    description: Specifies the intended purposes of the CityFurniture.
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
    range: CityFurnitureFunctionValue
    required: false
    multivalued: true
  usage:
    name: usage
    description: Specifies the actual uses of the CityFurniture.
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
    range: CityFurnitureUsageValue
    required: false
    multivalued: true
  adeOfCityFurniture:
    name: adeOfCityFurniture
    description: Augments the CityFurniture with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - CityFurniture
    range: ADEOfCityFurniture
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: CityFurniture
description: CityFurniture is an object or piece of equipment installed in the outdoor
  environment for various purposes. Examples include street signs, traffic signals,
  street lamps, benches, fountains.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractOccupiedSpace
abstract: false
attributes:
  class:
    name: class
    description: Indicates the specific type of the CityFurniture.
    from_schema: https://www.ogc.org/standards/citygml
    alias: class
    owner: CityFurniture
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
    range: CityFurnitureClassValue
    required: false
    multivalued: false
  function:
    name: function
    description: Specifies the intended purposes of the CityFurniture.
    from_schema: https://www.ogc.org/standards/citygml
    alias: function
    owner: CityFurniture
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
    range: CityFurnitureFunctionValue
    required: false
    multivalued: true
  usage:
    name: usage
    description: Specifies the actual uses of the CityFurniture.
    from_schema: https://www.ogc.org/standards/citygml
    alias: usage
    owner: CityFurniture
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
    range: CityFurnitureUsageValue
    required: false
    multivalued: true
  adeOfCityFurniture:
    name: adeOfCityFurniture
    description: Augments the CityFurniture with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfCityFurniture
    owner: CityFurniture
    domain_of:
    - CityFurniture
    range: ADEOfCityFurniture
    required: false
    multivalued: true
  adeOfAbstractOccupiedSpace:
    name: adeOfAbstractOccupiedSpace
    description: Augments AbstractOccupiedSpace with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractOccupiedSpace
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: CityFurniture
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
    owner: CityFurniture
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
    owner: CityFurniture
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>