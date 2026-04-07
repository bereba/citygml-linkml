

# Slot: adeOfAuxiliaryTrafficArea 


_Augments the AuxiliaryTrafficArea with properties defined in an ADE._





URI: [citygml:adeOfAuxiliaryTrafficArea](https://www.ogc.org/standards/citygml/adeOfAuxiliaryTrafficArea)
Alias: adeOfAuxiliaryTrafficArea

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AuxiliaryTrafficArea](AuxiliaryTrafficArea.md) | An AuxiliaryTrafficArea is the ground surface of an AuxiliaryTrafficSpace |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAuxiliaryTrafficArea](ADEOfAuxiliaryTrafficArea.md) |
| Domain Of | [AuxiliaryTrafficArea](AuxiliaryTrafficArea.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AuxiliaryTrafficArea](AuxiliaryTrafficArea.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAuxiliaryTrafficArea |
| native | citygml:adeOfAuxiliaryTrafficArea |




## LinkML Source

<details>
```yaml
name: adeOfAuxiliaryTrafficArea
description: Augments the AuxiliaryTrafficArea with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAuxiliaryTrafficArea
owner: AuxiliaryTrafficArea
domain_of:
- AuxiliaryTrafficArea
range: ADEOfAuxiliaryTrafficArea
required: false
multivalued: true

```
</details>