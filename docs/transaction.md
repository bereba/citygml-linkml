

# Slot: transaction 


_Relates to all transactions that have been applied as part of the VersionTransition._





URI: [citygml:transaction](https://www.ogc.org/standards/citygml/transaction)
Alias: transaction

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VersionTransition](VersionTransition.md) | VersionTransition describes the change of the state of a city model from one ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Transaction](Transaction.md) |
| Domain Of | [VersionTransition](VersionTransition.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [VersionTransition](VersionTransition.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:transaction |
| native | citygml:transaction |




## LinkML Source

<details>
```yaml
name: transaction
description: Relates to all transactions that have been applied as part of the VersionTransition.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: transaction
owner: VersionTransition
domain_of:
- VersionTransition
range: Transaction
required: false
multivalued: true

```
</details>