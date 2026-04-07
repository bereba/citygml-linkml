

# Class: MeasureAttribute 


_MeasureAttribute is a data type used to define generic attributes of type "Measure"._





URI: [citygml:MeasureAttribute](https://www.ogc.org/standards/citygml/MeasureAttribute)





```mermaid
 classDiagram
    class MeasureAttribute
    click MeasureAttribute href "../MeasureAttribute/"
      AbstractGenericAttribute <|-- MeasureAttribute
        click AbstractGenericAttribute href "../AbstractGenericAttribute/"
      
      MeasureAttribute : name
        
      MeasureAttribute : value
        
      
```





## Inheritance
* [AbstractGenericAttribute](AbstractGenericAttribute.md)
    * **MeasureAttribute**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | Specifies the name of the MeasureAttribute | direct |
| [value](value.md) | 1 <br/> [Float](Float.md) | Specifies the value of the MeasureAttribute | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:MeasureAttribute |
| native | citygml:MeasureAttribute |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MeasureAttribute
description: MeasureAttribute is a data type used to define generic attributes of
  type "Measure".
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractGenericAttribute
abstract: false
attributes:
  name:
    name: name
    description: Specifies the name of the MeasureAttribute.
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
    description: Specifies the value of the MeasureAttribute. The value is of type
      "Measure", which can additionally provide the units of measure. [cf. ISO 19103]
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
name: MeasureAttribute
description: MeasureAttribute is a data type used to define generic attributes of
  type "Measure".
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractGenericAttribute
abstract: false
attributes:
  name:
    name: name
    description: Specifies the name of the MeasureAttribute.
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: MeasureAttribute
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
    description: Specifies the value of the MeasureAttribute. The value is of type
      "Measure", which can additionally provide the units of measure. [cf. ISO 19103]
    from_schema: https://www.ogc.org/standards/citygml
    alias: value
    owner: MeasureAttribute
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