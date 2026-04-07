

# Class: CompositeTimeseries 


_A CompositeTimeseries is a (possibly recursive) aggregation of atomic and composite timeseries. The components of a composite timeseries must have non-overlapping time intervals._





URI: [citygml:CompositeTimeseries](https://www.ogc.org/standards/citygml/CompositeTimeseries)





```mermaid
 classDiagram
    class CompositeTimeseries
    click CompositeTimeseries href "../CompositeTimeseries/"
      AbstractTimeseries <|-- CompositeTimeseries
        click AbstractTimeseries href "../AbstractTimeseries/"
      
      CompositeTimeseries : adeOfAbstractFeature
        
          
    
        
        
        CompositeTimeseries --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      CompositeTimeseries : adeOfAbstractTimeseries
        
          
    
        
        
        CompositeTimeseries --> "*" ADEOfAbstractTimeseries : adeOfAbstractTimeseries
        click ADEOfAbstractTimeseries href "../ADEOfAbstractTimeseries/"
    

        
      CompositeTimeseries : adeOfCompositeTimeseries
        
          
    
        
        
        CompositeTimeseries --> "*" ADEOfCompositeTimeseries : adeOfCompositeTimeseries
        click ADEOfCompositeTimeseries href "../ADEOfCompositeTimeseries/"
    

        
      CompositeTimeseries : component
        
          
    
        
        
        CompositeTimeseries --> "1..*" TimeseriesComponent : component
        click TimeseriesComponent href "../TimeseriesComponent/"
    

        
      CompositeTimeseries : description
        
      CompositeTimeseries : featureID
        
          
    
        
        
        CompositeTimeseries --> "1" ID : featureID
        click ID href "../ID/"
    

        
      CompositeTimeseries : firstTimestamp
        
      CompositeTimeseries : identifier
        
      CompositeTimeseries : lastTimestamp
        
      CompositeTimeseries : name
        
      
```





## Inheritance
* [AbstractFeature](AbstractFeature.md)
    * [AbstractTimeseries](AbstractTimeseries.md)
        * **CompositeTimeseries**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [adeOfCompositeTimeseries](adeOfCompositeTimeseries.md) | * <br/> [ADEOfCompositeTimeseries](ADEOfCompositeTimeseries.md) | Augments the CompositeTimeseries with properties defined in an ADE | direct |
| [component](component.md) | 1..* <br/> [TimeseriesComponent](TimeseriesComponent.md) | Relates to the atomic and composite timeseries that are part of the Composite... | direct |
| [firstTimestamp](firstTimestamp.md) | 0..1 <br/> [String](String.md) | Specifies the beginning of the timeseries | [AbstractTimeseries](AbstractTimeseries.md) |
| [lastTimestamp](lastTimestamp.md) | 0..1 <br/> [String](String.md) | Specifies the end of the timeseries | [AbstractTimeseries](AbstractTimeseries.md) |
| [adeOfAbstractTimeseries](adeOfAbstractTimeseries.md) | * <br/> [ADEOfAbstractTimeseries](ADEOfAbstractTimeseries.md) | Augments AbstractTimeseries with properties defined in an ADE | [AbstractTimeseries](AbstractTimeseries.md) |
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
| self | citygml:CompositeTimeseries |
| native | citygml:CompositeTimeseries |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CompositeTimeseries
description: A CompositeTimeseries is a (possibly recursive) aggregation of atomic
  and composite timeseries. The components of a composite timeseries must have non-overlapping
  time intervals.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractTimeseries
abstract: false
attributes:
  adeOfCompositeTimeseries:
    name: adeOfCompositeTimeseries
    description: Augments the CompositeTimeseries with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - CompositeTimeseries
    range: ADEOfCompositeTimeseries
    required: false
    multivalued: true
  component:
    name: component
    description: Relates to the atomic and composite timeseries that are part of the
      CompositeTimeseries. The referenced timeseries are sequentially ordered.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - CompositeTimeseries
    range: TimeseriesComponent
    required: true
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: CompositeTimeseries
description: A CompositeTimeseries is a (possibly recursive) aggregation of atomic
  and composite timeseries. The components of a composite timeseries must have non-overlapping
  time intervals.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractTimeseries
abstract: false
attributes:
  adeOfCompositeTimeseries:
    name: adeOfCompositeTimeseries
    description: Augments the CompositeTimeseries with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfCompositeTimeseries
    owner: CompositeTimeseries
    domain_of:
    - CompositeTimeseries
    range: ADEOfCompositeTimeseries
    required: false
    multivalued: true
  component:
    name: component
    description: Relates to the atomic and composite timeseries that are part of the
      CompositeTimeseries. The referenced timeseries are sequentially ordered.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: component
    owner: CompositeTimeseries
    domain_of:
    - CompositeTimeseries
    range: TimeseriesComponent
    required: true
    multivalued: true
  firstTimestamp:
    name: firstTimestamp
    description: Specifies the beginning of the timeseries.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: firstTimestamp
    owner: CompositeTimeseries
    domain_of:
    - AbstractTimeseries
    range: string
    required: false
    multivalued: false
  lastTimestamp:
    name: lastTimestamp
    description: Specifies the end of the timeseries.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: lastTimestamp
    owner: CompositeTimeseries
    domain_of:
    - AbstractTimeseries
    range: string
    required: false
    multivalued: false
  adeOfAbstractTimeseries:
    name: adeOfAbstractTimeseries
    description: Augments AbstractTimeseries with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractTimeseries
    owner: CompositeTimeseries
    domain_of:
    - AbstractTimeseries
    range: ADEOfAbstractTimeseries
    required: false
    multivalued: true
  featureID:
    name: featureID
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: featureID
    owner: CompositeTimeseries
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
    owner: CompositeTimeseries
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: CompositeTimeseries
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
    owner: CompositeTimeseries
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
    owner: CompositeTimeseries
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>