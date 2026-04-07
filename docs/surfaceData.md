

# Slot: surfaceData 


_Relates to the surface data that are part of the Appearance._





URI: [citygml:surfaceData](https://www.ogc.org/standards/citygml/surfaceData)
Alias: surfaceData

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Appearance](Appearance.md) | An Appearance is a collection of surface data, i |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AbstractSurfaceData](AbstractSurfaceData.md) |
| Domain Of | [Appearance](Appearance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Appearance](Appearance.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:surfaceData |
| native | citygml:surfaceData |




## LinkML Source

<details>
```yaml
name: surfaceData
description: Relates to the surface data that are part of the Appearance.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: surfaceData
owner: Appearance
domain_of:
- Appearance
range: AbstractSurfaceData
required: false
multivalued: true

```
</details>