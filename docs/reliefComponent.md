

# Slot: reliefComponent 


_Relates to the terrain components that are part of the ReliefFeature._





URI: [citygml:reliefComponent](https://www.ogc.org/standards/citygml/reliefComponent)
Alias: reliefComponent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReliefFeature](ReliefFeature.md) | A ReliefFeature is a collection of terrain components representing the Earth'... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AbstractReliefComponent](AbstractReliefComponent.md) |
| Domain Of | [ReliefFeature](ReliefFeature.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | citygml:reliefComponent |
| native | citygml:reliefComponent |




## LinkML Source

<details>
```yaml
name: reliefComponent
description: Relates to the terrain components that are part of the ReliefFeature.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: reliefComponent
owner: ReliefFeature
domain_of:
- ReliefFeature
range: AbstractReliefComponent
required: true
multivalued: true

```
</details>