

# Slot: buildingPart 


_Relates the building parts to the Building._





URI: [citygml:buildingPart](https://www.ogc.org/standards/citygml/buildingPart)
Alias: buildingPart

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Building](Building.md) | A Building is a free-standing, self-supporting construction that is roofed, u... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BuildingPart](BuildingPart.md) |
| Domain Of | [Building](Building.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Building](Building.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:buildingPart |
| native | citygml:buildingPart |




## LinkML Source

<details>
```yaml
name: buildingPart
description: Relates the building parts to the Building.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: buildingPart
owner: Building
domain_of:
- Building
range: BuildingPart
required: false
multivalued: true

```
</details>