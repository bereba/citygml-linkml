

# Slot: adeOfDoorSurface 


_Augments the DoorSurface with properties defined in an ADE._





URI: [citygml:adeOfDoorSurface](https://www.ogc.org/standards/citygml/adeOfDoorSurface)
Alias: adeOfDoorSurface

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DoorSurface](DoorSurface.md) | A DoorSurface is either a boundary surface of a Door feature or a surface tha... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfDoorSurface](ADEOfDoorSurface.md) |
| Domain Of | [DoorSurface](DoorSurface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DoorSurface](DoorSurface.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfDoorSurface |
| native | citygml:adeOfDoorSurface |




## LinkML Source

<details>
```yaml
name: adeOfDoorSurface
description: Augments the DoorSurface with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfDoorSurface
owner: DoorSurface
domain_of:
- DoorSurface
range: ADEOfDoorSurface
required: false
multivalued: true

```
</details>