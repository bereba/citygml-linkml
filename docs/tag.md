

# Slot: tag 


_Allows for adding keywords to the city model version._





URI: [citygml:tag](https://www.ogc.org/standards/citygml/tag)
Alias: tag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Version](Version.md) | Version represents a defined state of a city model consisting of the dedicate... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | citygml:tag |
| native | citygml:tag |




## LinkML Source

<details>
```yaml
name: tag
description: Allows for adding keywords to the city model version.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: tag
owner: Version
domain_of:
- Version
range: string
required: false
multivalued: true

```
</details>