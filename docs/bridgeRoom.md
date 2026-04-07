

# Slot: bridgeRoom 


_Relates the rooms to the Bridge or BridgePart._





URI: [citygml:bridgeRoom](https://www.ogc.org/standards/citygml/bridgeRoom)
Alias: bridgeRoom

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BridgePart](BridgePart.md) | A BridgePart is a physical or functional subdivision of a Bridge |  no  |
| [Bridge](Bridge.md) | A Bridge represents a structure that affords the passage of pedestrians, anim... |  no  |
| [AbstractBridge](AbstractBridge.md) | AbstractBridge is an abstract superclass representing the common attributes a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BridgeRoom](BridgeRoom.md) |
| Domain Of | [AbstractBridge](AbstractBridge.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractBridge](AbstractBridge.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:bridgeRoom |
| native | citygml:bridgeRoom |




## LinkML Source

<details>
```yaml
name: bridgeRoom
description: Relates the rooms to the Bridge or BridgePart.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: bridgeRoom
owner: AbstractBridge
domain_of:
- AbstractBridge
range: BridgeRoom
required: false
multivalued: true

```
</details>