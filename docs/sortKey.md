

# Slot: sortKey 


_Defines an order among the objects that belong to the building subdivision. An example is the sorting of storeys._





URI: [citygml:sortKey](https://www.ogc.org/standards/citygml/sortKey)
Alias: sortKey

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) | AbstractBuildingSubdivision is the abstract superclass for different kinds of... |  no  |
| [Storey](Storey.md) | A Storey is typically a horizontal section of a Building |  no  |
| [BuildingUnit](BuildingUnit.md) | A BuildingUnit is a logical subdivision of a Building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:sortKey |
| native | citygml:sortKey |




## LinkML Source

<details>
```yaml
name: sortKey
description: Defines an order among the objects that belong to the building subdivision.
  An example is the sorting of storeys.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: sortKey
owner: AbstractBuildingSubdivision
domain_of:
- AbstractBuildingSubdivision
range: float
required: false
multivalued: false

```
</details>