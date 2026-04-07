

# Slot: reason 


_Specifies why the VersionTransition has been carried out._





URI: [citygml:reason](https://www.ogc.org/standards/citygml/reason)
Alias: reason

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VersionTransition](VersionTransition.md) | VersionTransition describes the change of the state of a city model from one ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [VersionTransition](VersionTransition.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | citygml:reason |
| native | citygml:reason |




## LinkML Source

<details>
```yaml
name: reason
description: Specifies why the VersionTransition has been carried out.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: reason
owner: VersionTransition
domain_of:
- VersionTransition
range: string
required: false
multivalued: false

```
</details>