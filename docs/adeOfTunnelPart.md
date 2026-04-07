

# Slot: adeOfTunnelPart 


_Augments the TunnelPart with properties defined in an ADE._





URI: [citygml:adeOfTunnelPart](https://www.ogc.org/standards/citygml/adeOfTunnelPart)
Alias: adeOfTunnelPart

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TunnelPart](TunnelPart.md) | A TunnelPart is a physical or functional subdivision of a Tunnel |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfTunnelPart](ADEOfTunnelPart.md) |
| Domain Of | [TunnelPart](TunnelPart.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TunnelPart](TunnelPart.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfTunnelPart |
| native | citygml:adeOfTunnelPart |




## LinkML Source

<details>
```yaml
name: adeOfTunnelPart
description: Augments the TunnelPart with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfTunnelPart
owner: TunnelPart
domain_of:
- TunnelPart
range: ADEOfTunnelPart
required: false
multivalued: true

```
</details>