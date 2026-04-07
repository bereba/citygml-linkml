

# Slot: minHeight 


_Specifies the minimum height of the PlantCover._





URI: [citygml:minHeight](https://www.ogc.org/standards/citygml/minHeight)
Alias: minHeight

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
| self | citygml:minHeight |
| native | citygml:minHeight |




## LinkML Source

<details>
```yaml
name: minHeight
description: Specifies the minimum height of the PlantCover.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: minHeight
owner: PlantCover
domain_of:
- PlantCover
range: float
required: false
multivalued: false

```
</details>