

# Slot: adeOfVersionTransition 


_Augments the VersionTransition with properties defined in an ADE._





URI: [citygml:adeOfVersionTransition](https://www.ogc.org/standards/citygml/adeOfVersionTransition)
Alias: adeOfVersionTransition

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VersionTransition](VersionTransition.md) | VersionTransition describes the change of the state of a city model from one ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfVersionTransition](ADEOfVersionTransition.md) |
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
| self | citygml:adeOfVersionTransition |
| native | citygml:adeOfVersionTransition |




## LinkML Source

<details>
```yaml
name: adeOfVersionTransition
description: Augments the VersionTransition with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfVersionTransition
owner: VersionTransition
domain_of:
- VersionTransition
range: ADEOfVersionTransition
required: false
multivalued: true

```
</details>