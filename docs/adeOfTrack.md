

# Slot: adeOfTrack 


_Augments the Track with properties defined in an ADE._





URI: [citygml:adeOfTrack](https://www.ogc.org/standards/citygml/adeOfTrack)
Alias: adeOfTrack

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Track](Track.md) | A Track is a small path mainly used by pedestrians |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfTrack](ADEOfTrack.md) |
| Domain Of | [Track](Track.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Track](Track.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfTrack |
| native | citygml:adeOfTrack |




## LinkML Source

<details>
```yaml
name: adeOfTrack
description: Augments the Track with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfTrack
owner: Track
domain_of:
- Track
range: ADEOfTrack
required: false
multivalued: true

```
</details>