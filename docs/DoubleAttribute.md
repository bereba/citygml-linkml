

# Class: DoubleAttribute 


_DoubleAttribute is a data type used to define generic attributes of type "Double"._





URI: [citygml:DoubleAttribute](https://www.ogc.org/standards/citygml/DoubleAttribute)





```mermaid
 classDiagram
    class DoubleAttribute
    click DoubleAttribute href "../DoubleAttribute/"
      AbstractGenericAttribute <|-- DoubleAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
      
      DoubleAttribute : name
        
      DoubleAttribute : value
        
      
```





## Inheritance
* [AbstractGenericAttribute](AbstractGenericAttribute.md)
    * **DoubleAttribute**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Specifies the name of the DoubleAttribute | direct |
| [value](value.md) | 1 <br/> [Float](Float.md) | Specifies the "Double" value | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:DoubleAttribute |
| native | citygml:DoubleAttribute |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DoubleAttribute
description: DoubleAttribute is a data type used to define generic attributes of type
  "Double".
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractGenericAttribute
abstract: false
attributes:
  name:
    name: name
    description: Specifies the name of the DoubleAttribute.
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
    required: true
    multivalued: false
  value:
    name: value
    description: Specifies the "Double" value.
    from_schema: https://www.ogc.org/standards/citygml
    domain_of:
    - Height
    - RoomHeight
    - DoubleOrNilReason
    - CodeAttribute
    - DateAttribute
    - DoubleAttribute
    - IntAttribute
    - MeasureAttribute
    - StringAttribute
    - UriAttribute
    range: float
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: DoubleAttribute
description: DoubleAttribute is a data type used to define generic attributes of type
  "Double".
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractGenericAttribute
abstract: false
attributes:
  name:
    name: name
    description: Specifies the name of the DoubleAttribute.
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: DoubleAttribute
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
    required: true
    multivalued: false
  value:
    name: value
    description: Specifies the "Double" value.
    from_schema: https://www.ogc.org/standards/citygml
    alias: value
    owner: DoubleAttribute
    domain_of:
    - Height
    - RoomHeight
    - DoubleOrNilReason
    - CodeAttribute
    - DateAttribute
    - DoubleAttribute
    - IntAttribute
    - MeasureAttribute
    - StringAttribute
    - UriAttribute
    range: float
    required: true
    multivalued: false

```
</details>