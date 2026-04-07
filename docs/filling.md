

# Slot: filling 


_Relates to the elements that fill the opening of the constructive element._





URI: [citygml:filling](https://www.ogc.org/standards/citygml/filling)
Alias: filling

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BridgeConstructiveElement](BridgeConstructiveElement.md) | A BridgeConstructiveElement is an element of a bridge which is essential from... |  no  |
| [TunnelConstructiveElement](TunnelConstructiveElement.md) | A TunnelConstructiveElement is an element of a Tunnel which is essential from... |  no  |
| [BuildingConstructiveElement](BuildingConstructiveElement.md) | A BuildingConstructiveElement is an element of a Building which is essential ... |  no  |
| [AbstractConstructiveElement](AbstractConstructiveElement.md) | AbstractConstructiveElement is the abstract superclass for the representation... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AbstractFillingElement](AbstractFillingElement.md) |
| Domain Of | [AbstractConstructiveElement](AbstractConstructiveElement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractConstructiveElement](AbstractConstructiveElement.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:filling |
| native | citygml:filling |




## LinkML Source

<details>
```yaml
name: filling
description: Relates to the elements that fill the opening of the constructive element.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: filling
owner: AbstractConstructiveElement
domain_of:
- AbstractConstructiveElement
range: AbstractFillingElement
required: false
multivalued: true

```
</details>