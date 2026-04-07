

# Slot: isStructuralElement 


_Indicates whether the constructive element is essential from a structural point of view. A structural element cannot be omitted without collapsing of the construction. Examples are pylons and anchorages of bridges._





URI: [citygml:isStructuralElement](https://www.ogc.org/standards/citygml/isStructuralElement)
Alias: isStructuralElement

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
| Range | [Boolean](Boolean.md) |
| Domain Of | [AbstractConstructiveElement](AbstractConstructiveElement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | citygml:isStructuralElement |
| native | citygml:isStructuralElement |




## LinkML Source

<details>
```yaml
name: isStructuralElement
description: Indicates whether the constructive element is essential from a structural
  point of view. A structural element cannot be omitted without collapsing of the
  construction. Examples are pylons and anchorages of bridges.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: isStructuralElement
owner: AbstractConstructiveElement
domain_of:
- AbstractConstructiveElement
range: boolean
required: false
multivalued: false

```
</details>