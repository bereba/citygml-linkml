

# Slot: clonePredecessor 


_Indicates whether the set of city object instances belonging to the successor version of the city model is either explicitly enumerated within the successor version object (attribute clonePredecessor=false),  or has to be derived from the modifications of the city model provided as a list of transactions on the city object versions contained in the predecessor version (attribute clonePredecessor=true)._





URI: [citygml:clonePredecessor](https://www.ogc.org/standards/citygml/clonePredecessor)
Alias: clonePredecessor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VersionTransition](VersionTransition.md) | VersionTransition describes the change of the state of a city model from one ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [VersionTransition](VersionTransition.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | citygml:clonePredecessor |
| native | citygml:clonePredecessor |




## LinkML Source

<details>
```yaml
name: clonePredecessor
description: Indicates whether the set of city object instances belonging to the successor
  version of the city model is either explicitly enumerated within the successor version
  object (attribute clonePredecessor=false),  or has to be derived from the modifications
  of the city model provided as a list of transactions on the city object versions
  contained in the predecessor version (attribute clonePredecessor=true).
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: clonePredecessor
owner: VersionTransition
domain_of:
- VersionTransition
range: boolean
required: true
multivalued: false

```
</details>