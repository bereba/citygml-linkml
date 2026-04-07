

# Slot: adeOfReliefFeature 


_Augments the ReliefFeature with properties defined in an ADE._





URI: [citygml:adeOfReliefFeature](https://www.ogc.org/standards/citygml/adeOfReliefFeature)
Alias: adeOfReliefFeature

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReliefFeature](ReliefFeature.md) | A ReliefFeature is a collection of terrain components representing the Earth'... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfReliefFeature](ADEOfReliefFeature.md) |
| Domain Of | [ReliefFeature](ReliefFeature.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ReliefFeature](ReliefFeature.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfReliefFeature |
| native | citygml:adeOfReliefFeature |




## LinkML Source

<details>
```yaml
name: adeOfReliefFeature
description: Augments the ReliefFeature with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfReliefFeature
owner: ReliefFeature
domain_of:
- ReliefFeature
range: ADEOfReliefFeature
required: false
multivalued: true

```
</details>