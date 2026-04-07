

# Slot: tunnelConstructiveElement 


_Relates the constructive elements to the Tunnel or TunnelPart._





URI: [citygml:tunnelConstructiveElement](https://www.ogc.org/standards/citygml/tunnelConstructiveElement)
Alias: tunnelConstructiveElement

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
| Range | [TunnelConstructiveElement](TunnelConstructiveElement.md) |
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
| self | citygml:tunnelConstructiveElement |
| native | citygml:tunnelConstructiveElement |




## LinkML Source

<details>
```yaml
name: tunnelConstructiveElement
description: Relates the constructive elements to the Tunnel or TunnelPart.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: tunnelConstructiveElement
owner: AbstractTunnel
domain_of:
- AbstractTunnel
range: TunnelConstructiveElement
required: false
multivalued: true

```
</details>