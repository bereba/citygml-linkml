

# Class: MeasureOrNilReasonList 


_CityGML class from package Core_





URI: [citygml:MeasureOrNilReasonList](https://www.ogc.org/standards/citygml/MeasureOrNilReasonList)





```mermaid
 classDiagram
    class MeasureOrNilReasonList
    click MeasureOrNilReasonList href "../MeasureOrNilReasonList/"
      DoubleOrNilReasonList <|-- MeasureOrNilReasonList
        click DoubleOrNilReasonList href "../DoubleOrNilReasonList/"
      
      MeasureOrNilReasonList : list
        
          
    
        
        
        MeasureOrNilReasonList --> "1" DoubleOrNilReason : list
        click DoubleOrNilReason href "../DoubleOrNilReason/"
    

        
      MeasureOrNilReasonList : uom
        
      
```





## Inheritance
* [DoubleOrNilReasonList](DoubleOrNilReasonList.md)
    * **MeasureOrNilReasonList**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [uom](uom.md) | 1 <br/> [String](String.md) |  | direct |
| [list](list.md) | 1 <br/> [DoubleOrNilReason](DoubleOrNilReason.md) |  | [DoubleOrNilReasonList](DoubleOrNilReasonList.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:MeasureOrNilReasonList |
| native | citygml:MeasureOrNilReasonList |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MeasureOrNilReasonList
description: CityGML class from package Core
from_schema: https://www.ogc.org/standards/citygml
is_a: DoubleOrNilReasonList
abstract: false
attributes:
  uom:
    name: uom
    from_schema: https://www.ogc.org/standards/citygml
    domain_of:
    - SensorConnection
    - AbstractAtomicTimeseries
    - MeasureOrNilReasonList
    range: string
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: MeasureOrNilReasonList
description: CityGML class from package Core
from_schema: https://www.ogc.org/standards/citygml
is_a: DoubleOrNilReasonList
abstract: false
attributes:
  uom:
    name: uom
    from_schema: https://www.ogc.org/standards/citygml
    alias: uom
    owner: MeasureOrNilReasonList
    domain_of:
    - SensorConnection
    - AbstractAtomicTimeseries
    - MeasureOrNilReasonList
    range: string
    required: true
    multivalued: false
  list:
    name: list
    from_schema: https://www.ogc.org/standards/citygml
    alias: list
    owner: MeasureOrNilReasonList
    domain_of:
    - DoubleBetween0and1List
    - DoubleList
    - DoubleOrNilReasonList
    range: DoubleOrNilReason
    required: true
    multivalued: false

```
</details>