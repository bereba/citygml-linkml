

# Slot: adeOfPlantCover 


_Augments the PlantCover with properties defined in an ADE._





URI: [citygml:adeOfPlantCover](https://www.ogc.org/standards/citygml/adeOfPlantCover)
Alias: adeOfPlantCover

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantCover](PlantCover.md) | A PlantCover represents a space covered by vegetation |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfPlantCover](ADEOfPlantCover.md) |
| Domain Of | [PlantCover](PlantCover.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PlantCover](PlantCover.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfPlantCover |
| native | citygml:adeOfPlantCover |




## LinkML Source

<details>
```yaml
name: adeOfPlantCover
description: Augments the PlantCover with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfPlantCover
owner: PlantCover
domain_of:
- PlantCover
range: ADEOfPlantCover
required: false
multivalued: true

```
</details>