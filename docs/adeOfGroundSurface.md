

# Slot: adeOfGroundSurface 


_Augments the GroundSurface with properties defined in an ADE._





URI: [citygml:adeOfGroundSurface](https://www.ogc.org/standards/citygml/adeOfGroundSurface)
Alias: adeOfGroundSurface

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GroundSurface](GroundSurface.md) | A GroundSurface is a surface that represents the ground plate of a constructi... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfGroundSurface](ADEOfGroundSurface.md) |
| Domain Of | [GroundSurface](GroundSurface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [GroundSurface](GroundSurface.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfGroundSurface |
| native | citygml:adeOfGroundSurface |




## LinkML Source

<details>
```yaml
name: adeOfGroundSurface
description: Augments the GroundSurface with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfGroundSurface
owner: GroundSurface
domain_of:
- GroundSurface
range: ADEOfGroundSurface
required: false
multivalued: true

```
</details>