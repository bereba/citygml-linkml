

# Class: ColorPlusOpacity 


_CityGML class from package Appearance_





URI: [citygml:ColorPlusOpacity](https://www.ogc.org/standards/citygml/ColorPlusOpacity)





```mermaid
 classDiagram
    class ColorPlusOpacity
    click ColorPlusOpacity href "../ColorPlusOpacity/"
      DoubleBetween0and1List <|-- ColorPlusOpacity
        click DoubleBetween0and1List href "../DoubleBetween0and1List/"
      
      ColorPlusOpacity : list
        
          
    
        
        
        ColorPlusOpacity --> "1" DoubleBetween0and1 : list
        click DoubleBetween0and1 href "../DoubleBetween0and1/"
    

        
      
```





## Inheritance
* [DoubleBetween0and1List](DoubleBetween0and1List.md)
    * **ColorPlusOpacity**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [list](list.md) | 1 <br/> [DoubleBetween0and1](DoubleBetween0and1.md) |  | [DoubleBetween0and1List](DoubleBetween0and1List.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AbstractTexture](AbstractTexture.md) | [borderColor](borderColor.md) | range | [ColorPlusOpacity](ColorPlusOpacity.md) |
| [GeoreferencedTexture](GeoreferencedTexture.md) | [borderColor](borderColor.md) | range | [ColorPlusOpacity](ColorPlusOpacity.md) |
| [ParameterizedTexture](ParameterizedTexture.md) | [borderColor](borderColor.md) | range | [ColorPlusOpacity](ColorPlusOpacity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:ColorPlusOpacity |
| native | citygml:ColorPlusOpacity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ColorPlusOpacity
description: CityGML class from package Appearance
from_schema: https://www.ogc.org/standards/citygml
is_a: DoubleBetween0and1List
abstract: false

```
</details>

### Induced

<details>
```yaml
name: ColorPlusOpacity
description: CityGML class from package Appearance
from_schema: https://www.ogc.org/standards/citygml
is_a: DoubleBetween0and1List
abstract: false
attributes:
  list:
    name: list
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: list
    owner: ColorPlusOpacity
    domain_of:
    - DoubleBetween0and1List
    - DoubleList
    - DoubleOrNilReasonList
    range: DoubleBetween0and1
    required: true
    multivalued: false

```
</details>