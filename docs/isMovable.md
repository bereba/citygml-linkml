

# Slot: isMovable 


_Indicates whether the Bridge or BridgePart can be moved to allow for watercraft to pass._





URI: [citygml:isMovable](https://www.ogc.org/standards/citygml/isMovable)
Alias: isMovable

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
| Range | [Boolean](Boolean.md) |
| Domain Of | [AbstractBridge](AbstractBridge.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | citygml:isMovable |
| native | citygml:isMovable |




## LinkML Source

<details>
```yaml
name: isMovable
description: Indicates whether the Bridge or BridgePart can be moved to allow for
  watercraft to pass.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: isMovable
owner: AbstractBridge
domain_of:
- AbstractBridge
range: boolean
required: false
multivalued: false

```
</details>