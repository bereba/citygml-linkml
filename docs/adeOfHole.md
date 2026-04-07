

# Slot: adeOfHole 


_Augments the Hole with properties defined in an ADE._





URI: [citygml:adeOfHole](https://www.ogc.org/standards/citygml/adeOfHole)
Alias: adeOfHole

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Hole](Hole.md) | A Hole is an opening in the surface of a Road, Track or Square such as road d... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfHole](ADEOfHole.md) |
| Domain Of | [Hole](Hole.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Hole](Hole.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfHole |
| native | citygml:adeOfHole |




## LinkML Source

<details>
```yaml
name: adeOfHole
description: Augments the Hole with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfHole
owner: Hole
domain_of:
- Hole
range: ADEOfHole
required: false
multivalued: true

```
</details>