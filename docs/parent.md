

# Slot: parent 


_Relates to a city object to which the CityObjectGroup belongs._





URI: [citygml:parent](https://www.ogc.org/standards/citygml/parent)
Alias: parent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CityObjectGroup](CityObjectGroup.md) | A CityObjectGroup represents an application-specific aggregation of city obje... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AbstractCityObject](AbstractCityObject.md) |
| Domain Of | [CityObjectGroup](CityObjectGroup.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | citygml:parent |
| native | citygml:parent |




## LinkML Source

<details>
```yaml
name: parent
description: Relates to a city object to which the CityObjectGroup belongs.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: parent
owner: CityObjectGroup
domain_of:
- CityObjectGroup
range: AbstractCityObject
required: false
multivalued: false

```
</details>