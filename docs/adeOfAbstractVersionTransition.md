

# Slot: adeOfAbstractVersionTransition 


_Augments AbstractVersionTransition with properties defined in an ADE._





URI: [citygml:adeOfAbstractVersionTransition](https://www.ogc.org/standards/citygml/adeOfAbstractVersionTransition)
Alias: adeOfAbstractVersionTransition

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VersionTransition](VersionTransition.md) | VersionTransition describes the change of the state of a city model from one ... |  no  |
| [AbstractVersionTransition](AbstractVersionTransition.md) | AbstractVersionTransition is the abstract superclass to represent VersionTran... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractVersionTransition](ADEOfAbstractVersionTransition.md) |
| Domain Of | [AbstractVersionTransition](AbstractVersionTransition.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractVersionTransition](AbstractVersionTransition.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractVersionTransition |
| native | citygml:adeOfAbstractVersionTransition |




## LinkML Source

<details>
```yaml
name: adeOfAbstractVersionTransition
description: Augments AbstractVersionTransition with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractVersionTransition
owner: AbstractVersionTransition
domain_of:
- AbstractVersionTransition
range: ADEOfAbstractVersionTransition
required: false
multivalued: true

```
</details>