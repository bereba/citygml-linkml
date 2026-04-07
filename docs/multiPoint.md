

# Slot: multiPoint 


_Relates to the MultiPoint geometry of the Address. The geometry relates the address spatially to a city object._





URI: [citygml:multiPoint](https://www.ogc.org/standards/citygml/multiPoint)
Alias: multiPoint

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Address](Address.md) | Address represents an address of a city object |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Address](Address.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Address](Address.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:multiPoint |
| native | citygml:multiPoint |




## LinkML Source

<details>
```yaml
name: multiPoint
description: Relates to the MultiPoint geometry of the Address. The geometry relates
  the address spatially to a city object.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: multiPoint
owner: Address
domain_of:
- Address
range: string
required: false
multivalued: false

```
</details>