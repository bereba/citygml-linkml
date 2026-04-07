

# Slot: type 



URI: [citygml:type](https://www.ogc.org/standards/citygml/type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VersionTransition](VersionTransition.md) | VersionTransition describes the change of the state of a city model from one ... |  no  |
| [Transaction](Transaction.md) | Transaction represents a modification of the city model by the creation, term... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Transaction](Transaction.md), [VersionTransition](VersionTransition.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:type |
| native | citygml:type |




## LinkML Source

<details>
```yaml
name: type
alias: type
domain_of:
- Transaction
- VersionTransition
range: string

```
</details>