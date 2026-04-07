

# Slot: adeOfAbstractDynamizer 


_Augments AbstractDynamizer with properties defined in an ADE._





URI: [citygml:adeOfAbstractDynamizer](https://www.ogc.org/standards/citygml/adeOfAbstractDynamizer)
Alias: adeOfAbstractDynamizer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dynamizer](Dynamizer.md) | A Dynamizer is an object that injects timeseries data for an individual attri... |  no  |
| [AbstractDynamizer](AbstractDynamizer.md) | AbstractDynamizer is the abstract superclass to represent Dynamizer objects |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractDynamizer](ADEOfAbstractDynamizer.md) |
| Domain Of | [AbstractDynamizer](AbstractDynamizer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractDynamizer](AbstractDynamizer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractDynamizer |
| native | citygml:adeOfAbstractDynamizer |




## LinkML Source

<details>
```yaml
name: adeOfAbstractDynamizer
description: Augments AbstractDynamizer with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractDynamizer
owner: AbstractDynamizer
domain_of:
- AbstractDynamizer
range: ADEOfAbstractDynamizer
required: false
multivalued: true

```
</details>