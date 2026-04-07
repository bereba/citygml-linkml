

# Slot: species 


_Indicates the botanical name of the SolitaryVegetationObject._





URI: [citygml:species](https://www.ogc.org/standards/citygml/species)
Alias: species

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SolitaryVegetationObject](SolitaryVegetationObject.md) | A SolitaryVegetationObject represents individual vegetation objects, e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SpeciesValue](SpeciesValue.md) |
| Domain Of | [SolitaryVegetationObject](SolitaryVegetationObject.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SolitaryVegetationObject](SolitaryVegetationObject.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:species |
| native | citygml:species |




## LinkML Source

<details>
```yaml
name: species
description: Indicates the botanical name of the SolitaryVegetationObject.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: species
owner: SolitaryVegetationObject
domain_of:
- SolitaryVegetationObject
range: SpeciesValue
required: false
multivalued: false

```
</details>