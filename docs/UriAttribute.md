

# Class: UriAttribute 


_UriAttribute is a data type used to define generic attributes of type "URI"._





URI: [citygml:UriAttribute](https://www.ogc.org/standards/citygml/UriAttribute)





```mermaid
 classDiagram
    class UriAttribute
    click UriAttribute href "../UriAttribute/"
      AbstractGenericAttribute <|-- UriAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
      
      UriAttribute : name
        
      UriAttribute : value
        
      
```





## Inheritance
* [AbstractGenericAttribute](AbstractGenericAttribute.md)
    * **UriAttribute**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Specifies the name of the UriAttribute | direct |
| [value](value.md) | 1 <br/> [Uri](Uri.md) | Specifies the "URI" value | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:UriAttribute |
| native | citygml:UriAttribute |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UriAttribute
description: UriAttribute is a data type used to define generic attributes of type
  "URI".
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractGenericAttribute
abstract: false
attributes:
  name:
    name: name
    description: Specifies the name of the UriAttribute.
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
    description: Specifies the "URI" value.
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
    range: uri
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: UriAttribute
description: UriAttribute is a data type used to define generic attributes of type
  "URI".
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractGenericAttribute
abstract: false
attributes:
  name:
    name: name
    description: Specifies the name of the UriAttribute.
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: UriAttribute
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
    description: Specifies the "URI" value.
    from_schema: https://www.ogc.org/standards/citygml
    alias: value
    owner: UriAttribute
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
    range: uri
    required: true
    multivalued: false

```
</details>