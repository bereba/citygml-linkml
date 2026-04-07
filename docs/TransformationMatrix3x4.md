

# Class: TransformationMatrix3x4 


_CityGML class from package Core_





URI: [citygml:TransformationMatrix3x4](https://www.ogc.org/standards/citygml/TransformationMatrix3x4)





```mermaid
 classDiagram
    class TransformationMatrix3x4
    click TransformationMatrix3x4 href "../TransformationMatrix3x4/"
      DoubleList <|-- TransformationMatrix3x4
        click DoubleList href "../DoubleList/"
      
      TransformationMatrix3x4 : list
        
      
```





## Inheritance
* [DoubleList](DoubleList.md)
    * **TransformationMatrix3x4**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [list](list.md) | 1 <br/> [Float](Float.md) |  | [DoubleList](DoubleList.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TexCoordGen](TexCoordGen.md) | [worldToTexture](worldToTexture.md) | range | [TransformationMatrix3x4](TransformationMatrix3x4.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:TransformationMatrix3x4 |
| native | citygml:TransformationMatrix3x4 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TransformationMatrix3x4
description: CityGML class from package Core
from_schema: https://www.ogc.org/standards/citygml
is_a: DoubleList
abstract: false

```
</details>

### Induced

<details>
```yaml
name: TransformationMatrix3x4
description: CityGML class from package Core
from_schema: https://www.ogc.org/standards/citygml
is_a: DoubleList
abstract: false
attributes:
  list:
    name: list
    from_schema: https://www.ogc.org/standards/citygml
    alias: list
    owner: TransformationMatrix3x4
    domain_of:
    - DoubleBetween0and1List
    - DoubleList
    - DoubleOrNilReasonList
    range: float
    required: true
    multivalued: false

```
</details>