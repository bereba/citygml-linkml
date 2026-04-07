

# Slot: storey 


_Relates to the storeys on which the BuildingUnit is located._





URI: [citygml:storey](https://www.ogc.org/standards/citygml/storey)
Alias: storey

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BuildingUnit](BuildingUnit.md) | A BuildingUnit is a logical subdivision of a Building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Storey](Storey.md) |
| Domain Of | [BuildingUnit](BuildingUnit.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BuildingUnit](BuildingUnit.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:storey |
| native | citygml:storey |




## LinkML Source

<details>
```yaml
name: storey
description: Relates to the storeys on which the BuildingUnit is located.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: storey
owner: BuildingUnit
domain_of:
- BuildingUnit
range: Storey
required: false
multivalued: true

```
</details>