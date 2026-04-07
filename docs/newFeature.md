

# Slot: newFeature 


_Relates to the version of the city object subsequent to the Transaction._





URI: [citygml:newFeature](https://www.ogc.org/standards/citygml/newFeature)
Alias: newFeature

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
| self | citygml:newFeature |
| native | citygml:newFeature |




## LinkML Source

<details>
```yaml
name: newFeature
description: Relates to the version of the city object subsequent to the Transaction.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: newFeature
owner: Transaction
domain_of:
- Transaction
range: AbstractFeatureWithLifespan
required: false
multivalued: false

```
</details>