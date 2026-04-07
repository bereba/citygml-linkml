

# Slot: adeOfAbstractBuildingSubdivision 


_Augments AbstractBuildingSubdivision with properties defined in an ADE._





URI: [citygml:adeOfAbstractBuildingSubdivision](https://www.ogc.org/standards/citygml/adeOfAbstractBuildingSubdivision)
Alias: adeOfAbstractBuildingSubdivision

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
| Range | [ADEOfAbstractBuildingSubdivision](ADEOfAbstractBuildingSubdivision.md) |
| Domain Of | [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | citygml:adeOfAbstractBuildingSubdivision |
| native | citygml:adeOfAbstractBuildingSubdivision |




## LinkML Source

<details>
```yaml
name: adeOfAbstractBuildingSubdivision
description: Augments AbstractBuildingSubdivision with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractBuildingSubdivision
owner: AbstractBuildingSubdivision
domain_of:
- AbstractBuildingSubdivision
range: ADEOfAbstractBuildingSubdivision
required: false
multivalued: true

```
</details>