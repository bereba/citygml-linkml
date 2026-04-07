

# Slot: adeOfHoleSurface 


_Augments the HoleSurface with properties defined in an ADE._





URI: [citygml:adeOfHoleSurface](https://www.ogc.org/standards/citygml/adeOfHoleSurface)
Alias: adeOfHoleSurface

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HoleSurface](HoleSurface.md) | A HoleSurface is a representation of the ground surface of a hole |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfHoleSurface](ADEOfHoleSurface.md) |
| Domain Of | [HoleSurface](HoleSurface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [HoleSurface](HoleSurface.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfHoleSurface |
| native | citygml:adeOfHoleSurface |




## LinkML Source

<details>
```yaml
name: adeOfHoleSurface
description: Augments the HoleSurface with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfHoleSurface
owner: HoleSurface
domain_of:
- HoleSurface
range: ADEOfHoleSurface
required: false
multivalued: true

```
</details>