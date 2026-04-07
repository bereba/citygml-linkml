

# Slot: tunnelInstallation 



URI: [citygml:tunnelInstallation](https://www.ogc.org/standards/citygml/tunnelInstallation)
Alias: tunnelInstallation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HollowSpace](HollowSpace.md) | A HollowSpace is a space within a Tunnel or TunnelPart intended for certain f... |  no  |
| [TunnelPart](TunnelPart.md) | A TunnelPart is a physical or functional subdivision of a Tunnel |  no  |
| [Tunnel](Tunnel.md) | A Tunnel represents a horizontal or sloping enclosed passage way of a certain... |  no  |
| [AbstractTunnel](AbstractTunnel.md) | AbstractTunnel is an abstract superclass representing the common attributes a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AbstractTunnel](AbstractTunnel.md), [HollowSpace](HollowSpace.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:tunnelInstallation |
| native | citygml:tunnelInstallation |




## LinkML Source

<details>
```yaml
name: tunnelInstallation
alias: tunnelInstallation
domain_of:
- AbstractTunnel
- HollowSpace
range: string

```
</details>