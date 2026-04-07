

# Slot: adeOfLandUse 


_Augments the LandUse with properties defined in an ADE._





URI: [citygml:adeOfLandUse](https://www.ogc.org/standards/citygml/adeOfLandUse)
Alias: adeOfLandUse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LandUse](LandUse.md) | A LandUse object is an area of the earth's surface dedicated to a specific la... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfLandUse](ADEOfLandUse.md) |
| Domain Of | [LandUse](LandUse.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [LandUse](LandUse.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfLandUse |
| native | citygml:adeOfLandUse |




## LinkML Source

<details>
```yaml
name: adeOfLandUse
description: Augments the LandUse with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfLandUse
owner: LandUse
domain_of:
- LandUse
range: ADEOfLandUse
required: false
multivalued: true

```
</details>