

# Slot: adeOfWaterway 


_Augments the Waterway with properties defined in an ADE._





URI: [citygml:adeOfWaterway](https://www.ogc.org/standards/citygml/adeOfWaterway)
Alias: adeOfWaterway

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Waterway](Waterway.md) | A Waterway is a transportation space used for the movement of vessels upon or... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfWaterway](ADEOfWaterway.md) |
| Domain Of | [Waterway](Waterway.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Waterway](Waterway.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfWaterway |
| native | citygml:adeOfWaterway |




## LinkML Source

<details>
```yaml
name: adeOfWaterway
description: Augments the Waterway with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfWaterway
owner: Waterway
domain_of:
- Waterway
range: ADEOfWaterway
required: false
multivalued: true

```
</details>