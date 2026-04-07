

# Class: DoorSurface 


_A DoorSurface is either a boundary surface of a Door feature or a surface that seals an opening filled by a door._





URI: [citygml:DoorSurface](https://www.ogc.org/standards/citygml/DoorSurface)





```mermaid
 classDiagram
    class DoorSurface
    click DoorSurface href "../DoorSurface/"
      AbstractFillingSurface <|-- DoorSurface
        click AbstractFillingSurface href "../AbstractFillingSurface/"
      
      DoorSurface : address
        
          
    
        
        
        DoorSurface --> "*" Address : address
        click Address href "../Address/"
    

        
      DoorSurface : adeOfAbstractCityObject
        
          
    
        
        
        DoorSurface --> "*" ADEOfAbstractCityObject : adeOfAbstractCityObject
        click ADEOfAbstractCityObject href "../ADEOfAbstractCityObject/"
    

        
      DoorSurface : adeOfAbstractFeature
        
          
    
        
        
        DoorSurface --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      DoorSurface : adeOfAbstractFeatureWithLifespan
        
          
    
        
        
        DoorSurface --> "*" ADEOfAbstractFeatureWithLifespan : adeOfAbstractFeatureWithLifespan
        click ADEOfAbstractFeatureWithLifespan href "../ADEOfAbstractFeatureWithLifespan/"
    

        
      DoorSurface : adeOfAbstractFillingSurface
        
          
    
        
        
        DoorSurface --> "*" ADEOfAbstractFillingSurface : adeOfAbstractFillingSurface
        click ADEOfAbstractFillingSurface href "../ADEOfAbstractFillingSurface/"
    

        
      DoorSurface : adeOfAbstractSpaceBoundary
        
          
    
        
        
        DoorSurface --> "*" ADEOfAbstractSpaceBoundary : adeOfAbstractSpaceBoundary
        click ADEOfAbstractSpaceBoundary href "../ADEOfAbstractSpaceBoundary/"
    

        
      DoorSurface : adeOfAbstractThematicSurface
        
          
    
        
        
        DoorSurface --> "*" ADEOfAbstractThematicSurface : adeOfAbstractThematicSurface
        click ADEOfAbstractThematicSurface href "../ADEOfAbstractThematicSurface/"
    

        
      DoorSurface : adeOfDoorSurface
        
          
    
        
        
        DoorSurface --> "*" ADEOfDoorSurface : adeOfDoorSurface
        click ADEOfDoorSurface href "../ADEOfDoorSurface/"
    

        
      DoorSurface : appearance
        
          
    
        
        
        DoorSurface --> "*" AbstractAppearance : appearance
        click AbstractAppearance href "../AbstractAppearance/"
    

        
      DoorSurface : area
        
          
    
        
        
        DoorSurface --> "*" QualifiedArea : area
        click QualifiedArea href "../QualifiedArea/"
    

        
      DoorSurface : creationDate
        
      DoorSurface : description
        
      DoorSurface : dynamizer
        
          
    
        
        
        DoorSurface --> "*" AbstractDynamizer : dynamizer
        click AbstractDynamizer href "../AbstractDynamizer/"
    

        
      DoorSurface : externalReference
        
          
    
        
        
        DoorSurface --> "*" ExternalReference : externalReference
        click ExternalReference href "../ExternalReference/"
    

        
      DoorSurface : featureID
        
          
    
        
        
        DoorSurface --> "1" ID : featureID
        click ID href "../ID/"
    

        
      DoorSurface : generalizesTo
        
          
    
        
        
        DoorSurface --> "*" AbstractCityObject : generalizesTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      DoorSurface : genericAttribute
        
          
    
        
        
        DoorSurface --> "*" AbstractGenericAttribute : genericAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
    

        
      DoorSurface : identifier
        
      DoorSurface : lod0MultiCurve
        
      DoorSurface : lod0MultiSurface
        
      DoorSurface : lod1MultiSurface
        
      DoorSurface : lod2MultiSurface
        
      DoorSurface : lod3MultiSurface
        
      DoorSurface : name
        
      DoorSurface : pointCloud
        
          
    
        
        
        DoorSurface --> "0..1" AbstractPointCloud : pointCloud
        click AbstractPointCloud href "../AbstractPointCloud/"
    

        
      DoorSurface : relatedTo
        
          
    
        
        
        DoorSurface --> "*" AbstractCityObject : relatedTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      DoorSurface : relativeToTerrain
        
          
    
        
        
        DoorSurface --> "0..1" RelativeToTerrain : relativeToTerrain
        click RelativeToTerrain href "../RelativeToTerrain/"
    

        
      DoorSurface : relativeToWater
        
          
    
        
        
        DoorSurface --> "0..1" RelativeToWater : relativeToWater
        click RelativeToWater href "../RelativeToWater/"
    

        
      DoorSurface : terminationDate
        
      DoorSurface : validFrom
        
      DoorSurface : validTo
        
      
```





## Inheritance
* [AbstractFeature](AbstractFeature.md)
    * [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md)
        * [AbstractCityObject](AbstractCityObject.md)
            * [AbstractSpaceBoundary](AbstractSpaceBoundary.md)
                * [AbstractThematicSurface](AbstractThematicSurface.md)
                    * [AbstractFillingSurface](AbstractFillingSurface.md)
                        * **DoorSurface**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [adeOfDoorSurface](adeOfDoorSurface.md) | * <br/> [ADEOfDoorSurface](ADEOfDoorSurface.md) | Augments the DoorSurface with properties defined in an ADE | direct |
| [address](address.md) | * <br/> [Address](Address.md) | Relates to the addresses that are assigned to the DoorSurface | direct |
| [adeOfAbstractFillingSurface](adeOfAbstractFillingSurface.md) | * <br/> [ADEOfAbstractFillingSurface](ADEOfAbstractFillingSurface.md) | Augments AbstractFillingSurface with properties defined in an ADE | [AbstractFillingSurface](AbstractFillingSurface.md) |
| [area](area.md) | * <br/> [QualifiedArea](QualifiedArea.md) | Specifies qualified areas related to the thematic surface | [AbstractThematicSurface](AbstractThematicSurface.md) |
| [adeOfAbstractThematicSurface](adeOfAbstractThematicSurface.md) | * <br/> [ADEOfAbstractThematicSurface](ADEOfAbstractThematicSurface.md) | Augments AbstractThematicSurface with properties defined in an ADE | [AbstractThematicSurface](AbstractThematicSurface.md) |
| [lod3MultiSurface](lod3MultiSurface.md) | 0..1 <br/> [String](String.md) | Relates to a 3D MultiSurface geometry that represents the thematic surface in... | [AbstractThematicSurface](AbstractThematicSurface.md) |
| [lod2MultiSurface](lod2MultiSurface.md) | 0..1 <br/> [String](String.md) | Relates to a 3D MultiSurface geometry that represents the thematic surface in... | [AbstractThematicSurface](AbstractThematicSurface.md) |
| [pointCloud](pointCloud.md) | 0..1 <br/> [AbstractPointCloud](AbstractPointCloud.md) | Relates to a 3D PointCloud that represents the thematic surface | [AbstractThematicSurface](AbstractThematicSurface.md) |
| [lod0MultiCurve](lod0MultiCurve.md) | 0..1 <br/> [String](String.md) | Relates to a 3D MultiCurve geometry that represents the thematic surface in L... | [AbstractThematicSurface](AbstractThematicSurface.md) |
| [lod0MultiSurface](lod0MultiSurface.md) | 0..1 <br/> [String](String.md) | Relates to a 3D MultiSurface geometry that represents the thematic surface in... | [AbstractThematicSurface](AbstractThematicSurface.md) |
| [lod1MultiSurface](lod1MultiSurface.md) | 0..1 <br/> [String](String.md) | Relates to a 3D MultiSurface geometry that represents the thematic surface in... | [AbstractThematicSurface](AbstractThematicSurface.md) |
| [adeOfAbstractSpaceBoundary](adeOfAbstractSpaceBoundary.md) | * <br/> [ADEOfAbstractSpaceBoundary](ADEOfAbstractSpaceBoundary.md) | Augments AbstractSpaceBoundary with properties defined in an ADE | [AbstractSpaceBoundary](AbstractSpaceBoundary.md) |
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
| [Door](Door.md) | [boundary](boundary.md) | range | [DoorSurface](DoorSurface.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:DoorSurface |
| native | citygml:DoorSurface |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DoorSurface
description: A DoorSurface is either a boundary surface of a Door feature or a surface
  that seals an opening filled by a door.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractFillingSurface
abstract: false
attributes:
  adeOfDoorSurface:
    name: adeOfDoorSurface
    description: Augments the DoorSurface with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - DoorSurface
    range: ADEOfDoorSurface
    required: false
    multivalued: true
  address:
    name: address
    description: Relates to the addresses that are assigned to the DoorSurface.
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

```
</details>

### Induced

<details>
```yaml
name: DoorSurface
description: A DoorSurface is either a boundary surface of a Door feature or a surface
  that seals an opening filled by a door.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractFillingSurface
abstract: false
attributes:
  adeOfDoorSurface:
    name: adeOfDoorSurface
    description: Augments the DoorSurface with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfDoorSurface
    owner: DoorSurface
    domain_of:
    - DoorSurface
    range: ADEOfDoorSurface
    required: false
    multivalued: true
  address:
    name: address
    description: Relates to the addresses that are assigned to the DoorSurface.
    from_schema: https://www.ogc.org/standards/citygml
    alias: address
    owner: DoorSurface
    domain_of:
    - Door
    - DoorSurface
    - AbstractBridge
    - AbstractBuilding
    - BuildingUnit
    range: Address
    required: false
    multivalued: true
  adeOfAbstractFillingSurface:
    name: adeOfAbstractFillingSurface
    description: Augments AbstractFillingSurface with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractFillingSurface
    owner: DoorSurface
    domain_of:
    - AbstractFillingSurface
    range: ADEOfAbstractFillingSurface
    required: false
    multivalued: true
  area:
    name: area
    description: Specifies qualified areas related to the thematic surface.
    from_schema: https://www.ogc.org/standards/citygml
    alias: area
    owner: DoorSurface
    domain_of:
    - QualifiedArea
    - AbstractSpace
    - AbstractThematicSurface
    range: QualifiedArea
    required: false
    multivalued: true
  adeOfAbstractThematicSurface:
    name: adeOfAbstractThematicSurface
    description: Augments AbstractThematicSurface with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractThematicSurface
    owner: DoorSurface
    domain_of:
    - AbstractThematicSurface
    range: ADEOfAbstractThematicSurface
    required: false
    multivalued: true
  lod3MultiSurface:
    name: lod3MultiSurface
    description: Relates to a 3D MultiSurface geometry that represents the thematic
      surface in Level of Detail 3.
    from_schema: https://www.ogc.org/standards/citygml
    alias: lod3MultiSurface
    owner: DoorSurface
    domain_of:
    - AbstractSpace
    - AbstractThematicSurface
    range: string
    required: false
    multivalued: false
  lod2MultiSurface:
    name: lod2MultiSurface
    description: Relates to a 3D MultiSurface geometry that represents the thematic
      surface in Level of Detail 2.
    from_schema: https://www.ogc.org/standards/citygml
    alias: lod2MultiSurface
    owner: DoorSurface
    domain_of:
    - AbstractSpace
    - AbstractThematicSurface
    range: string
    required: false
    multivalued: false
  pointCloud:
    name: pointCloud
    description: Relates to a 3D PointCloud that represents the thematic surface.
    from_schema: https://www.ogc.org/standards/citygml
    alias: pointCloud
    owner: DoorSurface
    domain_of:
    - AbstractPhysicalSpace
    - AbstractThematicSurface
    - MassPointRelief
    range: AbstractPointCloud
    required: false
    multivalued: false
  lod0MultiCurve:
    name: lod0MultiCurve
    description: Relates to a 3D MultiCurve geometry that represents the thematic
      surface in Level of Detail 0.
    from_schema: https://www.ogc.org/standards/citygml
    alias: lod0MultiCurve
    owner: DoorSurface
    domain_of:
    - AbstractSpace
    - AbstractThematicSurface
    range: string
    required: false
    multivalued: false
  lod0MultiSurface:
    name: lod0MultiSurface
    description: Relates to a 3D MultiSurface geometry that represents the thematic
      surface in Level of Detail 0.
    from_schema: https://www.ogc.org/standards/citygml
    alias: lod0MultiSurface
    owner: DoorSurface
    domain_of:
    - AbstractSpace
    - AbstractThematicSurface
    range: string
    required: false
    multivalued: false
  lod1MultiSurface:
    name: lod1MultiSurface
    description: Relates to a 3D MultiSurface geometry that represents the thematic
      surface in Level of Detail 1.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod1MultiSurface
    owner: DoorSurface
    domain_of:
    - AbstractThematicSurface
    range: string
    required: false
    multivalued: false
  adeOfAbstractSpaceBoundary:
    name: adeOfAbstractSpaceBoundary
    description: Augments AbstractSpaceBoundary with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractSpaceBoundary
    owner: DoorSurface
    domain_of:
    - AbstractSpaceBoundary
    range: ADEOfAbstractSpaceBoundary
    required: false
    multivalued: true
  relativeToTerrain:
    name: relativeToTerrain
    description: Describes the vertical position of the city object relative to the
      surrounding terrain.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: relativeToTerrain
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: DoorSurface
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
    owner: DoorSurface
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
    owner: DoorSurface
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>