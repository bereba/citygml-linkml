

# Slot: adeOfBuildingInstallation 


_Augments the BuildingInstallation with properties defined in an ADE._





URI: [citygml:adeOfBuildingInstallation](https://www.ogc.org/standards/citygml/adeOfBuildingInstallation)
Alias: adeOfBuildingInstallation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BuildingInstallation](BuildingInstallation.md) | A BuildingInstallation is a permanent part of a Building (inside and/or outsi... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfBuildingInstallation](ADEOfBuildingInstallation.md) |
| Domain Of | [BuildingInstallation](BuildingInstallation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BuildingInstallation](BuildingInstallation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfBuildingInstallation |
| native | citygml:adeOfBuildingInstallation |




## LinkML Source

<details>
```yaml
name: adeOfBuildingInstallation
description: Augments the BuildingInstallation with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfBuildingInstallation
owner: BuildingInstallation
domain_of:
- BuildingInstallation
range: ADEOfBuildingInstallation
required: false
multivalued: true

```
</details>