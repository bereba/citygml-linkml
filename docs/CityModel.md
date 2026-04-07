

# Class: CityModel 


_CityModel is the container for all objects belonging to a city model._





URI: [citygml:CityModel](https://www.ogc.org/standards/citygml/CityModel)





```mermaid
 classDiagram
    class CityModel
    click CityModel href "../CityModel/"
      AbstractFeatureWithLifespan <|-- CityModel
        click AbstractFeatureWithLifespan href "../AbstractFeatureWithLifespan/"
      
      CityModel : adeOfAbstractFeature
        
          
    
        
        
        CityModel --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      CityModel : adeOfAbstractFeatureWithLifespan
        
          
    
        
        
        CityModel --> "*" ADEOfAbstractFeatureWithLifespan : adeOfAbstractFeatureWithLifespan
        click ADEOfAbstractFeatureWithLifespan href "../ADEOfAbstractFeatureWithLifespan/"
    

        
      CityModel : adeOfCityModel
        
          
    
        
        
        CityModel --> "*" ADEOfCityModel : adeOfCityModel
        click ADEOfCityModel href "../ADEOfCityModel/"
    

        
      CityModel : cityModelMember
        
          
    
        
        
        CityModel --> "*" CityModelMember : cityModelMember
        click CityModelMember href "../CityModelMember/"
    

        
      CityModel : creationDate
        
      CityModel : description
        
      CityModel : engineeringCRS
        
      CityModel : featureID
        
          
    
        
        
        CityModel --> "1" ID : featureID
        click ID href "../ID/"
    

        
      CityModel : identifier
        
      CityModel : name
        
      CityModel : terminationDate
        
      CityModel : validFrom
        
      CityModel : validTo
        
      
```





## Inheritance
* [AbstractFeature](AbstractFeature.md)
    * [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md)
        * **CityModel**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [engineeringCRS](engineeringCRS.md) | 0..1 <br/> [String](String.md) | Specifies the local engineering coordinate reference system of the CityModel ... | direct |
| [adeOfCityModel](adeOfCityModel.md) | * <br/> [ADEOfCityModel](ADEOfCityModel.md) | Augments the CityModel with properties defined in an ADE | direct |
| [cityModelMember](cityModelMember.md) | * <br/> [CityModelMember](CityModelMember.md) |  | direct |
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
| self | citygml:CityModel |
| native | citygml:CityModel |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CityModel
description: CityModel is the container for all objects belonging to a city model.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractFeatureWithLifespan
abstract: false
attributes:
  engineeringCRS:
    name: engineeringCRS
    description: Specifies the local engineering coordinate reference system of the
      CityModel that can be provided inline the CityModel instead of referencing a
      well-known CRS definition. The definition of an engineering CRS requires an
      anchor point which relates the origin of the local coordinate system to a point
      on the earth's surface in order to facilitate the transformation of coordinates
      from the local engineering CRS.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - CityModel
    range: string
    required: false
    multivalued: false
  adeOfCityModel:
    name: adeOfCityModel
    description: Augments the CityModel with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - CityModel
    range: ADEOfCityModel
    required: false
    multivalued: true
  cityModelMember:
    name: cityModelMember
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - CityModel
    range: CityModelMember
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: CityModel
description: CityModel is the container for all objects belonging to a city model.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractFeatureWithLifespan
abstract: false
attributes:
  engineeringCRS:
    name: engineeringCRS
    description: Specifies the local engineering coordinate reference system of the
      CityModel that can be provided inline the CityModel instead of referencing a
      well-known CRS definition. The definition of an engineering CRS requires an
      anchor point which relates the origin of the local coordinate system to a point
      on the earth's surface in order to facilitate the transformation of coordinates
      from the local engineering CRS.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: engineeringCRS
    owner: CityModel
    domain_of:
    - CityModel
    range: string
    required: false
    multivalued: false
  adeOfCityModel:
    name: adeOfCityModel
    description: Augments the CityModel with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfCityModel
    owner: CityModel
    domain_of:
    - CityModel
    range: ADEOfCityModel
    required: false
    multivalued: true
  cityModelMember:
    name: cityModelMember
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: cityModelMember
    owner: CityModel
    domain_of:
    - CityModel
    range: CityModelMember
    required: false
    multivalued: true
  creationDate:
    name: creationDate
    description: Indicates the date at which a CityGML feature was added to the CityModel.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: creationDate
    owner: CityModel
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
    owner: CityModel
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
    owner: CityModel
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
    owner: CityModel
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
    owner: CityModel
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
    owner: CityModel
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
    owner: CityModel
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: CityModel
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
    owner: CityModel
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
    owner: CityModel
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>