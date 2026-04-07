

# Class: DoubleList 


_CityGML class from package Core_





URI: [citygml:DoubleList](https://www.ogc.org/standards/citygml/DoubleList)





```mermaid
 classDiagram
    class DoubleList
    click DoubleList href "../DoubleList/"
      DoubleList <|-- TransformationMatrix2x2
        click TransformationMatrix2x2 href "../TransformationMatrix2x2/"
      DoubleList <|-- TransformationMatrix3x4
        click TransformationMatrix3x4 href "../TransformationMatrix3x4/"
      DoubleList <|-- TransformationMatrix4x4
        click TransformationMatrix4x4 href "../TransformationMatrix4x4/"
      
      DoubleList : list
        
      
```





## Inheritance
* **DoubleList**
    * [TransformationMatrix2x2](TransformationMatrix2x2.md)
    * [TransformationMatrix3x4](TransformationMatrix3x4.md)
    * [TransformationMatrix4x4](TransformationMatrix4x4.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [list](list.md) | 1 <br/> [Float](Float.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TexCoordList](TexCoordList.md) | [textureCoordinates](textureCoordinates.md) | range | [DoubleList](DoubleList.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:DoubleList |
| native | citygml:DoubleList |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DoubleList
description: CityGML class from package Core
from_schema: https://www.ogc.org/standards/citygml
abstract: false
attributes:
  list:
    name: list
    from_schema: https://www.ogc.org/standards/citygml
    domain_of:
    - DoubleBetween0and1List
    - DoubleList
    - DoubleOrNilReasonList
    range: float
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: DoubleList
description: CityGML class from package Core
from_schema: https://www.ogc.org/standards/citygml
abstract: false
attributes:
  list:
    name: list
    from_schema: https://www.ogc.org/standards/citygml
    alias: list
    owner: DoubleList
    domain_of:
    - DoubleBetween0and1List
    - DoubleList
    - DoubleOrNilReasonList
    range: float
    required: true
    multivalued: false

```
</details>