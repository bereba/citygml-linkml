

# Slot: elevationReference 


_Specifies the level from which the elevation was measured. [cf. INSPIRE]_





URI: [citygml:elevationReference](https://www.ogc.org/standards/citygml/elevationReference)
Alias: elevationReference

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevation](Elevation.md) | Elevation is a data type that includes the elevation value itself and informa... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ElevationReferenceValue](ElevationReferenceValue.md) |
| Domain Of | [Elevation](Elevation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Elevation](Elevation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:elevationReference |
| native | citygml:elevationReference |




## LinkML Source

<details>
```yaml
name: elevationReference
description: Specifies the level from which the elevation was measured. [cf. INSPIRE]
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: elevationReference
owner: Elevation
domain_of:
- Elevation
range: ElevationReferenceValue
required: true
multivalued: false

```
</details>