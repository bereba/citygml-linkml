

# Slot: lod1MultiSurface 


_Relates to a 3D MultiSurface geometry that represents the thematic surface in Level of Detail 1._





URI: [citygml:lod1MultiSurface](https://www.ogc.org/standards/citygml/lod1MultiSurface)
Alias: lod1MultiSurface

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OuterFloorSurface](OuterFloorSurface.md) | An OuterFloorSurface is a surface that belongs to the outer construction shel... |  no  |
| [TrafficArea](TrafficArea.md) | A TrafficArea is the ground surface of a TrafficSpace |  no  |
| [AbstractThematicSurface](AbstractThematicSurface.md) | AbstractThematicSurface is the abstract superclass for all types of thematic ... |  no  |
| [GroundSurface](GroundSurface.md) | A GroundSurface is a surface that represents the ground plate of a constructi... |  no  |
| [WallSurface](WallSurface.md) | A WallSurface is a surface that is part of the building facade visible from t... |  no  |
| [HoleSurface](HoleSurface.md) | A HoleSurface is a representation of the ground surface of a hole |  no  |
| [AbstractConstructionSurface](AbstractConstructionSurface.md) | AbstractConstructionSurface is the abstract superclass for different kinds of... |  no  |
| [WaterSurface](WaterSurface.md) | A WaterSurface represents the upper exterior interface between a water body a... |  no  |
| [OuterCeilingSurface](OuterCeilingSurface.md) | An OuterCeilingSurface is a surface that belongs to the outer building shell ... |  no  |
| [ClosureSurface](ClosureSurface.md) | ClosureSurface is a special type of thematic surface used to close holes in v... |  no  |
| [RoofSurface](RoofSurface.md) | A RoofSurface is a surface that delimits major roof parts of a construction |  no  |
| [WindowSurface](WindowSurface.md) | A WindowSurface is either a boundary surface of a Window feature or a surface... |  no  |
| [FloorSurface](FloorSurface.md) | A FloorSurface is surface that represents the interior floor of a constructio... |  no  |
| [LandUse](LandUse.md) | A LandUse object is an area of the earth's surface dedicated to a specific la... |  no  |
| [AbstractWaterBoundarySurface](AbstractWaterBoundarySurface.md) | AbstractWaterBoundarySurface is the abstract superclass for all kinds of them... |  no  |
| [CeilingSurface](CeilingSurface.md) | A CeilingSurface is a surface that represents the interior ceiling of a const... |  no  |
| [AuxiliaryTrafficArea](AuxiliaryTrafficArea.md) | An AuxiliaryTrafficArea is the ground surface of an AuxiliaryTrafficSpace |  no  |
| [DoorSurface](DoorSurface.md) | A DoorSurface is either a boundary surface of a Door feature or a surface tha... |  no  |
| [AbstractFillingSurface](AbstractFillingSurface.md) | AbstractFillingSurface is the abstract superclass for different kinds of surf... |  no  |
| [InteriorWallSurface](InteriorWallSurface.md) | An InteriorWallSurface is a surface that is visible from inside a constructio... |  no  |
| [Marking](Marking.md) | A Marking is a visible pattern on a transportation area relevant to the struc... |  no  |
| [GenericThematicSurface](GenericThematicSurface.md) | A GenericThematicSurface is a surface that is not represented by any explicit... |  no  |
| [WaterGroundSurface](WaterGroundSurface.md) | A WaterGroundSurface represents the exterior boundary surface of the submerge... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AbstractThematicSurface](AbstractThematicSurface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractThematicSurface](AbstractThematicSurface.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:lod1MultiSurface |
| native | citygml:lod1MultiSurface |




## LinkML Source

<details>
```yaml
name: lod1MultiSurface
description: Relates to a 3D MultiSurface geometry that represents the thematic surface
  in Level of Detail 1.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: lod1MultiSurface
owner: AbstractThematicSurface
domain_of:
- AbstractThematicSurface
range: string
required: false
multivalued: false

```
</details>