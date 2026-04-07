

# Class: Road 


_A Road is a transportation space used by vehicles, bicycles and/or pedestrians._





URI: [citygml:Road](https://www.ogc.org/standards/citygml/Road)





```mermaid
 classDiagram
    class Road
    click Road href "../Road/"
      AbstractTransportationSpace <|-- Road
        click AbstractTransportationSpace href "../AbstractTransportationSpace/"
      
      Road : adeOfAbstractCityObject
        
          
    
        
        
        Road --> "*" ADEOfAbstractCityObject : adeOfAbstractCityObject
        click ADEOfAbstractCityObject href "../ADEOfAbstractCityObject/"
    

        
      Road : adeOfAbstractFeature
        
          
    
        
        
        Road --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      Road : adeOfAbstractFeatureWithLifespan
        
          
    
        
        
        Road --> "*" ADEOfAbstractFeatureWithLifespan : adeOfAbstractFeatureWithLifespan
        click ADEOfAbstractFeatureWithLifespan href "../ADEOfAbstractFeatureWithLifespan/"
    

        
      Road : adeOfAbstractPhysicalSpace
        
          
    
        
        
        Road --> "*" ADEOfAbstractPhysicalSpace : adeOfAbstractPhysicalSpace
        click ADEOfAbstractPhysicalSpace href "../ADEOfAbstractPhysicalSpace/"
    

        
      Road : adeOfAbstractSpace
        
          
    
        
        
        Road --> "*" ADEOfAbstractSpace : adeOfAbstractSpace
        click ADEOfAbstractSpace href "../ADEOfAbstractSpace/"
    

        
      Road : adeOfAbstractTransportationSpace
        
          
    
        
        
        Road --> "*" ADEOfAbstractTransportationSpace : adeOfAbstractTransportationSpace
        click ADEOfAbstractTransportationSpace href "../ADEOfAbstractTransportationSpace/"
    

        
      Road : adeOfAbstractUnoccupiedSpace
        
          
    
        
        
        Road --> "*" ADEOfAbstractUnoccupiedSpace : adeOfAbstractUnoccupiedSpace
        click ADEOfAbstractUnoccupiedSpace href "../ADEOfAbstractUnoccupiedSpace/"
    

        
      Road : adeOfRoad
        
          
    
        
        
        Road --> "*" ADEOfRoad : adeOfRoad
        click ADEOfRoad href "../ADEOfRoad/"
    

        
      Road : appearance
        
          
    
        
        
        Road --> "*" AbstractAppearance : appearance
        click AbstractAppearance href "../AbstractAppearance/"
    

        
      Road : area
        
          
    
        
        
        Road --> "*" QualifiedArea : area
        click QualifiedArea href "../QualifiedArea/"
    

        
      Road : auxiliaryTrafficSpace
        
          
    
        
        
        Road --> "*" AuxiliaryTrafficSpace : auxiliaryTrafficSpace
        click AuxiliaryTrafficSpace href "../AuxiliaryTrafficSpace/"
    

        
      Road : boundary
        
          
    
        
        
        Road --> "*" AbstractSpaceBoundary : boundary
        click AbstractSpaceBoundary href "../AbstractSpaceBoundary/"
    

        
      Road : class
        
          
    
        
        
        Road --> "0..1" RoadClassValue : class
        click RoadClassValue href "../RoadClassValue/"
    

        
      Road : creationDate
        
      Road : description
        
      Road : dynamizer
        
          
    
        
        
        Road --> "*" AbstractDynamizer : dynamizer
        click AbstractDynamizer href "../AbstractDynamizer/"
    

        
      Road : externalReference
        
          
    
        
        
        Road --> "*" ExternalReference : externalReference
        click ExternalReference href "../ExternalReference/"
    

        
      Road : featureID
        
          
    
        
        
        Road --> "1" ID : featureID
        click ID href "../ID/"
    

        
      Road : function
        
          
    
        
        
        Road --> "*" RoadFunctionValue : function
        click RoadFunctionValue href "../RoadFunctionValue/"
    

        
      Road : generalizesTo
        
          
    
        
        
        Road --> "*" AbstractCityObject : generalizesTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      Road : genericAttribute
        
          
    
        
        
        Road --> "*" AbstractGenericAttribute : genericAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
    

        
      Road : hole
        
          
    
        
        
        Road --> "*" Hole : hole
        click Hole href "../Hole/"
    

        
      Road : identifier
        
      Road : intersection
        
          
    
        
        
        Road --> "*" Intersection : intersection
        click Intersection href "../Intersection/"
    

        
      Road : lod0MultiCurve
        
      Road : lod0MultiSurface
        
      Road : lod0Point
        
      Road : lod1Solid
        
      Road : lod1TerrainIntersectionCurve
        
      Road : lod2MultiCurve
        
      Road : lod2MultiSurface
        
      Road : lod2Solid
        
      Road : lod2TerrainIntersectionCurve
        
      Road : lod3MultiCurve
        
      Road : lod3MultiSurface
        
      Road : lod3Solid
        
      Road : lod3TerrainIntersectionCurve
        
      Road : marking
        
          
    
        
        
        Road --> "*" Marking : marking
        click Marking href "../Marking/"
    

        
      Road : name
        
      Road : occupancy
        
          
    
        
        
        Road --> "*" Occupancy : occupancy
        click Occupancy href "../Occupancy/"
    

        
      Road : pointCloud
        
          
    
        
        
        Road --> "0..1" AbstractPointCloud : pointCloud
        click AbstractPointCloud href "../AbstractPointCloud/"
    

        
      Road : relatedTo
        
          
    
        
        
        Road --> "*" AbstractCityObject : relatedTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      Road : relativeToTerrain
        
          
    
        
        
        Road --> "0..1" RelativeToTerrain : relativeToTerrain
        click RelativeToTerrain href "../RelativeToTerrain/"
    

        
      Road : relativeToWater
        
          
    
        
        
        Road --> "0..1" RelativeToWater : relativeToWater
        click RelativeToWater href "../RelativeToWater/"
    

        
      Road : section
        
          
    
        
        
        Road --> "*" Section : section
        click Section href "../Section/"
    

        
      Road : spaceType
        
          
    
        
        
        Road --> "0..1" SpaceType : spaceType
        click SpaceType href "../SpaceType/"
    

        
      Road : terminationDate
        
      Road : trafficDirection
        
          
    
        
        
        Road --> "0..1" TrafficDirectionValue : trafficDirection
        click TrafficDirectionValue href "../TrafficDirectionValue/"
    

        
      Road : trafficSpace
        
          
    
        
        
        Road --> "*" TrafficSpace : trafficSpace
        click TrafficSpace href "../TrafficSpace/"
    

        
      Road : usage
        
          
    
        
        
        Road --> "*" RoadUsageValue : usage
        click RoadUsageValue href "../RoadUsageValue/"
    

        
      Road : validFrom
        
      Road : validTo
        
      Road : volume
        
          
    
        
        
        Road --> "*" QualifiedVolume : volume
        click QualifiedVolume href "../QualifiedVolume/"
    

        
      
```





## Inheritance
* [AbstractFeature](AbstractFeature.md)
    * [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md)
        * [AbstractCityObject](AbstractCityObject.md)
            * [AbstractSpace](AbstractSpace.md)
                * [AbstractPhysicalSpace](AbstractPhysicalSpace.md)
                    * [AbstractUnoccupiedSpace](AbstractUnoccupiedSpace.md)
                        * [AbstractTransportationSpace](AbstractTransportationSpace.md)
                            * **Road**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [class](class.md) | 0..1 <br/> [RoadClassValue](RoadClassValue.md) | Indicates the specific type of the Road | direct |
| [function](function.md) | * <br/> [RoadFunctionValue](RoadFunctionValue.md) | Specifies the intended purposes of the Road | direct |
| [usage](usage.md) | * <br/> [RoadUsageValue](RoadUsageValue.md) | Specifies the actual uses of the Road | direct |
| [adeOfRoad](adeOfRoad.md) | * <br/> [ADEOfRoad](ADEOfRoad.md) | Augments the Road with properties defined in an ADE | direct |
| [intersection](intersection.md) | * <br/> [Intersection](Intersection.md) | Relates to the intersections that are part of the Road | direct |
| [section](section.md) | * <br/> [Section](Section.md) | Relates to the sections that are part of the Road | direct |
| [trafficDirection](trafficDirection.md) | 0..1 <br/> [TrafficDirectionValue](TrafficDirectionValue.md) | Indicates the direction of traffic flow relative to the corresponding linear ... | [AbstractTransportationSpace](AbstractTransportationSpace.md) |
| [occupancy](occupancy.md) | * <br/> [Occupancy](Occupancy.md) | Provides information on the residency of persons, vehicles, or other moving f... | [AbstractTransportationSpace](AbstractTransportationSpace.md) |
| [adeOfAbstractTransportationSpace](adeOfAbstractTransportationSpace.md) | * <br/> [ADEOfAbstractTransportationSpace](ADEOfAbstractTransportationSpace.md) | Augments AbstractTransportationSpace with properties defined in an ADE | [AbstractTransportationSpace](AbstractTransportationSpace.md) |
| [auxiliaryTrafficSpace](auxiliaryTrafficSpace.md) | * <br/> [AuxiliaryTrafficSpace](AuxiliaryTrafficSpace.md) | Relates to the auxiliary traffic spaces that are part of the transportation s... | [AbstractTransportationSpace](AbstractTransportationSpace.md) |
| [hole](hole.md) | * <br/> [Hole](Hole.md) | Relates to the holes that are part of the transportation space | [AbstractTransportationSpace](AbstractTransportationSpace.md) |
| [trafficSpace](trafficSpace.md) | * <br/> [TrafficSpace](TrafficSpace.md) | Relates to the traffic spaces that are part of the transportation space | [AbstractTransportationSpace](AbstractTransportationSpace.md) |
| [marking](marking.md) | * <br/> [Marking](Marking.md) | Relates to the markings that are part of the transportation space | [AbstractTransportationSpace](AbstractTransportationSpace.md) |
| [adeOfAbstractUnoccupiedSpace](adeOfAbstractUnoccupiedSpace.md) | * <br/> [ADEOfAbstractUnoccupiedSpace](ADEOfAbstractUnoccupiedSpace.md) | Augments AbstractUnoccupiedSpace with properties defined in an ADE | [AbstractUnoccupiedSpace](AbstractUnoccupiedSpace.md) |
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
| self | citygml:Road |
| native | citygml:Road |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Road
description: A Road is a transportation space used by vehicles, bicycles and/or pedestrians.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractTransportationSpace
abstract: false
attributes:
  class:
    name: class
    description: Indicates the specific type of the Road.
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
    range: RoadClassValue
    required: false
    multivalued: false
  function:
    name: function
    description: Specifies the intended purposes of the Road.
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
    range: RoadFunctionValue
    required: false
    multivalued: true
  usage:
    name: usage
    description: Specifies the actual uses of the Road.
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
    range: RoadUsageValue
    required: false
    multivalued: true
  adeOfRoad:
    name: adeOfRoad
    description: Augments the Road with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - Road
    range: ADEOfRoad
    required: false
    multivalued: true
  intersection:
    name: intersection
    description: Relates to the intersections that are part of the Road.
    from_schema: https://www.ogc.org/standards/citygml
    domain_of:
    - Railway
    - Road
    - Track
    - Waterway
    range: Intersection
    required: false
    multivalued: true
  section:
    name: section
    description: Relates to the sections that are part of the Road.
    from_schema: https://www.ogc.org/standards/citygml
    domain_of:
    - Railway
    - Road
    - Track
    - Waterway
    range: Section
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: Road
description: A Road is a transportation space used by vehicles, bicycles and/or pedestrians.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractTransportationSpace
abstract: false
attributes:
  class:
    name: class
    description: Indicates the specific type of the Road.
    from_schema: https://www.ogc.org/standards/citygml
    alias: class
    owner: Road
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
    range: RoadClassValue
    required: false
    multivalued: false
  function:
    name: function
    description: Specifies the intended purposes of the Road.
    from_schema: https://www.ogc.org/standards/citygml
    alias: function
    owner: Road
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
    range: RoadFunctionValue
    required: false
    multivalued: true
  usage:
    name: usage
    description: Specifies the actual uses of the Road.
    from_schema: https://www.ogc.org/standards/citygml
    alias: usage
    owner: Road
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
    range: RoadUsageValue
    required: false
    multivalued: true
  adeOfRoad:
    name: adeOfRoad
    description: Augments the Road with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfRoad
    owner: Road
    domain_of:
    - Road
    range: ADEOfRoad
    required: false
    multivalued: true
  intersection:
    name: intersection
    description: Relates to the intersections that are part of the Road.
    from_schema: https://www.ogc.org/standards/citygml
    alias: intersection
    owner: Road
    domain_of:
    - Railway
    - Road
    - Track
    - Waterway
    range: Intersection
    required: false
    multivalued: true
  section:
    name: section
    description: Relates to the sections that are part of the Road.
    from_schema: https://www.ogc.org/standards/citygml
    alias: section
    owner: Road
    domain_of:
    - Railway
    - Road
    - Track
    - Waterway
    range: Section
    required: false
    multivalued: true
  trafficDirection:
    name: trafficDirection
    description: Indicates the direction of traffic flow relative to the corresponding
      linear geometry representation.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: trafficDirection
    owner: Road
    domain_of:
    - AbstractTransportationSpace
    - TrafficSpace
    range: TrafficDirectionValue
    required: false
    multivalued: false
  occupancy:
    name: occupancy
    description: Provides information on the residency of persons, vehicles, or other
      moving features in the transportation space.
    from_schema: https://www.ogc.org/standards/citygml
    alias: occupancy
    owner: Road
    domain_of:
    - AbstractConstruction
    - AbstractTransportationSpace
    - TrafficSpace
    range: Occupancy
    required: false
    multivalued: true
  adeOfAbstractTransportationSpace:
    name: adeOfAbstractTransportationSpace
    description: Augments AbstractTransportationSpace with properties defined in an
      ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractTransportationSpace
    owner: Road
    domain_of:
    - AbstractTransportationSpace
    range: ADEOfAbstractTransportationSpace
    required: false
    multivalued: true
  auxiliaryTrafficSpace:
    name: auxiliaryTrafficSpace
    description: Relates to the auxiliary traffic spaces that are part of the transportation
      space.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: auxiliaryTrafficSpace
    owner: Road
    domain_of:
    - AbstractTransportationSpace
    range: AuxiliaryTrafficSpace
    required: false
    multivalued: true
  hole:
    name: hole
    description: Relates to the holes that are part of the transportation space.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: hole
    owner: Road
    domain_of:
    - AbstractTransportationSpace
    range: Hole
    required: false
    multivalued: true
  trafficSpace:
    name: trafficSpace
    description: Relates to the traffic spaces that are part of the transportation
      space.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: trafficSpace
    owner: Road
    domain_of:
    - AbstractTransportationSpace
    range: TrafficSpace
    required: false
    multivalued: true
  marking:
    name: marking
    description: Relates to the markings that are part of the transportation space.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: marking
    owner: Road
    domain_of:
    - AbstractTransportationSpace
    range: Marking
    required: false
    multivalued: true
  adeOfAbstractUnoccupiedSpace:
    name: adeOfAbstractUnoccupiedSpace
    description: Augments AbstractUnoccupiedSpace with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractUnoccupiedSpace
    owner: Road
    domain_of:
    - AbstractUnoccupiedSpace
    range: ADEOfAbstractUnoccupiedSpace
    required: false
    multivalued: true
  adeOfAbstractPhysicalSpace:
    name: adeOfAbstractPhysicalSpace
    description: Augments AbstractPhysicalSpace with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractPhysicalSpace
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
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
    owner: Road
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: Road
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
    owner: Road
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
    owner: Road
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>