

# Class: Tunnel 


_A Tunnel represents a horizontal or sloping enclosed passage way of a certain length, mainly underground or underwater. [cf. ISO 6707-1]_





URI: [citygml:Tunnel](https://www.ogc.org/standards/citygml/Tunnel)





```mermaid
 classDiagram
    class Tunnel
    click Tunnel href "../Tunnel/"
      AbstractTunnel <|-- Tunnel
        click AbstractTunnel href "../AbstractTunnel/"
      
      Tunnel : adeOfAbstractCityObject
        
          
    
        
        
        Tunnel --> "*" ADEOfAbstractCityObject : adeOfAbstractCityObject
        click ADEOfAbstractCityObject href "../ADEOfAbstractCityObject/"
    

        
      Tunnel : adeOfAbstractConstruction
        
          
    
        
        
        Tunnel --> "*" ADEOfAbstractConstruction : adeOfAbstractConstruction
        click ADEOfAbstractConstruction href "../ADEOfAbstractConstruction/"
    

        
      Tunnel : adeOfAbstractFeature
        
          
    
        
        
        Tunnel --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      Tunnel : adeOfAbstractFeatureWithLifespan
        
          
    
        
        
        Tunnel --> "*" ADEOfAbstractFeatureWithLifespan : adeOfAbstractFeatureWithLifespan
        click ADEOfAbstractFeatureWithLifespan href "../ADEOfAbstractFeatureWithLifespan/"
    

        
      Tunnel : adeOfAbstractOccupiedSpace
        
          
    
        
        
        Tunnel --> "*" ADEOfAbstractOccupiedSpace : adeOfAbstractOccupiedSpace
        click ADEOfAbstractOccupiedSpace href "../ADEOfAbstractOccupiedSpace/"
    

        
      Tunnel : adeOfAbstractPhysicalSpace
        
          
    
        
        
        Tunnel --> "*" ADEOfAbstractPhysicalSpace : adeOfAbstractPhysicalSpace
        click ADEOfAbstractPhysicalSpace href "../ADEOfAbstractPhysicalSpace/"
    

        
      Tunnel : adeOfAbstractSpace
        
          
    
        
        
        Tunnel --> "*" ADEOfAbstractSpace : adeOfAbstractSpace
        click ADEOfAbstractSpace href "../ADEOfAbstractSpace/"
    

        
      Tunnel : adeOfAbstractTunnel
        
          
    
        
        
        Tunnel --> "*" ADEOfAbstractTunnel : adeOfAbstractTunnel
        click ADEOfAbstractTunnel href "../ADEOfAbstractTunnel/"
    

        
      Tunnel : adeOfTunnel
        
          
    
        
        
        Tunnel --> "*" ADEOfTunnel : adeOfTunnel
        click ADEOfTunnel href "../ADEOfTunnel/"
    

        
      Tunnel : appearance
        
          
    
        
        
        Tunnel --> "*" AbstractAppearance : appearance
        click AbstractAppearance href "../AbstractAppearance/"
    

        
      Tunnel : area
        
          
    
        
        
        Tunnel --> "*" QualifiedArea : area
        click QualifiedArea href "../QualifiedArea/"
    

        
      Tunnel : boundary
        
          
    
        
        
        Tunnel --> "*" AbstractThematicSurface : boundary
        click AbstractThematicSurface href "../AbstractThematicSurface/"
    

        
      Tunnel : class
        
          
    
        
        
        Tunnel --> "0..1" TunnelClassValue : class
        click TunnelClassValue href "../TunnelClassValue/"
    

        
      Tunnel : conditionOfConstruction
        
          
    
        
        
        Tunnel --> "0..1" ConditionOfConstructionValue : conditionOfConstruction
        click ConditionOfConstructionValue href "../ConditionOfConstructionValue/"
    

        
      Tunnel : constructionEvent
        
          
    
        
        
        Tunnel --> "*" ConstructionEvent : constructionEvent
        click ConstructionEvent href "../ConstructionEvent/"
    

        
      Tunnel : creationDate
        
      Tunnel : dateOfConstruction
        
      Tunnel : dateOfDemolition
        
      Tunnel : description
        
      Tunnel : dynamizer
        
          
    
        
        
        Tunnel --> "*" AbstractDynamizer : dynamizer
        click AbstractDynamizer href "../AbstractDynamizer/"
    

        
      Tunnel : elevation
        
          
    
        
        
        Tunnel --> "*" Elevation : elevation
        click Elevation href "../Elevation/"
    

        
      Tunnel : externalReference
        
          
    
        
        
        Tunnel --> "*" ExternalReference : externalReference
        click ExternalReference href "../ExternalReference/"
    

        
      Tunnel : featureID
        
          
    
        
        
        Tunnel --> "1" ID : featureID
        click ID href "../ID/"
    

        
      Tunnel : function
        
          
    
        
        
        Tunnel --> "*" TunnelFunctionValue : function
        click TunnelFunctionValue href "../TunnelFunctionValue/"
    

        
      Tunnel : generalizesTo
        
          
    
        
        
        Tunnel --> "*" AbstractCityObject : generalizesTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      Tunnel : genericAttribute
        
          
    
        
        
        Tunnel --> "*" AbstractGenericAttribute : genericAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
    

        
      Tunnel : height
        
          
    
        
        
        Tunnel --> "*" Height : height
        click Height href "../Height/"
    

        
      Tunnel : hollowSpace
        
          
    
        
        
        Tunnel --> "*" HollowSpace : hollowSpace
        click HollowSpace href "../HollowSpace/"
    

        
      Tunnel : identifier
        
      Tunnel : lod0MultiCurve
        
      Tunnel : lod0MultiSurface
        
      Tunnel : lod0Point
        
      Tunnel : lod1ImplicitRepresentation
        
          
    
        
        
        Tunnel --> "0..1" ImplicitGeometry : lod1ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      Tunnel : lod1Solid
        
      Tunnel : lod1TerrainIntersectionCurve
        
      Tunnel : lod2ImplicitRepresentation
        
          
    
        
        
        Tunnel --> "0..1" ImplicitGeometry : lod2ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      Tunnel : lod2MultiCurve
        
      Tunnel : lod2MultiSurface
        
      Tunnel : lod2Solid
        
      Tunnel : lod2TerrainIntersectionCurve
        
      Tunnel : lod3ImplicitRepresentation
        
          
    
        
        
        Tunnel --> "0..1" ImplicitGeometry : lod3ImplicitRepresentation
        click ImplicitGeometry href "../ImplicitGeometry/"
    

        
      Tunnel : lod3MultiCurve
        
      Tunnel : lod3MultiSurface
        
      Tunnel : lod3Solid
        
      Tunnel : lod3TerrainIntersectionCurve
        
      Tunnel : name
        
      Tunnel : occupancy
        
          
    
        
        
        Tunnel --> "*" Occupancy : occupancy
        click Occupancy href "../Occupancy/"
    

        
      Tunnel : pointCloud
        
          
    
        
        
        Tunnel --> "0..1" AbstractPointCloud : pointCloud
        click AbstractPointCloud href "../AbstractPointCloud/"
    

        
      Tunnel : relatedTo
        
          
    
        
        
        Tunnel --> "*" AbstractCityObject : relatedTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      Tunnel : relativeToTerrain
        
          
    
        
        
        Tunnel --> "0..1" RelativeToTerrain : relativeToTerrain
        click RelativeToTerrain href "../RelativeToTerrain/"
    

        
      Tunnel : relativeToWater
        
          
    
        
        
        Tunnel --> "0..1" RelativeToWater : relativeToWater
        click RelativeToWater href "../RelativeToWater/"
    

        
      Tunnel : spaceType
        
          
    
        
        
        Tunnel --> "0..1" SpaceType : spaceType
        click SpaceType href "../SpaceType/"
    

        
      Tunnel : terminationDate
        
      Tunnel : tunnelConstructiveElement
        
          
    
        
        
        Tunnel --> "*" TunnelConstructiveElement : tunnelConstructiveElement
        click TunnelConstructiveElement href "../TunnelConstructiveElement/"
    

        
      Tunnel : tunnelFurniture
        
          
    
        
        
        Tunnel --> "*" TunnelFurniture : tunnelFurniture
        click TunnelFurniture href "../TunnelFurniture/"
    

        
      Tunnel : tunnelInstallation
        
          
    
        
        
        Tunnel --> "*" TunnelInstallation : tunnelInstallation
        click TunnelInstallation href "../TunnelInstallation/"
    

        
      Tunnel : tunnelPart
        
          
    
        
        
        Tunnel --> "*" TunnelPart : tunnelPart
        click TunnelPart href "../TunnelPart/"
    

        
      Tunnel : usage
        
          
    
        
        
        Tunnel --> "*" TunnelUsageValue : usage
        click TunnelUsageValue href "../TunnelUsageValue/"
    

        
      Tunnel : validFrom
        
      Tunnel : validTo
        
      Tunnel : volume
        
          
    
        
        
        Tunnel --> "*" QualifiedVolume : volume
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
                            * [AbstractTunnel](AbstractTunnel.md)
                                * **Tunnel**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [adeOfTunnel](adeOfTunnel.md) | * <br/> [ADEOfTunnel](ADEOfTunnel.md) | Augments the Tunnel with properties defined in an ADE | direct |
| [tunnelPart](tunnelPart.md) | * <br/> [TunnelPart](TunnelPart.md) | Relates the tunnel parts to the Tunnel | direct |
| [class](class.md) | 0..1 <br/> [TunnelClassValue](TunnelClassValue.md) | Indicates the specific type of the Tunnel or TunnelPart | [AbstractTunnel](AbstractTunnel.md) |
| [function](function.md) | * <br/> [TunnelFunctionValue](TunnelFunctionValue.md) | Specifies the intended purposes of the Tunnel or TunnelPart | [AbstractTunnel](AbstractTunnel.md) |
| [usage](usage.md) | * <br/> [TunnelUsageValue](TunnelUsageValue.md) | Specifies the actual uses of the Tunnel or TunnelPart | [AbstractTunnel](AbstractTunnel.md) |
| [adeOfAbstractTunnel](adeOfAbstractTunnel.md) | * <br/> [ADEOfAbstractTunnel](ADEOfAbstractTunnel.md) | Augments AbstractTunnel with properties defined in an ADE | [AbstractTunnel](AbstractTunnel.md) |
| [tunnelConstructiveElement](tunnelConstructiveElement.md) | * <br/> [TunnelConstructiveElement](TunnelConstructiveElement.md) | Relates the constructive elements to the Tunnel or TunnelPart | [AbstractTunnel](AbstractTunnel.md) |
| [tunnelFurniture](tunnelFurniture.md) | * <br/> [TunnelFurniture](TunnelFurniture.md) | Relates the furniture objects to the Tunnel or TunnelPart | [AbstractTunnel](AbstractTunnel.md) |
| [tunnelInstallation](tunnelInstallation.md) | * <br/> [TunnelInstallation](TunnelInstallation.md) | Relates the installation objects to the Tunnel or TunnelPart | [AbstractTunnel](AbstractTunnel.md) |
| [hollowSpace](hollowSpace.md) | * <br/> [HollowSpace](HollowSpace.md) | Relates the hollow spaces to the Tunnel or TunnelPart | [AbstractTunnel](AbstractTunnel.md) |
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
| self | citygml:Tunnel |
| native | citygml:Tunnel |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Tunnel
description: A Tunnel represents a horizontal or sloping enclosed passage way of a
  certain length, mainly underground or underwater. [cf. ISO 6707-1]
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractTunnel
abstract: false
attributes:
  adeOfTunnel:
    name: adeOfTunnel
    description: Augments the Tunnel with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - Tunnel
    range: ADEOfTunnel
    required: false
    multivalued: true
  tunnelPart:
    name: tunnelPart
    description: Relates the tunnel parts to the Tunnel.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - Tunnel
    range: TunnelPart
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: Tunnel
description: A Tunnel represents a horizontal or sloping enclosed passage way of a
  certain length, mainly underground or underwater. [cf. ISO 6707-1]
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractTunnel
abstract: false
attributes:
  adeOfTunnel:
    name: adeOfTunnel
    description: Augments the Tunnel with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfTunnel
    owner: Tunnel
    domain_of:
    - Tunnel
    range: ADEOfTunnel
    required: false
    multivalued: true
  tunnelPart:
    name: tunnelPart
    description: Relates the tunnel parts to the Tunnel.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: tunnelPart
    owner: Tunnel
    domain_of:
    - Tunnel
    range: TunnelPart
    required: false
    multivalued: true
  class:
    name: class
    description: Indicates the specific type of the Tunnel or TunnelPart.
    from_schema: https://www.ogc.org/standards/citygml
    alias: class
    owner: Tunnel
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
    range: TunnelClassValue
    required: false
    multivalued: false
  function:
    name: function
    description: Specifies the intended purposes of the Tunnel or TunnelPart.
    from_schema: https://www.ogc.org/standards/citygml
    alias: function
    owner: Tunnel
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
    range: TunnelFunctionValue
    required: false
    multivalued: true
  usage:
    name: usage
    description: Specifies the actual uses of the Tunnel or TunnelPart.
    from_schema: https://www.ogc.org/standards/citygml
    alias: usage
    owner: Tunnel
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
    range: TunnelUsageValue
    required: false
    multivalued: true
  adeOfAbstractTunnel:
    name: adeOfAbstractTunnel
    description: Augments AbstractTunnel with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractTunnel
    owner: Tunnel
    domain_of:
    - AbstractTunnel
    range: ADEOfAbstractTunnel
    required: false
    multivalued: true
  tunnelConstructiveElement:
    name: tunnelConstructiveElement
    description: Relates the constructive elements to the Tunnel or TunnelPart.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: tunnelConstructiveElement
    owner: Tunnel
    domain_of:
    - AbstractTunnel
    range: TunnelConstructiveElement
    required: false
    multivalued: true
  tunnelFurniture:
    name: tunnelFurniture
    description: Relates the furniture objects to the Tunnel or TunnelPart.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: tunnelFurniture
    owner: Tunnel
    domain_of:
    - AbstractTunnel
    - HollowSpace
    range: TunnelFurniture
    required: false
    multivalued: true
  tunnelInstallation:
    name: tunnelInstallation
    description: Relates the installation objects to the Tunnel or TunnelPart.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: tunnelInstallation
    owner: Tunnel
    domain_of:
    - AbstractTunnel
    - HollowSpace
    range: TunnelInstallation
    required: false
    multivalued: true
  hollowSpace:
    name: hollowSpace
    description: Relates the hollow spaces to the Tunnel or TunnelPart.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: hollowSpace
    owner: Tunnel
    domain_of:
    - AbstractTunnel
    range: HollowSpace
    required: false
    multivalued: true
  conditionOfConstruction:
    name: conditionOfConstruction
    description: Indicates the life-cycle status of the construction. [cf. INSPIRE]
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: conditionOfConstruction
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: Tunnel
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
    owner: Tunnel
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
    owner: Tunnel
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>