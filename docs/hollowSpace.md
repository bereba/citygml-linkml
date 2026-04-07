

# Slot: hollowSpace 


_Relates the hollow spaces to the Tunnel or TunnelPart._





URI: [citygml:hollowSpace](https://www.ogc.org/standards/citygml/hollowSpace)
Alias: hollowSpace

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
| Range | [HollowSpace](HollowSpace.md) |
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
| self | citygml:hollowSpace |
| native | citygml:hollowSpace |




## LinkML Source

<details>
```yaml
name: hollowSpace
description: Relates the hollow spaces to the Tunnel or TunnelPart.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: hollowSpace
owner: AbstractTunnel
domain_of:
- AbstractTunnel
range: HollowSpace
required: false
multivalued: true

```
</details>