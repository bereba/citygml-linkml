

# Slot: adeOfBridgeRoom 


_Augments the BridgeRoom with properties defined in an ADE._





URI: [citygml:adeOfBridgeRoom](https://www.ogc.org/standards/citygml/adeOfBridgeRoom)
Alias: adeOfBridgeRoom

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BridgeRoom](BridgeRoom.md) | A BridgeRoom is a space within a Bridge or BridgePart intended for human occu... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfBridgeRoom](ADEOfBridgeRoom.md) |
| Domain Of | [BridgeRoom](BridgeRoom.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BridgeRoom](BridgeRoom.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfBridgeRoom |
| native | citygml:adeOfBridgeRoom |




## LinkML Source

<details>
```yaml
name: adeOfBridgeRoom
description: Augments the BridgeRoom with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfBridgeRoom
owner: BridgeRoom
domain_of:
- BridgeRoom
range: ADEOfBridgeRoom
required: false
multivalued: true

```
</details>