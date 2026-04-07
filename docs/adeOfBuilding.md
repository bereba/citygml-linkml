

# Slot: adeOfBuilding 


_Augments the Building with properties defined in an ADE._





URI: [citygml:adeOfBuilding](https://www.ogc.org/standards/citygml/adeOfBuilding)
Alias: adeOfBuilding

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Building](Building.md) | A Building is a free-standing, self-supporting construction that is roofed, u... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfBuilding](ADEOfBuilding.md) |
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
| self | citygml:adeOfBuilding |
| native | citygml:adeOfBuilding |




## LinkML Source

<details>
```yaml
name: adeOfBuilding
description: Augments the Building with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfBuilding
owner: Building
domain_of:
- Building
range: ADEOfBuilding
required: false
multivalued: true

```
</details>