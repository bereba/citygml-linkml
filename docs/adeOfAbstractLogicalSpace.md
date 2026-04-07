

# Slot: adeOfAbstractLogicalSpace 


_Augments AbstractLogicalSpace with properties defined in an ADE._





URI: [citygml:adeOfAbstractLogicalSpace](https://www.ogc.org/standards/citygml/adeOfAbstractLogicalSpace)
Alias: adeOfAbstractLogicalSpace

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Storey](Storey.md) | A Storey is typically a horizontal section of a Building |  no  |
| [GenericLogicalSpace](GenericLogicalSpace.md) | A GenericLogicalSpace is a space that is not represented by any explicitly mo... |  no  |
| [AbstractBuildingSubdivision](AbstractBuildingSubdivision.md) | AbstractBuildingSubdivision is the abstract superclass for different kinds of... |  no  |
| [CityObjectGroup](CityObjectGroup.md) | A CityObjectGroup represents an application-specific aggregation of city obje... |  no  |
| [AbstractLogicalSpace](AbstractLogicalSpace.md) | AbstractLogicalSpace is the abstract superclass for all types of logical spac... |  no  |
| [BuildingUnit](BuildingUnit.md) | A BuildingUnit is a logical subdivision of a Building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractLogicalSpace](ADEOfAbstractLogicalSpace.md) |
| Domain Of | [AbstractLogicalSpace](AbstractLogicalSpace.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractLogicalSpace](AbstractLogicalSpace.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractLogicalSpace |
| native | citygml:adeOfAbstractLogicalSpace |




## LinkML Source

<details>
```yaml
name: adeOfAbstractLogicalSpace
description: Augments AbstractLogicalSpace with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractLogicalSpace
owner: AbstractLogicalSpace
domain_of:
- AbstractLogicalSpace
range: ADEOfAbstractLogicalSpace
required: false
multivalued: true

```
</details>