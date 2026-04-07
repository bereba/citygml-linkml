

# Slot: adeOfRoad 


_Augments the Road with properties defined in an ADE._





URI: [citygml:adeOfRoad](https://www.ogc.org/standards/citygml/adeOfRoad)
Alias: adeOfRoad

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Road](Road.md) | A Road is a transportation space used by vehicles, bicycles and/or pedestrian... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfRoad](ADEOfRoad.md) |
| Domain Of | [Road](Road.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Road](Road.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfRoad |
| native | citygml:adeOfRoad |




## LinkML Source

<details>
```yaml
name: adeOfRoad
description: Augments the Road with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfRoad
owner: Road
domain_of:
- Road
range: ADEOfRoad
required: false
multivalued: true

```
</details>