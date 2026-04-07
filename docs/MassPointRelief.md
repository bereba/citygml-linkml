

# Class: MassPointRelief 


_A MassPointRelief represents a terrain component as a collection of 3D points._





URI: [citygml:MassPointRelief](https://www.ogc.org/standards/citygml/MassPointRelief)





```mermaid
 classDiagram
    class MassPointRelief
    click MassPointRelief href "../MassPointRelief/"
      AbstractReliefComponent <|-- MassPointRelief
        click AbstractReliefComponent href "../AbstractReliefComponent/"
      
      MassPointRelief : adeOfAbstractCityObject
        
          
    
        
        
        MassPointRelief --> "*" ADEOfAbstractCityObject : adeOfAbstractCityObject
        click ADEOfAbstractCityObject href "../ADEOfAbstractCityObject/"
    

        
      MassPointRelief : adeOfAbstractFeature
        
          
    
        
        
        MassPointRelief --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      MassPointRelief : adeOfAbstractFeatureWithLifespan
        
          
    
        
        
        MassPointRelief --> "*" ADEOfAbstractFeatureWithLifespan : adeOfAbstractFeatureWithLifespan
        click ADEOfAbstractFeatureWithLifespan href "../ADEOfAbstractFeatureWithLifespan/"
    

        
      MassPointRelief : adeOfAbstractReliefComponent
        
          
    
        
        
        MassPointRelief --> "*" ADEOfAbstractReliefComponent : adeOfAbstractReliefComponent
        click ADEOfAbstractReliefComponent href "../ADEOfAbstractReliefComponent/"
    

        
      MassPointRelief : adeOfAbstractSpaceBoundary
        
          
    
        
        
        MassPointRelief --> "*" ADEOfAbstractSpaceBoundary : adeOfAbstractSpaceBoundary
        click ADEOfAbstractSpaceBoundary href "../ADEOfAbstractSpaceBoundary/"
    

        
      MassPointRelief : adeOfMassPointRelief
        
          
    
        
        
        MassPointRelief --> "*" ADEOfMassPointRelief : adeOfMassPointRelief
        click ADEOfMassPointRelief href "../ADEOfMassPointRelief/"
    

        
      MassPointRelief : appearance
        
          
    
        
        
        MassPointRelief --> "*" AbstractAppearance : appearance
        click AbstractAppearance href "../AbstractAppearance/"
    

        
      MassPointRelief : creationDate
        
      MassPointRelief : description
        
      MassPointRelief : dynamizer
        
          
    
        
        
        MassPointRelief --> "*" AbstractDynamizer : dynamizer
        click AbstractDynamizer href "../AbstractDynamizer/"
    

        
      MassPointRelief : extent
        
      MassPointRelief : externalReference
        
          
    
        
        
        MassPointRelief --> "*" ExternalReference : externalReference
        click ExternalReference href "../ExternalReference/"
    

        
      MassPointRelief : featureID
        
          
    
        
        
        MassPointRelief --> "1" ID : featureID
        click ID href "../ID/"
    

        
      MassPointRelief : generalizesTo
        
          
    
        
        
        MassPointRelief --> "*" AbstractCityObject : generalizesTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      MassPointRelief : genericAttribute
        
          
    
        
        
        MassPointRelief --> "*" AbstractGenericAttribute : genericAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
    

        
      MassPointRelief : identifier
        
      MassPointRelief : lod
        
          
    
        
        
        MassPointRelief --> "1" IntegerBetween0and3 : lod
        click IntegerBetween0and3 href "../IntegerBetween0and3/"
    

        
      MassPointRelief : name
        
      MassPointRelief : pointCloud
        
          
    
        
        
        MassPointRelief --> "0..1" AbstractPointCloud : pointCloud
        click AbstractPointCloud href "../AbstractPointCloud/"
    

        
      MassPointRelief : relatedTo
        
          
    
        
        
        MassPointRelief --> "*" AbstractCityObject : relatedTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      MassPointRelief : relativeToTerrain
        
          
    
        
        
        MassPointRelief --> "0..1" RelativeToTerrain : relativeToTerrain
        click RelativeToTerrain href "../RelativeToTerrain/"
    

        
      MassPointRelief : relativeToWater
        
          
    
        
        
        MassPointRelief --> "0..1" RelativeToWater : relativeToWater
        click RelativeToWater href "../RelativeToWater/"
    

        
      MassPointRelief : reliefPoints
        
      MassPointRelief : terminationDate
        
      MassPointRelief : validFrom
        
      MassPointRelief : validTo
        
      
```





## Inheritance
* [AbstractFeature](AbstractFeature.md)
    * [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md)
        * [AbstractCityObject](AbstractCityObject.md)
            * [AbstractSpaceBoundary](AbstractSpaceBoundary.md)
                * [AbstractReliefComponent](AbstractReliefComponent.md)
                    * **MassPointRelief**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [adeOfMassPointRelief](adeOfMassPointRelief.md) | * <br/> [ADEOfMassPointRelief](ADEOfMassPointRelief.md) | Augments the MassPointRelief with properties defined in an ADE | direct |
| [pointCloud](pointCloud.md) | 0..1 <br/> [AbstractPointCloud](AbstractPointCloud.md) | Relates to the 3D PointCloud of the MassPointRelief | direct |
| [reliefPoints](reliefPoints.md) | 0..1 <br/> [String](String.md) | Relates to the 3D MultiPoint geometry of the MassPointRelief | direct |
| [lod](lod.md) | 1 <br/> [IntegerBetween0and3](IntegerBetween0and3.md) | Indicates the Level of Detail of the terrain component | [AbstractReliefComponent](AbstractReliefComponent.md) |
| [adeOfAbstractReliefComponent](adeOfAbstractReliefComponent.md) | * <br/> [ADEOfAbstractReliefComponent](ADEOfAbstractReliefComponent.md) | Augments AbstractReliefComponent with properties defined in an ADE | [AbstractReliefComponent](AbstractReliefComponent.md) |
| [extent](extent.md) | 0..1 <br/> [String](String.md) | Indicates the geometrical extent of the terrain component | [AbstractReliefComponent](AbstractReliefComponent.md) |
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















## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:MassPointRelief |
| native | citygml:MassPointRelief |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MassPointRelief
description: A MassPointRelief represents a terrain component as a collection of 3D
  points.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractReliefComponent
abstract: false
attributes:
  adeOfMassPointRelief:
    name: adeOfMassPointRelief
    description: Augments the MassPointRelief with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - MassPointRelief
    range: ADEOfMassPointRelief
    required: false
    multivalued: true
  pointCloud:
    name: pointCloud
    description: Relates to the 3D PointCloud of the MassPointRelief.
    from_schema: https://www.ogc.org/standards/citygml
    domain_of:
    - AbstractPhysicalSpace
    - AbstractThematicSurface
    - MassPointRelief
    range: AbstractPointCloud
    required: false
    multivalued: false
  reliefPoints:
    name: reliefPoints
    description: Relates to the 3D MultiPoint geometry of the MassPointRelief.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - MassPointRelief
    range: string
    required: false
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: MassPointRelief
description: A MassPointRelief represents a terrain component as a collection of 3D
  points.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractReliefComponent
abstract: false
attributes:
  adeOfMassPointRelief:
    name: adeOfMassPointRelief
    description: Augments the MassPointRelief with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfMassPointRelief
    owner: MassPointRelief
    domain_of:
    - MassPointRelief
    range: ADEOfMassPointRelief
    required: false
    multivalued: true
  pointCloud:
    name: pointCloud
    description: Relates to the 3D PointCloud of the MassPointRelief.
    from_schema: https://www.ogc.org/standards/citygml
    alias: pointCloud
    owner: MassPointRelief
    domain_of:
    - AbstractPhysicalSpace
    - AbstractThematicSurface
    - MassPointRelief
    range: AbstractPointCloud
    required: false
    multivalued: false
  reliefPoints:
    name: reliefPoints
    description: Relates to the 3D MultiPoint geometry of the MassPointRelief.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: reliefPoints
    owner: MassPointRelief
    domain_of:
    - MassPointRelief
    range: string
    required: false
    multivalued: false
  lod:
    name: lod
    description: Indicates the Level of Detail of the terrain component.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod
    owner: MassPointRelief
    domain_of:
    - AbstractReliefComponent
    - ReliefFeature
    range: IntegerBetween0and3
    required: true
    multivalued: false
  adeOfAbstractReliefComponent:
    name: adeOfAbstractReliefComponent
    description: Augments AbstractReliefComponent with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractReliefComponent
    owner: MassPointRelief
    domain_of:
    - AbstractReliefComponent
    range: ADEOfAbstractReliefComponent
    required: false
    multivalued: true
  extent:
    name: extent
    description: Indicates the geometrical extent of the terrain component. The geometrical
      extent is provided as a 2D Surface geometry.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: extent
    owner: MassPointRelief
    domain_of:
    - AbstractReliefComponent
    range: string
    required: false
    multivalued: false
  adeOfAbstractSpaceBoundary:
    name: adeOfAbstractSpaceBoundary
    description: Augments AbstractSpaceBoundary with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractSpaceBoundary
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: MassPointRelief
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
    owner: MassPointRelief
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
    owner: MassPointRelief
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>