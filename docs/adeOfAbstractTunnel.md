

# Slot: adeOfAbstractTunnel 


_Augments AbstractTunnel with properties defined in an ADE._





URI: [citygml:adeOfAbstractTunnel](https://www.ogc.org/standards/citygml/adeOfAbstractTunnel)
Alias: adeOfAbstractTunnel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TunnelPart](TunnelPart.md) | A TunnelPart is a physical or functional subdivision of a Tunnel |  no  |
| [Tunnel](Tunnel.md) | A Tunnel represents a horizontal or sloping enclosed passage way of a certain... |  no  |
| [AbstractTunnel](AbstractTunnel.md) | AbstractTunnel is an abstract superclass representing the common attributes a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractTunnel](ADEOfAbstractTunnel.md) |
| Domain Of | [AbstractTunnel](AbstractTunnel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractTunnel](AbstractTunnel.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractTunnel |
| native | citygml:adeOfAbstractTunnel |




## LinkML Source

<details>
```yaml
name: adeOfAbstractTunnel
description: Augments AbstractTunnel with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractTunnel
owner: AbstractTunnel
domain_of:
- AbstractTunnel
range: ADEOfAbstractTunnel
required: false
multivalued: true

```
</details>