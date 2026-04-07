

# Slot: adeOfBuildingFurniture 


_Augments the BuildingFurniture with properties defined in an ADE._





URI: [citygml:adeOfBuildingFurniture](https://www.ogc.org/standards/citygml/adeOfBuildingFurniture)
Alias: adeOfBuildingFurniture

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BuildingFurniture](BuildingFurniture.md) | A BuildingFurniture is an equipment for occupant use, usually not fixed to th... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfBuildingFurniture](ADEOfBuildingFurniture.md) |
| Domain Of | [BuildingFurniture](BuildingFurniture.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BuildingFurniture](BuildingFurniture.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfBuildingFurniture |
| native | citygml:adeOfBuildingFurniture |




## LinkML Source

<details>
```yaml
name: adeOfBuildingFurniture
description: Augments the BuildingFurniture with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfBuildingFurniture
owner: BuildingFurniture
domain_of:
- BuildingFurniture
range: ADEOfBuildingFurniture
required: false
multivalued: true

```
</details>