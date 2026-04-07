

# Slot: elevationValue 


_Specifies the value of the elevation. [cf. INSPIRE]_





URI: [citygml:elevationValue](https://www.ogc.org/standards/citygml/elevationValue)
Alias: elevationValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Elevation](Elevation.md) | Elevation is a data type that includes the elevation value itself and informa... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | citygml:elevationValue |
| native | citygml:elevationValue |




## LinkML Source

<details>
```yaml
name: elevationValue
description: Specifies the value of the elevation. [cf. INSPIRE]
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: elevationValue
owner: Elevation
domain_of:
- Elevation
range: string
required: true
multivalued: false

```
</details>