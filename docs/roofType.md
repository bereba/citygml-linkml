

# Slot: roofType 


_Indicates the shape of the roof of the Building or BuildingPart._





URI: [citygml:roofType](https://www.ogc.org/standards/citygml/roofType)
Alias: roofType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Building](Building.md) | A Building is a free-standing, self-supporting construction that is roofed, u... |  no  |
| [AbstractBuilding](AbstractBuilding.md) | AbstractBuilding is an abstract superclass representing the common attributes... |  no  |
| [BuildingPart](BuildingPart.md) | A BuildingPart is a physical or functional subdivision of a Building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RoofTypeValue](RoofTypeValue.md) |
| Domain Of | [AbstractBuilding](AbstractBuilding.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractBuilding](AbstractBuilding.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:roofType |
| native | citygml:roofType |




## LinkML Source

<details>
```yaml
name: roofType
description: Indicates the shape of the roof of the Building or BuildingPart.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: roofType
owner: AbstractBuilding
domain_of:
- AbstractBuilding
range: RoofTypeValue
required: false
multivalued: false

```
</details>