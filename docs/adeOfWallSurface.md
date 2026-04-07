

# Slot: adeOfWallSurface 


_Augments the WallSurface with properties defined in an ADE._





URI: [citygml:adeOfWallSurface](https://www.ogc.org/standards/citygml/adeOfWallSurface)
Alias: adeOfWallSurface

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WallSurface](WallSurface.md) | A WallSurface is a surface that is part of the building facade visible from t... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfWallSurface](ADEOfWallSurface.md) |
| Domain Of | [WallSurface](WallSurface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [WallSurface](WallSurface.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfWallSurface |
| native | citygml:adeOfWallSurface |




## LinkML Source

<details>
```yaml
name: adeOfWallSurface
description: Augments the WallSurface with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfWallSurface
owner: WallSurface
domain_of:
- WallSurface
range: ADEOfWallSurface
required: false
multivalued: true

```
</details>