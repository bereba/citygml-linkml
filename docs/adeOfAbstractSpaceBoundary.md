

# Slot: adeOfAbstractSpaceBoundary 


_Augments AbstractSpaceBoundary with properties defined in an ADE._





URI: [citygml:adeOfAbstractSpaceBoundary](https://www.ogc.org/standards/citygml/adeOfAbstractSpaceBoundary)
Alias: adeOfAbstractSpaceBoundary

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
| [ReliefFeature](ReliefFeature.md) | A ReliefFeature is a collection of terrain components representing the Earth'... |  no  |
| [RoofSurface](RoofSurface.md) | A RoofSurface is a surface that delimits major roof parts of a construction |  no  |
| [WindowSurface](WindowSurface.md) | A WindowSurface is either a boundary surface of a Window feature or a surface... |  no  |
| [FloorSurface](FloorSurface.md) | A FloorSurface is surface that represents the interior floor of a constructio... |  no  |
| [LandUse](LandUse.md) | A LandUse object is an area of the earth's surface dedicated to a specific la... |  no  |
| [AbstractWaterBoundarySurface](AbstractWaterBoundarySurface.md) | AbstractWaterBoundarySurface is the abstract superclass for all kinds of them... |  no  |
| [CeilingSurface](CeilingSurface.md) | A CeilingSurface is a surface that represents the interior ceiling of a const... |  no  |
| [AbstractSpaceBoundary](AbstractSpaceBoundary.md) | AbstractSpaceBoundary is the abstract superclass for all types of space bound... |  no  |
| [AuxiliaryTrafficArea](AuxiliaryTrafficArea.md) | An AuxiliaryTrafficArea is the ground surface of an AuxiliaryTrafficSpace |  no  |
| [DoorSurface](DoorSurface.md) | A DoorSurface is either a boundary surface of a Door feature or a surface tha... |  no  |
| [TINRelief](TINRelief.md) | A TINRelief represents a terrain component as a triangulated irregular networ... |  no  |
| [AbstractFillingSurface](AbstractFillingSurface.md) | AbstractFillingSurface is the abstract superclass for different kinds of surf... |  no  |
| [BreaklineRelief](BreaklineRelief.md) | A BreaklineRelief represents a terrain component with 3D lines |  no  |
| [RasterRelief](RasterRelief.md) | A RasterRelief represents a terrain component as a regular raster or grid |  no  |
| [InteriorWallSurface](InteriorWallSurface.md) | An InteriorWallSurface is a surface that is visible from inside a constructio... |  no  |
| [MassPointRelief](MassPointRelief.md) | A MassPointRelief represents a terrain component as a collection of 3D points |  no  |
| [Marking](Marking.md) | A Marking is a visible pattern on a transportation area relevant to the struc... |  no  |
| [GenericThematicSurface](GenericThematicSurface.md) | A GenericThematicSurface is a surface that is not represented by any explicit... |  no  |
| [WaterGroundSurface](WaterGroundSurface.md) | A WaterGroundSurface represents the exterior boundary surface of the submerge... |  no  |
| [AbstractReliefComponent](AbstractReliefComponent.md) | An AbstractReliefComponent represents an element of the terrain surface - eit... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractSpaceBoundary](ADEOfAbstractSpaceBoundary.md) |
| Domain Of | [AbstractSpaceBoundary](AbstractSpaceBoundary.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractSpaceBoundary](AbstractSpaceBoundary.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractSpaceBoundary |
| native | citygml:adeOfAbstractSpaceBoundary |




## LinkML Source

<details>
```yaml
name: adeOfAbstractSpaceBoundary
description: Augments AbstractSpaceBoundary with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractSpaceBoundary
owner: AbstractSpaceBoundary
domain_of:
- AbstractSpaceBoundary
range: ADEOfAbstractSpaceBoundary
required: false
multivalued: true

```
</details>