

# Slot: bridgePart 


_Relates the bridge parts to the Bridge._





URI: [citygml:bridgePart](https://www.ogc.org/standards/citygml/bridgePart)
Alias: bridgePart

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bridge](Bridge.md) | A Bridge represents a structure that affords the passage of pedestrians, anim... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BridgePart](BridgePart.md) |
| Domain Of | [Bridge](Bridge.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Bridge](Bridge.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:bridgePart |
| native | citygml:bridgePart |




## LinkML Source

<details>
```yaml
name: bridgePart
description: Relates the bridge parts to the Bridge.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: bridgePart
owner: Bridge
domain_of:
- Bridge
range: BridgePart
required: false
multivalued: true

```
</details>