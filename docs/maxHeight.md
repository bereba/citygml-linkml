

# Slot: maxHeight 


_Specifies the maximum height of the PlantCover._





URI: [citygml:maxHeight](https://www.ogc.org/standards/citygml/maxHeight)
Alias: maxHeight

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
| self | citygml:maxHeight |
| native | citygml:maxHeight |




## LinkML Source

<details>
```yaml
name: maxHeight
description: Specifies the maximum height of the PlantCover.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: maxHeight
owner: PlantCover
domain_of:
- PlantCover
range: float
required: false
multivalued: false

```
</details>