

# Slot: adeOfFloorSurface 


_Augments the FloorSurface with properties defined in an ADE._





URI: [citygml:adeOfFloorSurface](https://www.ogc.org/standards/citygml/adeOfFloorSurface)
Alias: adeOfFloorSurface

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FloorSurface](FloorSurface.md) | A FloorSurface is surface that represents the interior floor of a constructio... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfFloorSurface](ADEOfFloorSurface.md) |
| Domain Of | [FloorSurface](FloorSurface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FloorSurface](FloorSurface.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfFloorSurface |
| native | citygml:adeOfFloorSurface |




## LinkML Source

<details>
```yaml
name: adeOfFloorSurface
description: Augments the FloorSurface with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfFloorSurface
owner: FloorSurface
domain_of:
- FloorSurface
range: ADEOfFloorSurface
required: false
multivalued: true

```
</details>