

# Slot: adeOfAbstractBuilding 


_Augments AbstractBuilding with properties defined in an ADE._





URI: [citygml:adeOfAbstractBuilding](https://www.ogc.org/standards/citygml/adeOfAbstractBuilding)
Alias: adeOfAbstractBuilding

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Building](Building.md) | A Building is a free-standing, self-supporting construction that is roofed, u... |  no  |
| [AbstractBuilding](AbstractBuilding.md) | AbstractBuilding is an abstract superclass representing the common attributes... |  no  |
| [BuildingPart](BuildingPart.md) | A BuildingPart is a physical or functional subdivision of a Building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractBuilding](ADEOfAbstractBuilding.md) |
| Domain Of | [AbstractBuilding](AbstractBuilding.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractBuilding](AbstractBuilding.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractBuilding |
| native | citygml:adeOfAbstractBuilding |




## LinkML Source

<details>
```yaml
name: adeOfAbstractBuilding
description: Augments AbstractBuilding with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractBuilding
owner: AbstractBuilding
domain_of:
- AbstractBuilding
range: ADEOfAbstractBuilding
required: false
multivalued: true

```
</details>