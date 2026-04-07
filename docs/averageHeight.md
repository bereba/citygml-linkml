

# Slot: averageHeight 


_Specifies the average height of the PlantCover._





URI: [citygml:averageHeight](https://www.ogc.org/standards/citygml/averageHeight)
Alias: averageHeight

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantCover](PlantCover.md) | A PlantCover represents a space covered by vegetation |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [PlantCover](PlantCover.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PlantCover](PlantCover.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:averageHeight |
| native | citygml:averageHeight |




## LinkML Source

<details>
```yaml
name: averageHeight
description: Specifies the average height of the PlantCover.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: averageHeight
owner: PlantCover
domain_of:
- PlantCover
range: float
required: false
multivalued: false

```
</details>