

# Class: AbstractFeature 


_AbstractFeature is the abstract superclass of all feature types within the CityGML Conceptual Model._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [citygml:AbstractFeature](https://www.ogc.org/standards/citygml/AbstractFeature)





```mermaid
 classDiagram
    class AbstractFeature
    click AbstractFeature href "../AbstractFeature/"
      AbstractFeature <|-- AbstractTimeseries
        click AbstractTimeseries href "../AbstractTimeseries/"
      AbstractFeature <|-- AbstractSurfaceData
        click AbstractSurfaceData href "../AbstractSurfaceData/"
      AbstractFeature <|-- AbstractFeatureWithLifespan
        click AbstractFeatureWithLifespan href "../AbstractFeatureWithLifespan/"
      AbstractFeature <|-- AbstractPointCloud
        click AbstractPointCloud href "../AbstractPointCloud/"
      AbstractFeature <|-- Address
        click Address href "../Address/"
      
      AbstractFeature : adeOfAbstractFeature
        
          
    
        
        
        AbstractFeature --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      AbstractFeature : description
        
      AbstractFeature : featureID
        
          
    
        
        
        AbstractFeature --> "1" ID : featureID
        click ID href "../ID/"
    

        
      AbstractFeature : identifier
        
      AbstractFeature : name
        
      
```





## Inheritance
* **AbstractFeature**
    * [AbstractTimeseries](AbstractTimeseries.md)
    * [AbstractSurfaceData](AbstractSurfaceData.md)
    * [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md)
    * [AbstractPointCloud](AbstractPointCloud.md)
    * [Address](Address.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [featureID](featureID.md) | 1 <br/> [ID](ID.md) |  | direct |
| [identifier](identifier.md) | 0..1 <br/> [String](String.md) |  | direct |
| [name](name.md) | * <br/> [String](String.md) |  | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | direct |
| [adeOfAbstractFeature](adeOfAbstractFeature.md) | * <br/> [ADEOfAbstractFeature](ADEOfAbstractFeature.md) | Augments AbstractFeature with properties defined in an ADE | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CityModelMember](CityModelMember.md) | [featureMember](featureMember.md) | range | [AbstractFeature](AbstractFeature.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:AbstractFeature |
| native | citygml:AbstractFeature |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AbstractFeature
description: AbstractFeature is the abstract superclass of all feature types within
  the CityGML Conceptual Model.
from_schema: https://www.ogc.org/standards/citygml
abstract: true
attributes:
  featureID:
    name: featureID
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractFeature
    range: ID
    required: true
    multivalued: false
  identifier:
    name: identifier
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
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
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: AbstractFeature
description: AbstractFeature is the abstract superclass of all feature types within
  the CityGML Conceptual Model.
from_schema: https://www.ogc.org/standards/citygml
abstract: true
attributes:
  featureID:
    name: featureID
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: featureID
    owner: AbstractFeature
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
    owner: AbstractFeature
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: AbstractFeature
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
    owner: AbstractFeature
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
    owner: AbstractFeature
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>