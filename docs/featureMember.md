

# Slot: featureMember 



URI: [citygml:featureMember](https://www.ogc.org/standards/citygml/featureMember)
Alias: featureMember

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CityModelMember](CityModelMember.md) | CityGML class from package Core |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AbstractFeature](AbstractFeature.md) |
| Domain Of | [CityModelMember](CityModelMember.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CityModelMember](CityModelMember.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:featureMember |
| native | citygml:featureMember |




## LinkML Source

<details>
```yaml
name: featureMember
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: featureMember
owner: CityModelMember
domain_of:
- CityModelMember
range: AbstractFeature
required: true
multivalued: false

```
</details>