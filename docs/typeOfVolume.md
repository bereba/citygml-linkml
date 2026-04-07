

# Slot: typeOfVolume 


_Indicates the specific type of the QualifiedVolume._





URI: [citygml:typeOfVolume](https://www.ogc.org/standards/citygml/typeOfVolume)
Alias: typeOfVolume

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QualifiedVolume](QualifiedVolume.md) | QualifiedVolume is an application-dependent measure of the volume of a space |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [QualifiedVolumeTypeValue](QualifiedVolumeTypeValue.md) |
| Domain Of | [QualifiedVolume](QualifiedVolume.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [QualifiedVolume](QualifiedVolume.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:typeOfVolume |
| native | citygml:typeOfVolume |




## LinkML Source

<details>
```yaml
name: typeOfVolume
description: Indicates the specific type of the QualifiedVolume.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: typeOfVolume
owner: QualifiedVolume
domain_of:
- QualifiedVolume
range: QualifiedVolumeTypeValue
required: true
multivalued: false

```
</details>