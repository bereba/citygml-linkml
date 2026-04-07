

# Slot: adeOfBuildingPart 


_Augments the BuildingPart with properties defined in an ADE._





URI: [citygml:adeOfBuildingPart](https://www.ogc.org/standards/citygml/adeOfBuildingPart)
Alias: adeOfBuildingPart

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BuildingPart](BuildingPart.md) | A BuildingPart is a physical or functional subdivision of a Building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfBuildingPart](ADEOfBuildingPart.md) |
| Domain Of | [BuildingPart](BuildingPart.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BuildingPart](BuildingPart.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfBuildingPart |
| native | citygml:adeOfBuildingPart |




## LinkML Source

<details>
```yaml
name: adeOfBuildingPart
description: Augments the BuildingPart with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfBuildingPart
owner: BuildingPart
domain_of:
- BuildingPart
range: ADEOfBuildingPart
required: false
multivalued: true

```
</details>