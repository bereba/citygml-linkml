

# Slot: adeOfBuildingUnit 


_Augments the BuildingUnit with properties defined in an ADE._





URI: [citygml:adeOfBuildingUnit](https://www.ogc.org/standards/citygml/adeOfBuildingUnit)
Alias: adeOfBuildingUnit

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BuildingUnit](BuildingUnit.md) | A BuildingUnit is a logical subdivision of a Building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfBuildingUnit](ADEOfBuildingUnit.md) |
| Domain Of | [BuildingUnit](BuildingUnit.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BuildingUnit](BuildingUnit.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfBuildingUnit |
| native | citygml:adeOfBuildingUnit |




## LinkML Source

<details>
```yaml
name: adeOfBuildingUnit
description: Augments the BuildingUnit with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfBuildingUnit
owner: BuildingUnit
domain_of:
- BuildingUnit
range: ADEOfBuildingUnit
required: false
multivalued: true

```
</details>