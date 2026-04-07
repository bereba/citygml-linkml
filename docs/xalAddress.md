

# Slot: xalAddress 


_Relates an OASIS address object to the Address._





URI: [citygml:xalAddress](https://www.ogc.org/standards/citygml/xalAddress)
Alias: xalAddress

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Address](Address.md) | Address represents an address of a city object |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [XALAddress](XALAddress.md) |
| Domain Of | [Address](Address.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | citygml:xalAddress |
| native | citygml:xalAddress |




## LinkML Source

<details>
```yaml
name: xalAddress
description: Relates an OASIS address object to the Address.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: xalAddress
owner: Address
domain_of:
- Address
range: XALAddress
required: true
multivalued: false

```
</details>