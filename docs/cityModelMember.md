

# Slot: cityModelMember 



URI: [citygml:cityModelMember](https://www.ogc.org/standards/citygml/cityModelMember)
Alias: cityModelMember

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CityModel](CityModel.md) | CityModel is the container for all objects belonging to a city model |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CityModelMember](CityModelMember.md) |
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
| self | citygml:cityModelMember |
| native | citygml:cityModelMember |




## LinkML Source

<details>
```yaml
name: cityModelMember
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: cityModelMember
owner: CityModel
domain_of:
- CityModel
range: CityModelMember
required: false
multivalued: true

```
</details>