

# Slot: geometryValue 


_Specifies the geometry value of the TimeValuePair._





URI: [citygml:geometryValue](https://www.ogc.org/standards/citygml/geometryValue)
Alias: geometryValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeValuePair](TimeValuePair.md) | A TimeValuePair represents a value that is valid for a given timepoint |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [TimeValuePair](TimeValuePair.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TimeValuePair](TimeValuePair.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:geometryValue |
| native | citygml:geometryValue |




## LinkML Source

<details>
```yaml
name: geometryValue
description: Specifies the geometry value of the TimeValuePair.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: geometryValue
owner: TimeValuePair
domain_of:
- TimeValuePair
range: string
required: false
multivalued: false

```
</details>