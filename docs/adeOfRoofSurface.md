

# Slot: adeOfRoofSurface 


_Augments the RoofSurface with properties defined in an ADE._





URI: [citygml:adeOfRoofSurface](https://www.ogc.org/standards/citygml/adeOfRoofSurface)
Alias: adeOfRoofSurface

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RoofSurface](RoofSurface.md) | A RoofSurface is a surface that delimits major roof parts of a construction |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfRoofSurface](ADEOfRoofSurface.md) |
| Domain Of | [RoofSurface](RoofSurface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [RoofSurface](RoofSurface.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfRoofSurface |
| native | citygml:adeOfRoofSurface |




## LinkML Source

<details>
```yaml
name: adeOfRoofSurface
description: Augments the RoofSurface with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfRoofSurface
owner: RoofSurface
domain_of:
- RoofSurface
range: ADEOfRoofSurface
required: false
multivalued: true

```
</details>