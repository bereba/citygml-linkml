

# Slot: adeOfCityModel 


_Augments the CityModel with properties defined in an ADE._





URI: [citygml:adeOfCityModel](https://www.ogc.org/standards/citygml/adeOfCityModel)
Alias: adeOfCityModel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CityModel](CityModel.md) | CityModel is the container for all objects belonging to a city model |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfCityModel](ADEOfCityModel.md) |
| Domain Of | [CityModel](CityModel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CityModel](CityModel.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfCityModel |
| native | citygml:adeOfCityModel |




## LinkML Source

<details>
```yaml
name: adeOfCityModel
description: Augments the CityModel with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfCityModel
owner: CityModel
domain_of:
- CityModel
range: ADEOfCityModel
required: false
multivalued: true

```
</details>