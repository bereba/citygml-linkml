

# Slot: adeOfBridgeInstallation 


_Augments the BridgeInstallation with properties defined in an ADE._





URI: [citygml:adeOfBridgeInstallation](https://www.ogc.org/standards/citygml/adeOfBridgeInstallation)
Alias: adeOfBridgeInstallation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BridgeInstallation](BridgeInstallation.md) | A BridgeInstallation is a permanent part of a Bridge (inside and/or outside) ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfBridgeInstallation](ADEOfBridgeInstallation.md) |
| Domain Of | [BridgeInstallation](BridgeInstallation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BridgeInstallation](BridgeInstallation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfBridgeInstallation |
| native | citygml:adeOfBridgeInstallation |




## LinkML Source

<details>
```yaml
name: adeOfBridgeInstallation
description: Augments the BridgeInstallation with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfBridgeInstallation
owner: BridgeInstallation
domain_of:
- BridgeInstallation
range: ADEOfBridgeInstallation
required: false
multivalued: true

```
</details>