

# Slot: adeOfAbstractVegetationObject 


_Augments AbstractVegetationObject with properties defined in an ADE._





URI: [citygml:adeOfAbstractVegetationObject](https://www.ogc.org/standards/citygml/adeOfAbstractVegetationObject)
Alias: adeOfAbstractVegetationObject

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AbstractVegetationObject](AbstractVegetationObject.md) | AbstractVegetationObject is the abstract superclass for all kinds of vegetati... |  no  |
| [PlantCover](PlantCover.md) | A PlantCover represents a space covered by vegetation |  no  |
| [SolitaryVegetationObject](SolitaryVegetationObject.md) | A SolitaryVegetationObject represents individual vegetation objects, e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractVegetationObject](ADEOfAbstractVegetationObject.md) |
| Domain Of | [AbstractVegetationObject](AbstractVegetationObject.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractVegetationObject](AbstractVegetationObject.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractVegetationObject |
| native | citygml:adeOfAbstractVegetationObject |




## LinkML Source

<details>
```yaml
name: adeOfAbstractVegetationObject
description: Augments AbstractVegetationObject with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractVegetationObject
owner: AbstractVegetationObject
domain_of:
- AbstractVegetationObject
range: ADEOfAbstractVegetationObject
required: false
multivalued: true

```
</details>