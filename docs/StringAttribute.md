

# Class: StringAttribute 


_StringAttribute is a data type used to define generic attributes of type "String"._





URI: [citygml:StringAttribute](https://www.ogc.org/standards/citygml/StringAttribute)





```mermaid
 classDiagram
    class StringAttribute
    click StringAttribute href "../StringAttribute/"
      AbstractGenericAttribute <|-- StringAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
      
      StringAttribute : name
        
      StringAttribute : value
        
      
```





## Inheritance
* [AbstractGenericAttribute](AbstractGenericAttribute.md)
    * **StringAttribute**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Specifies the name of the StringAttribute | direct |
| [value](value.md) | 1 <br/> [String](String.md) | Specifies the "String" value | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:StringAttribute |
| native | citygml:StringAttribute |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StringAttribute
description: StringAttribute is a data type used to define generic attributes of type
  "String".
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractGenericAttribute
abstract: false
attributes:
  name:
    name: name
    description: Specifies the name of the StringAttribute.
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
    description: Specifies the "String" value.
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
    range: string
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: StringAttribute
description: StringAttribute is a data type used to define generic attributes of type
  "String".
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractGenericAttribute
abstract: false
attributes:
  name:
    name: name
    description: Specifies the name of the StringAttribute.
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: StringAttribute
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
    description: Specifies the "String" value.
    from_schema: https://www.ogc.org/standards/citygml
    alias: value
    owner: StringAttribute
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
    range: string
    required: true
    multivalued: false

```
</details>