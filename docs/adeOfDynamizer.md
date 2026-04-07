

# Slot: adeOfDynamizer 


_Augments the Dynamizer with properties defined in an ADE._





URI: [citygml:adeOfDynamizer](https://www.ogc.org/standards/citygml/adeOfDynamizer)
Alias: adeOfDynamizer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dynamizer](Dynamizer.md) | A Dynamizer is an object that injects timeseries data for an individual attri... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfDynamizer](ADEOfDynamizer.md) |
| Domain Of | [Dynamizer](Dynamizer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dynamizer](Dynamizer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfDynamizer |
| native | citygml:adeOfDynamizer |




## LinkML Source

<details>
```yaml
name: adeOfDynamizer
description: Augments the Dynamizer with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfDynamizer
owner: Dynamizer
domain_of:
- Dynamizer
range: ADEOfDynamizer
required: false
multivalued: true

```
</details>