

# Slot: adeOfAbstractInstallation 


_Augments AbstractInstallation with properties defined in an ADE._





URI: [citygml:adeOfAbstractInstallation](https://www.ogc.org/standards/citygml/adeOfAbstractInstallation)
Alias: adeOfAbstractInstallation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BuildingInstallation](BuildingInstallation.md) | A BuildingInstallation is a permanent part of a Building (inside and/or outsi... |  no  |
| [TunnelInstallation](TunnelInstallation.md) | A TunnelInstallation is a permanent part of a Tunnel (inside and/or outside) ... |  no  |
| [BridgeInstallation](BridgeInstallation.md) | A BridgeInstallation is a permanent part of a Bridge (inside and/or outside) ... |  no  |
| [AbstractInstallation](AbstractInstallation.md) | AbstractInstallation is the abstract superclass for the representation of ins... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractInstallation](ADEOfAbstractInstallation.md) |
| Domain Of | [AbstractInstallation](AbstractInstallation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractInstallation](AbstractInstallation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractInstallation |
| native | citygml:adeOfAbstractInstallation |




## LinkML Source

<details>
```yaml
name: adeOfAbstractInstallation
description: Augments AbstractInstallation with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractInstallation
owner: AbstractInstallation
domain_of:
- AbstractInstallation
range: ADEOfAbstractInstallation
required: false
multivalued: true

```
</details>