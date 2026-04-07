

# Slot: adeOfTunnelInstallation 


_Augments the TunnelInstallation with properties defined in an ADE._





URI: [citygml:adeOfTunnelInstallation](https://www.ogc.org/standards/citygml/adeOfTunnelInstallation)
Alias: adeOfTunnelInstallation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TunnelInstallation](TunnelInstallation.md) | A TunnelInstallation is a permanent part of a Tunnel (inside and/or outside) ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfTunnelInstallation](ADEOfTunnelInstallation.md) |
| Domain Of | [TunnelInstallation](TunnelInstallation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TunnelInstallation](TunnelInstallation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfTunnelInstallation |
| native | citygml:adeOfTunnelInstallation |




## LinkML Source

<details>
```yaml
name: adeOfTunnelInstallation
description: Augments the TunnelInstallation with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfTunnelInstallation
owner: TunnelInstallation
domain_of:
- TunnelInstallation
range: ADEOfTunnelInstallation
required: false
multivalued: true

```
</details>