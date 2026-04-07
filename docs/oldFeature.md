

# Slot: oldFeature 


_Relates to the version of the city object prior to the Transaction._





URI: [citygml:oldFeature](https://www.ogc.org/standards/citygml/oldFeature)
Alias: oldFeature

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transaction](Transaction.md) | Transaction represents a modification of the city model by the creation, term... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AbstractFeatureWithLifespan](AbstractFeatureWithLifespan.md) |
| Domain Of | [Transaction](Transaction.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Transaction](Transaction.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:oldFeature |
| native | citygml:oldFeature |




## LinkML Source

<details>
```yaml
name: oldFeature
description: Relates to the version of the city object prior to the Transaction.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: oldFeature
owner: Transaction
domain_of:
- Transaction
range: AbstractFeatureWithLifespan
required: false
multivalued: false

```
</details>