

# Slot: adeOfAbstractVersion 


_Augments AbstractVersion with properties defined in an ADE._





URI: [citygml:adeOfAbstractVersion](https://www.ogc.org/standards/citygml/adeOfAbstractVersion)
Alias: adeOfAbstractVersion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Version](Version.md) | Version represents a defined state of a city model consisting of the dedicate... |  no  |
| [AbstractVersion](AbstractVersion.md) | AbstractVersion is the abstract superclass to represent Version objects |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractVersion](ADEOfAbstractVersion.md) |
| Domain Of | [AbstractVersion](AbstractVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractVersion](AbstractVersion.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractVersion |
| native | citygml:adeOfAbstractVersion |




## LinkML Source

<details>
```yaml
name: adeOfAbstractVersion
description: Augments AbstractVersion with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractVersion
owner: AbstractVersion
domain_of:
- AbstractVersion
range: ADEOfAbstractVersion
required: false
multivalued: true

```
</details>