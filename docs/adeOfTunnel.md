

# Slot: adeOfTunnel 


_Augments the Tunnel with properties defined in an ADE._





URI: [citygml:adeOfTunnel](https://www.ogc.org/standards/citygml/adeOfTunnel)
Alias: adeOfTunnel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tunnel](Tunnel.md) | A Tunnel represents a horizontal or sloping enclosed passage way of a certain... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfTunnel](ADEOfTunnel.md) |
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
| self | citygml:adeOfTunnel |
| native | citygml:adeOfTunnel |




## LinkML Source

<details>
```yaml
name: adeOfTunnel
description: Augments the Tunnel with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfTunnel
owner: Tunnel
domain_of:
- Tunnel
range: ADEOfTunnel
required: false
multivalued: true

```
</details>