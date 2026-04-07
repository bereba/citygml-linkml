

# Slot: constructionEvent 


_Describes specific events in the life-time of the construction._





URI: [citygml:constructionEvent](https://www.ogc.org/standards/citygml/constructionEvent)
Alias: constructionEvent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Building](Building.md) | A Building is a free-standing, self-supporting construction that is roofed, u... |  no  |
| [AbstractBuilding](AbstractBuilding.md) | AbstractBuilding is an abstract superclass representing the common attributes... |  no  |
| [Bridge](Bridge.md) | A Bridge represents a structure that affords the passage of pedestrians, anim... |  no  |
| [OtherConstruction](OtherConstruction.md) | An OtherConstruction is a construction that is not covered by any of the othe... |  no  |
| [AbstractBridge](AbstractBridge.md) | AbstractBridge is an abstract superclass representing the common attributes a... |  no  |
| [AbstractConstruction](AbstractConstruction.md) | AbstractConstruction is the abstract superclass for objects that are manufact... |  no  |
| [BuildingPart](BuildingPart.md) | A BuildingPart is a physical or functional subdivision of a Building |  no  |
| [BridgePart](BridgePart.md) | A BridgePart is a physical or functional subdivision of a Bridge |  no  |
| [TunnelPart](TunnelPart.md) | A TunnelPart is a physical or functional subdivision of a Tunnel |  no  |
| [Tunnel](Tunnel.md) | A Tunnel represents a horizontal or sloping enclosed passage way of a certain... |  no  |
| [AbstractTunnel](AbstractTunnel.md) | AbstractTunnel is an abstract superclass representing the common attributes a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConstructionEvent](ConstructionEvent.md) |
| Domain Of | [AbstractConstruction](AbstractConstruction.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractConstruction](AbstractConstruction.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:constructionEvent |
| native | citygml:constructionEvent |




## LinkML Source

<details>
```yaml
name: constructionEvent
description: Describes specific events in the life-time of the construction.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: constructionEvent
owner: AbstractConstruction
domain_of:
- AbstractConstruction
range: ConstructionEvent
required: false
multivalued: true

```
</details>