

# Slot: adeOfBridgePart 


_Augments the BridgePart with properties defined in an ADE._





URI: [citygml:adeOfBridgePart](https://www.ogc.org/standards/citygml/adeOfBridgePart)
Alias: adeOfBridgePart

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BridgePart](BridgePart.md) | A BridgePart is a physical or functional subdivision of a Bridge |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfBridgePart](ADEOfBridgePart.md) |
| Domain Of | [BridgePart](BridgePart.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BridgePart](BridgePart.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfBridgePart |
| native | citygml:adeOfBridgePart |




## LinkML Source

<details>
```yaml
name: adeOfBridgePart
description: Augments the BridgePart with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfBridgePart
owner: BridgePart
domain_of:
- BridgePart
range: ADEOfBridgePart
required: false
multivalued: true

```
</details>