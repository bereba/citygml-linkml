

# Slot: tunnelPart 


_Relates the tunnel parts to the Tunnel._





URI: [citygml:tunnelPart](https://www.ogc.org/standards/citygml/tunnelPart)
Alias: tunnelPart

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tunnel](Tunnel.md) | A Tunnel represents a horizontal or sloping enclosed passage way of a certain... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TunnelPart](TunnelPart.md) |
| Domain Of | [Tunnel](Tunnel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Tunnel](Tunnel.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:tunnelPart |
| native | citygml:tunnelPart |




## LinkML Source

<details>
```yaml
name: tunnelPart
description: Relates the tunnel parts to the Tunnel.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: tunnelPart
owner: Tunnel
domain_of:
- Tunnel
range: TunnelPart
required: false
multivalued: true

```
</details>