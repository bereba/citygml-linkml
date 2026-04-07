

# Slot: adeOfInteriorWallSurface 


_Augments the InteriorWallSurface with properties defined in an ADE._





URI: [citygml:adeOfInteriorWallSurface](https://www.ogc.org/standards/citygml/adeOfInteriorWallSurface)
Alias: adeOfInteriorWallSurface

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InteriorWallSurface](InteriorWallSurface.md) | An InteriorWallSurface is a surface that is visible from inside a constructio... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfInteriorWallSurface](ADEOfInteriorWallSurface.md) |
| Domain Of | [InteriorWallSurface](InteriorWallSurface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [InteriorWallSurface](InteriorWallSurface.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfInteriorWallSurface |
| native | citygml:adeOfInteriorWallSurface |




## LinkML Source

<details>
```yaml
name: adeOfInteriorWallSurface
description: Augments the InteriorWallSurface with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfInteriorWallSurface
owner: InteriorWallSurface
domain_of:
- InteriorWallSurface
range: ADEOfInteriorWallSurface
required: false
multivalued: true

```
</details>