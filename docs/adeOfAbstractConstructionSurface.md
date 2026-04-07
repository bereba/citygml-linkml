

# Slot: adeOfAbstractConstructionSurface 


_Augments AbstractConstructionSurface with properties defined in an ADE._





URI: [citygml:adeOfAbstractConstructionSurface](https://www.ogc.org/standards/citygml/adeOfAbstractConstructionSurface)
Alias: adeOfAbstractConstructionSurface

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OuterFloorSurface](OuterFloorSurface.md) | An OuterFloorSurface is a surface that belongs to the outer construction shel... |  no  |
| [AbstractConstructionSurface](AbstractConstructionSurface.md) | AbstractConstructionSurface is the abstract superclass for different kinds of... |  no  |
| [FloorSurface](FloorSurface.md) | A FloorSurface is surface that represents the interior floor of a constructio... |  no  |
| [WallSurface](WallSurface.md) | A WallSurface is a surface that is part of the building facade visible from t... |  no  |
| [InteriorWallSurface](InteriorWallSurface.md) | An InteriorWallSurface is a surface that is visible from inside a constructio... |  no  |
| [CeilingSurface](CeilingSurface.md) | A CeilingSurface is a surface that represents the interior ceiling of a const... |  no  |
| [OuterCeilingSurface](OuterCeilingSurface.md) | An OuterCeilingSurface is a surface that belongs to the outer building shell ... |  no  |
| [GroundSurface](GroundSurface.md) | A GroundSurface is a surface that represents the ground plate of a constructi... |  no  |
| [RoofSurface](RoofSurface.md) | A RoofSurface is a surface that delimits major roof parts of a construction |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractConstructionSurface](ADEOfAbstractConstructionSurface.md) |
| Domain Of | [AbstractConstructionSurface](AbstractConstructionSurface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractConstructionSurface](AbstractConstructionSurface.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractConstructionSurface |
| native | citygml:adeOfAbstractConstructionSurface |




## LinkML Source

<details>
```yaml
name: adeOfAbstractConstructionSurface
description: Augments AbstractConstructionSurface with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractConstructionSurface
owner: AbstractConstructionSurface
domain_of:
- AbstractConstructionSurface
range: ADEOfAbstractConstructionSurface
required: false
multivalued: true

```
</details>