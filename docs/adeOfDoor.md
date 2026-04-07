

# Slot: adeOfDoor 


_Augments the Door with properties defined in an ADE._





URI: [citygml:adeOfDoor](https://www.ogc.org/standards/citygml/adeOfDoor)
Alias: adeOfDoor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Door](Door.md) | A Door is a construction for closing an opening intended primarily for access... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfDoor](ADEOfDoor.md) |
| Domain Of | [Door](Door.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Door](Door.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfDoor |
| native | citygml:adeOfDoor |




## LinkML Source

<details>
```yaml
name: adeOfDoor
description: Augments the Door with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfDoor
owner: Door
domain_of:
- Door
range: ADEOfDoor
required: false
multivalued: true

```
</details>