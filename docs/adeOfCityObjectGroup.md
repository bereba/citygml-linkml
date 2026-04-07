

# Slot: adeOfCityObjectGroup 


_Augments the CityObjectGroup with properties defined in an ADE._





URI: [citygml:adeOfCityObjectGroup](https://www.ogc.org/standards/citygml/adeOfCityObjectGroup)
Alias: adeOfCityObjectGroup

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CityObjectGroup](CityObjectGroup.md) | A CityObjectGroup represents an application-specific aggregation of city obje... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfCityObjectGroup](ADEOfCityObjectGroup.md) |
| Domain Of | [CityObjectGroup](CityObjectGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CityObjectGroup](CityObjectGroup.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfCityObjectGroup |
| native | citygml:adeOfCityObjectGroup |




## LinkML Source

<details>
```yaml
name: adeOfCityObjectGroup
description: Augments the CityObjectGroup with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfCityObjectGroup
owner: CityObjectGroup
domain_of:
- CityObjectGroup
range: ADEOfCityObjectGroup
required: false
multivalued: true

```
</details>