

# Slot: adeOfMassPointRelief 


_Augments the MassPointRelief with properties defined in an ADE._





URI: [citygml:adeOfMassPointRelief](https://www.ogc.org/standards/citygml/adeOfMassPointRelief)
Alias: adeOfMassPointRelief

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassPointRelief](MassPointRelief.md) | A MassPointRelief represents a terrain component as a collection of 3D points |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfMassPointRelief](ADEOfMassPointRelief.md) |
| Domain Of | [MassPointRelief](MassPointRelief.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MassPointRelief](MassPointRelief.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfMassPointRelief |
| native | citygml:adeOfMassPointRelief |




## LinkML Source

<details>
```yaml
name: adeOfMassPointRelief
description: Augments the MassPointRelief with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfMassPointRelief
owner: MassPointRelief
domain_of:
- MassPointRelief
range: ADEOfMassPointRelief
required: false
multivalued: true

```
</details>