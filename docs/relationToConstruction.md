

# Slot: relationToConstruction 


_Indicates whether the installation is located inside and/or outside of the construction._





URI: [citygml:relationToConstruction](https://www.ogc.org/standards/citygml/relationToConstruction)
Alias: relationToConstruction

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
| Range | [RelationToConstruction](RelationToConstruction.md) |
| Domain Of | [AbstractInstallation](AbstractInstallation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | citygml:relationToConstruction |
| native | citygml:relationToConstruction |




## LinkML Source

<details>
```yaml
name: relationToConstruction
description: Indicates whether the installation is located inside and/or outside of
  the construction.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: relationToConstruction
owner: AbstractInstallation
domain_of:
- AbstractInstallation
range: RelationToConstruction
required: false
multivalued: false

```
</details>