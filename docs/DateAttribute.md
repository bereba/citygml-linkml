

# Class: DateAttribute 


_DateAttribute is a data type used to define generic attributes of type "Date"._





URI: [citygml:DateAttribute](https://www.ogc.org/standards/citygml/DateAttribute)





```mermaid
 classDiagram
    class DateAttribute
    click DateAttribute href "../DateAttribute/"
      AbstractGenericAttribute <|-- DateAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
      
      DateAttribute : name
        
      DateAttribute : value
        
      
```





## Inheritance
* [AbstractGenericAttribute](AbstractGenericAttribute.md)
    * **DateAttribute**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Specifies the name of the DateAttribute | direct |
| [value](value.md) | 1 <br/> [Date](Date.md) | Specifies the "Date" value | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:DateAttribute |
| native | citygml:DateAttribute |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DateAttribute
description: DateAttribute is a data type used to define generic attributes of type
  "Date".
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractGenericAttribute
abstract: false
attributes:
  name:
    name: name
    description: Specifies the name of the DateAttribute.
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
    description: Specifies the "Date" value.
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
    range: date
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: DateAttribute
description: DateAttribute is a data type used to define generic attributes of type
  "Date".
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractGenericAttribute
abstract: false
attributes:
  name:
    name: name
    description: Specifies the name of the DateAttribute.
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: DateAttribute
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
    description: Specifies the "Date" value.
    from_schema: https://www.ogc.org/standards/citygml
    alias: value
    owner: DateAttribute
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
    range: date
    required: true
    multivalued: false

```
</details>