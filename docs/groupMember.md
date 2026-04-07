

# Slot: groupMember 



URI: [citygml:groupMember](https://www.ogc.org/standards/citygml/groupMember)
Alias: groupMember

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
| self | citygml:groupMember |
| native | citygml:groupMember |




## LinkML Source

<details>
```yaml
name: groupMember
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: groupMember
owner: CityObjectGroup
domain_of:
- CityObjectGroup
range: AbstractCityObject
required: false
multivalued: true

```
</details>