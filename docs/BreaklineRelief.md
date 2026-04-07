

# Class: BreaklineRelief 


_A BreaklineRelief represents a terrain component with 3D lines. These lines denote break lines or ridge/valley lines._





URI: [citygml:BreaklineRelief](https://www.ogc.org/standards/citygml/BreaklineRelief)





```mermaid
 classDiagram
    class BreaklineRelief
    click BreaklineRelief href "../BreaklineRelief/"
      AbstractReliefComponent <|-- BreaklineRelief
        click AbstractReliefComponent href "../AbstractReliefComponent/"
      
      BreaklineRelief : adeOfAbstractCityObject
        
          
    
        
        
        BreaklineRelief --> "*" ADEOfAbstractCityObject : adeOfAbstractCityObject
        click ADEOfAbstractCityObject href "../ADEOfAbstractCityObject/"
    

        
      BreaklineRelief : adeOfAbstractFeature
        
          
    
        
        
        BreaklineRelief --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      BreaklineRelief : adeOfAbstractFeatureWithLifespan
        
          
    
        
        
        BreaklineRelief --> "*" ADEOfAbstractFeatureWithLifespan : adeOfAbstractFeatureWithLifespan
        click ADEOfAbstractFeatureWithLifespan href "../ADEOfAbstractFeatureWithLifespan/"
    

        
      BreaklineRelief : adeOfAbstractReliefComponent
        
          
    
        
        
        BreaklineRelief --> "*" ADEOfAbstractReliefComponent : adeOfAbstractReliefComponent
        click ADEOfAbstractReliefComponent href "../ADEOfAbstractReliefComponent/"
    

        
      BreaklineRelief : adeOfAbstractSpaceBoundary
        
          
    
        
        
        BreaklineRelief --> "*" ADEOfAbstractSpaceBoundary : adeOfAbstractSpaceBoundary
        click ADEOfAbstractSpaceBoundary href "../ADEOfAbstractSpaceBoundary/"
    

        
      BreaklineRelief : adeOfBreaklineRelief
        
          
    
        
        
        BreaklineRelief --> "*" ADEOfBreaklineRelief : adeOfBreaklineRelief
        click ADEOfBreaklineRelief href "../ADEOfBreaklineRelief/"
    

        
      BreaklineRelief : appearance
        
          
    
        
        
        BreaklineRelief --> "*" AbstractAppearance : appearance
        click AbstractAppearance href "../AbstractAppearance/"
    

        
      BreaklineRelief : breaklines
        
      BreaklineRelief : creationDate
        
      BreaklineRelief : description
        
      BreaklineRelief : dynamizer
        
          
    
        
        
        BreaklineRelief --> "*" AbstractDynamizer : dynamizer
        click AbstractDynamizer href "../AbstractDynamizer/"
    

        
      BreaklineRelief : extent
        
      BreaklineRelief : externalReference
        
          
    
        
        
        BreaklineRelief --> "*" ExternalReference : externalReference
        click ExternalReference href "../ExternalReference/"
    

        
      BreaklineRelief : featureID
        
          
    
        
        
        BreaklineRelief --> "1" ID : featureID
        click ID href "../ID/"
    

        
      BreaklineRelief : generalizesTo
        
          
    
        
        
        BreaklineRelief --> "*" AbstractCityObject : generalizesTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      BreaklineRelief : genericAttribute
        
          
    
        
        
        BreaklineRelief --> "*" AbstractGenericAttribute : genericAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
    

        
      BreaklineRelief : identifier
        
      BreaklineRelief : lod
        
          
    
        
        
        BreaklineRelief --> "1" IntegerBetween0and3 : lod
        click IntegerBetween0and3 href "../IntegerBetween0and3/"
    

        
      BreaklineRelief : name
        
      BreaklineRelief : relatedTo
        
          
    
        
        
        BreaklineRelief --> "*" AbstractCityObject : relatedTo
        click AbstractCityObject href "../AbstractCityObject/"
    

        
      BreaklineRelief : relativeToTerrain
        
          
    
        
        
        BreaklineRelief --> "0..1" RelativeToTerrain : relativeToTerrain
        click RelativeToTerrain href "../RelativeToTerrain/"
    

        
      BreaklineRelief : relativeToWater
        
          
    
        
        
        BreaklineRelief --> "0..1" RelativeToWater : relativeToWater
        click RelativeToWater href "../RelativeToWater/"
    

        
      BreaklineRelief : ridgeOrValleyLines
        
      BreaklineRelief : terminationDate
        
      BreaklineRelief : validFrom
        
      BreaklineRelief : validTo
        
      
```





## Inheritance
* [AbstractFeature](AbstractFeature.md)
    * [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md)
        * [AbstractCityObject](AbstractCityObject.md)
            * [AbstractSpaceBoundary](AbstractSpaceBoundary.md)
                * [AbstractReliefComponent](AbstractReliefComponent.md)
                    * **BreaklineRelief**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [adeOfBreaklineRelief](adeOfBreaklineRelief.md) | * <br/> [ADEOfBreaklineRelief](ADEOfBreaklineRelief.md) | Augments the BreaklineRelief with properties defined in an ADE | direct |
| [ridgeOrValleyLines](ridgeOrValleyLines.md) | 0..1 <br/> [String](String.md) | Relates to the 3D MultiCurve geometry of the MassPointRelief | direct |
| [breaklines](breaklines.md) | 0..1 <br/> [String](String.md) | Relates to the 3D MultiCurve geometry of the MassPointRelief | direct |
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
| self | citygml:BreaklineRelief |
| native | citygml:BreaklineRelief |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BreaklineRelief
description: A BreaklineRelief represents a terrain component with 3D lines. These
  lines denote break lines or ridge/valley lines.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractReliefComponent
abstract: false
attributes:
  adeOfBreaklineRelief:
    name: adeOfBreaklineRelief
    description: Augments the BreaklineRelief with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - BreaklineRelief
    range: ADEOfBreaklineRelief
    required: false
    multivalued: true
  ridgeOrValleyLines:
    name: ridgeOrValleyLines
    description: Relates to the 3D MultiCurve geometry of the MassPointRelief. This
      association role is used to represent ridge or valley lines.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - BreaklineRelief
    range: string
    required: false
    multivalued: false
  breaklines:
    name: breaklines
    description: Relates to the 3D MultiCurve geometry of the MassPointRelief. This
      association role is used to represent break lines.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - BreaklineRelief
    range: string
    required: false
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: BreaklineRelief
description: A BreaklineRelief represents a terrain component with 3D lines. These
  lines denote break lines or ridge/valley lines.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractReliefComponent
abstract: false
attributes:
  adeOfBreaklineRelief:
    name: adeOfBreaklineRelief
    description: Augments the BreaklineRelief with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfBreaklineRelief
    owner: BreaklineRelief
    domain_of:
    - BreaklineRelief
    range: ADEOfBreaklineRelief
    required: false
    multivalued: true
  ridgeOrValleyLines:
    name: ridgeOrValleyLines
    description: Relates to the 3D MultiCurve geometry of the MassPointRelief. This
      association role is used to represent ridge or valley lines.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: ridgeOrValleyLines
    owner: BreaklineRelief
    domain_of:
    - BreaklineRelief
    range: string
    required: false
    multivalued: false
  breaklines:
    name: breaklines
    description: Relates to the 3D MultiCurve geometry of the MassPointRelief. This
      association role is used to represent break lines.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: breaklines
    owner: BreaklineRelief
    domain_of:
    - BreaklineRelief
    range: string
    required: false
    multivalued: false
  lod:
    name: lod
    description: Indicates the Level of Detail of the terrain component.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lod
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: BreaklineRelief
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
    owner: BreaklineRelief
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
    owner: BreaklineRelief
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>