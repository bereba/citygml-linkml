

# Slot: adeOfBridge 


_Augments the Bridge with properties defined in an ADE._





URI: [citygml:adeOfBridge](https://www.ogc.org/standards/citygml/adeOfBridge)
Alias: adeOfBridge

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bridge](Bridge.md) | A Bridge represents a structure that affords the passage of pedestrians, anim... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfBridge](ADEOfBridge.md) |
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
| self | citygml:adeOfBridge |
| native | citygml:adeOfBridge |




## LinkML Source

<details>
```yaml
name: adeOfBridge
description: Augments the Bridge with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfBridge
owner: Bridge
domain_of:
- Bridge
range: ADEOfBridge
required: false
multivalued: true

```
</details>