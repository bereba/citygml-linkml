

# Slot: buildingUnit 


_Relates to the building units that belong to the Storey._





URI: [citygml:buildingUnit](https://www.ogc.org/standards/citygml/buildingUnit)
Alias: buildingUnit

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Storey](Storey.md) | A Storey is typically a horizontal section of a Building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BuildingUnit](BuildingUnit.md) |
| Domain Of | [Storey](Storey.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Storey](Storey.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:buildingUnit |
| native | citygml:buildingUnit |




## LinkML Source

<details>
```yaml
name: buildingUnit
description: Relates to the building units that belong to the Storey.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: buildingUnit
owner: Storey
domain_of:
- Storey
range: BuildingUnit
required: false
multivalued: true

```
</details>