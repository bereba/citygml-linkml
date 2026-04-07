

# Class: IntAttribute 


_IntAttribute is a data type used to define generic attributes of type "Integer"._





URI: [citygml:IntAttribute](https://www.ogc.org/standards/citygml/IntAttribute)





```mermaid
 classDiagram
    class IntAttribute
    click IntAttribute href "../IntAttribute/"
      AbstractGenericAttribute <|-- IntAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
      
      IntAttribute : name
        
      IntAttribute : value
        
      
```





## Inheritance
* [AbstractGenericAttribute](AbstractGenericAttribute.md)
    * **IntAttribute**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Specifies the name of the IntAttribute | direct |
| [value](value.md) | 1 <br/> [Integer](Integer.md) | Specifies the "Integer" value | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:IntAttribute |
| native | citygml:IntAttribute |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IntAttribute
description: IntAttribute is a data type used to define generic attributes of type
  "Integer".
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractGenericAttribute
abstract: false
attributes:
  name:
    name: name
    description: Specifies the name of the IntAttribute.
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
    description: Specifies the "Integer" value.
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
    range: integer
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: IntAttribute
description: IntAttribute is a data type used to define generic attributes of type
  "Integer".
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractGenericAttribute
abstract: false
attributes:
  name:
    name: name
    description: Specifies the name of the IntAttribute.
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: IntAttribute
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
    description: Specifies the "Integer" value.
    from_schema: https://www.ogc.org/standards/citygml
    alias: value
    owner: IntAttribute
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
    range: integer
    required: true
    multivalued: false

```
</details>