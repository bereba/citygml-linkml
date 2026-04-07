

# Slot: adeOfRailway 


_Augments the Railway with properties defined in an ADE._





URI: [citygml:adeOfRailway](https://www.ogc.org/standards/citygml/adeOfRailway)
Alias: adeOfRailway

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Railway](Railway.md) | A Railway is a transportation space used by wheeled vehicles on rails |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfRailway](ADEOfRailway.md) |
| Domain Of | [Railway](Railway.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Railway](Railway.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfRailway |
| native | citygml:adeOfRailway |




## LinkML Source

<details>
```yaml
name: adeOfRailway
description: Augments the Railway with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfRailway
owner: Railway
domain_of:
- Railway
range: ADEOfRailway
required: false
multivalued: true

```
</details>