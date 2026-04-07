

# Slot: adeOfVersion 


_Augments the Version with properties defined in an ADE._





URI: [citygml:adeOfVersion](https://www.ogc.org/standards/citygml/adeOfVersion)
Alias: adeOfVersion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Version](Version.md) | Version represents a defined state of a city model consisting of the dedicate... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfVersion](ADEOfVersion.md) |
| Domain Of | [Version](Version.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Version](Version.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfVersion |
| native | citygml:adeOfVersion |




## LinkML Source

<details>
```yaml
name: adeOfVersion
description: Augments the Version with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfVersion
owner: Version
domain_of:
- Version
range: ADEOfVersion
required: false
multivalued: true

```
</details>