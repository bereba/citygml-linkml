

# Slot: adeOfAbstractBridge 


_Augments AbstractBridge with properties defined in an ADE._





URI: [citygml:adeOfAbstractBridge](https://www.ogc.org/standards/citygml/adeOfAbstractBridge)
Alias: adeOfAbstractBridge

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
| Range | [ADEOfAbstractBridge](ADEOfAbstractBridge.md) |
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
| self | citygml:adeOfAbstractBridge |
| native | citygml:adeOfAbstractBridge |




## LinkML Source

<details>
```yaml
name: adeOfAbstractBridge
description: Augments AbstractBridge with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractBridge
owner: AbstractBridge
domain_of:
- AbstractBridge
range: ADEOfAbstractBridge
required: false
multivalued: true

```
</details>