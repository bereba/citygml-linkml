

# Slot: attributeRef 


_Specifies the attribute of a CityGML feature whose value is overridden or replaced by the (dynamic) values specified by the Dynamizer._





URI: [citygml:attributeRef](https://www.ogc.org/standards/citygml/attributeRef)
Alias: attributeRef

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dynamizer](Dynamizer.md) | A Dynamizer is an object that injects timeseries data for an individual attri... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Dynamizer](Dynamizer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dynamizer](Dynamizer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:attributeRef |
| native | citygml:attributeRef |




## LinkML Source

<details>
```yaml
name: attributeRef
description: Specifies the attribute of a CityGML feature whose value is overridden
  or replaced by the (dynamic) values specified by the Dynamizer.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: attributeRef
owner: Dynamizer
domain_of:
- Dynamizer
range: string
required: true
multivalued: false

```
</details>