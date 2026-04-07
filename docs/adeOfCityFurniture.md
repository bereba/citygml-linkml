

# Slot: adeOfCityFurniture 


_Augments the CityFurniture with properties defined in an ADE._





URI: [citygml:adeOfCityFurniture](https://www.ogc.org/standards/citygml/adeOfCityFurniture)
Alias: adeOfCityFurniture

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CityFurniture](CityFurniture.md) | CityFurniture is an object or piece of equipment installed in the outdoor env... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfCityFurniture](ADEOfCityFurniture.md) |
| Domain Of | [CityFurniture](CityFurniture.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CityFurniture](CityFurniture.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfCityFurniture |
| native | citygml:adeOfCityFurniture |




## LinkML Source

<details>
```yaml
name: adeOfCityFurniture
description: Augments the CityFurniture with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfCityFurniture
owner: CityFurniture
domain_of:
- CityFurniture
range: ADEOfCityFurniture
required: false
multivalued: true

```
</details>