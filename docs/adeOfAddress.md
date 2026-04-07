

# Slot: adeOfAddress 


_Augments the Address with properties defined in an ADE._





URI: [citygml:adeOfAddress](https://www.ogc.org/standards/citygml/adeOfAddress)
Alias: adeOfAddress

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Address](Address.md) | Address represents an address of a city object |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAddress](ADEOfAddress.md) |
| Domain Of | [Address](Address.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Address](Address.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAddress |
| native | citygml:adeOfAddress |




## LinkML Source

<details>
```yaml
name: adeOfAddress
description: Augments the Address with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAddress
owner: Address
domain_of:
- Address
range: ADEOfAddress
required: false
multivalued: true

```
</details>