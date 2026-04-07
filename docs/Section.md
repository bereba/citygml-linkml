

# Class: Section 


_A Section is a transportation space that is a segment of a Road, Railway, Track, or Waterway._





URI: [citygml:Section](https://www.ogc.org/standards/citygml/Section)





```mermaid
 classDiagram
    class Section
    click Section href "../Section/"
      AbstractTransportationSpace <|-- Section
        click AbstractTransportationSpace href "../AbstractTransportationSpace/"
      
      Section : adeOfAbstractCityObject
        
          
    
        
        
        Section --> "*" ADEOfAbstractCityObject : adeOfAbstractCityObject
        click ADEOfAbstractCityObject href "../ADEOfAbstractCityObject/"
    

        
      Section : adeOfAbstractFeature
        
          
    
        
        
        Section --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      Section : adeOfAbstractFeatureWithLifespan
        
          
    
        
        
        Section --> "*" ADEOfAbstractFeatureWithLifespan : adeOfAbstractFeatureWithLifespan
        click ADEOfAbstractFeatureWithLifespan href "../ADEOfAbstractFeatureWithLifespan/"
    

        
      Section : adeOfAbstractPhysicalSpace
        
          
    
        
        
        Section --> "*" ADEOfAbstractPhysicalSpace : adeOfAbstractPhysicalSpace
        click ADEOfAbstractPhysicalSpace href "../ADEOfAbstractPhysicalSpace/"
    

        
      Section : adeOfAbstractSpace
        
          
    
        
        
        Section --> "*" ADEOfAbstractSpace : adeOfAbstractSpace
        click ADEOfAbstractSpace href "../ADEOfAbstractSpace/"
    

        
      Section : adeOfAbstractTransportationSpace
        
          
    
        
        
        Section --> "*" ADEOfAbstractTransportationSpace : adeOfAbstractTransportationSpace
        click ADEOfAbstractTransportationSpace href "../ADEOfAbstractTransportationSpace/"
    

        
      Section : adeOfAbstractUnoccupiedSpace
        
          
    
        
        
        Section --> "*" ADEOfAbstractUnoccupiedSpace : adeOfAbstractUnoccupiedSpace
        click ADEOfAbstractUnoccupiedSpace href "../ADEOfAbstractUnoccupiedSpace/"
    

        
      Section : adeOfSection
        
          
    
        
        
        Section --> "*" ADEOfSection : adeOfSection
        click ADEOfSection href "../ADEOfSection/"
    

        
      Section : appearance
        
          
    
        
        
        Section --> "*" AbstractAppearance : appearance
        click AbstractAppearance href "../AbstractAppearance/"
    

        
      Section : area
        
          
    
        
        
        Section --> "*" QualifiedArea : area
        click QualifiedArea href "../QualifiedArea/"
    

        
      Section : auxiliaryTrafficSpace
        
          
    
        
        
        Section --> "*" AuxiliaryTrafficSpace : auxiliaryTrafficSpace
        click AuxiliaryTrafficSpace href "../AuxiliaryTrafficSpace/"
    

        
      Section : boundary
        
          
    
        
        
        Section --> "*" AbstractSpaceBoundary : boundary
        click AbstractSpaceBoundary href "../AbstractSpaceBoundary/"
    

        
      Section : class
        
          
    
        
        
        Section --> "0..1" SectionClassValue : class
        click SectionClassValue href "../SectionClassValue/"
    

        
      Section : creationDate
        
      Section : description
        
      Section : dynamizer
        
          
    
        
        
        Section --> "*" AbstractDynamizer : dynamizer
        click AbstractDynamizer href "../AbstractDynamizer/"
    

        
      Section : externalReference
        
          
    
        
        
        Section --> "*" ExternalReference : externalReference
        click ExternalReference href "../ExternalReference/"
    

        
      Section : featureID
        
          
    
        
        
        Section --> "1" ID : featureID
        click ID href "../ID/"
    

        
      Section : generalizesTo
        
          
    
        
        
        Section --> "*" AbstractCityObject : generalizesTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      Section : genericAttribute
        
          
    
        
        
        Section --> "*" AbstractGenericAttribute : genericAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
    

        
      Section : hole
        
          
    
        
        
        Section --> "*" Hole : hole
        click Hole href "../Hole/"
    

        
      Section : identifier
        
      Section : lod0MultiCurve
        
      Section : lod0MultiSurface
        
      Section : lod0Point
        
      Section : lod1Solid
        
      Section : lod1TerrainIntersectionCurve
        
      Section : lod2MultiCurve
        
      Section : lod2MultiSurface
        
      Section : lod2Solid
        
      Section : lod2TerrainIntersectionCurve
        
      Section : lod3MultiCurve
        
      Section : lod3MultiSurface
        
      Section : lod3Solid
        
      Section : lod3TerrainIntersectionCurve
        
      Section : marking
        
          
    
        
        
        Section --> "*" Marking : marking
        click Marking href "../Marking/"
    

        
      Section : name
        
      Section : occupancy
        
          
    
        
        
        Section --> "*" Occupancy : occupancy
        click Occupancy href "../Occupancy/"
    

        
      Section : pointCloud
        
          
    
        
        
        Section --> "0..1" AbstractPointCloud : pointCloud
        click AbstractPointCloud href "../AbstractPointCloud/"
    

        
      Section : relatedTo
        
          
    
        
        
        Section --> "*" AbstractCityObject : relatedTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      Section : relativeToTerrain
        
          
    
        
        
        Section --> "0..1" RelativeToTerrain : relativeToTerrain
        click RelativeToTerrain href "../RelativeToTerrain/"
    

        
      Section : relativeToWater
        
          
    
        
        
        Section --> "0..1" RelativeToWater : relativeToWater
        click RelativeToWater href "../RelativeToWater/"
    

        
      Section : spaceType
        
          
    
        
        
        Section --> "0..1" SpaceType : spaceType
        click SpaceType href "../SpaceType/"
    

        
      Section : terminationDate
        
      Section : trafficDirection
        
          
    
        
        
        Section --> "0..1" TrafficDirectionValue : trafficDirection
        click TrafficDirectionValue href "../TrafficDirectionValue/"
    

        
      Section : trafficSpace
        
          
    
        
        
        Section --> "*" TrafficSpace : trafficSpace
        click TrafficSpace href "../TrafficSpace/"
    

        
      Section : validFrom
        
      Section : validTo
        
      Section : volume
        
          
    
        
        
        Section --> "*" QualifiedVolume : volume
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
                            * **Section**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [class](class.md) | 0..1 <br/> [SectionClassValue](SectionClassValue.md) | Indicates the specific type of the Section | direct |
| [adeOfSection](adeOfSection.md) | * <br/> [ADEOfSection](ADEOfSection.md) | Augments the Section with properties defined in an ADE | direct |
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





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Railway](Railway.md) | [section](section.md) | range | [Section](Section.md) |
| [Road](Road.md) | [section](section.md) | range | [Section](Section.md) |
| [Track](Track.md) | [section](section.md) | range | [Section](Section.md) |
| [Waterway](Waterway.md) | [section](section.md) | range | [Section](Section.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:Section |
| native | citygml:Section |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Section
description: A Section is a transportation space that is a segment of a Road, Railway,
  Track, or Waterway.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractTransportationSpace
abstract: false
attributes:
  class:
    name: class
    description: Indicates the specific type of the Section.
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
    range: SectionClassValue
    required: false
    multivalued: false
  adeOfSection:
    name: adeOfSection
    description: Augments the Section with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - Section
    range: ADEOfSection
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: Section
description: A Section is a transportation space that is a segment of a Road, Railway,
  Track, or Waterway.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractTransportationSpace
abstract: false
attributes:
  class:
    name: class
    description: Indicates the specific type of the Section.
    from_schema: https://www.ogc.org/standards/citygml
    alias: class
    owner: Section
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
    range: SectionClassValue
    required: false
    multivalued: false
  adeOfSection:
    name: adeOfSection
    description: Augments the Section with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfSection
    owner: Section
    domain_of:
    - Section
    range: ADEOfSection
    required: false
    multivalued: true
  trafficDirection:
    name: trafficDirection
    description: Indicates the direction of traffic flow relative to the corresponding
      linear geometry representation.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: trafficDirection
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
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
    owner: Section
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: Section
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
    owner: Section
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
    owner: Section
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>