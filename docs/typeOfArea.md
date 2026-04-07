

# Slot: typeOfArea 


_Indicates the specific type of the QualifiedArea._





URI: [citygml:typeOfArea](https://www.ogc.org/standards/citygml/typeOfArea)
Alias: typeOfArea

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QualifiedArea](QualifiedArea.md) | QualifiedArea is an application-dependent measure of the area of a space or o... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [QualifiedAreaTypeValue](QualifiedAreaTypeValue.md) |
| Domain Of | [QualifiedArea](QualifiedArea.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [QualifiedArea](QualifiedArea.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:typeOfArea |
| native | citygml:typeOfArea |




## LinkML Source

<details>
```yaml
name: typeOfArea
description: Indicates the specific type of the QualifiedArea.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: typeOfArea
owner: QualifiedArea
domain_of:
- QualifiedArea
range: QualifiedAreaTypeValue
required: true
multivalued: false

```
</details>