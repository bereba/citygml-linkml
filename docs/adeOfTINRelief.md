

# Slot: adeOfTINRelief 


_Augments the TINRelief with properties defined in an ADE._





URI: [citygml:adeOfTINRelief](https://www.ogc.org/standards/citygml/adeOfTINRelief)
Alias: adeOfTINRelief

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TINRelief](TINRelief.md) | A TINRelief represents a terrain component as a triangulated irregular networ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfTINRelief](ADEOfTINRelief.md) |
| Domain Of | [TINRelief](TINRelief.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TINRelief](TINRelief.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfTINRelief |
| native | citygml:adeOfTINRelief |




## LinkML Source

<details>
```yaml
name: adeOfTINRelief
description: Augments the TINRelief with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfTINRelief
owner: TINRelief
domain_of:
- TINRelief
range: ADEOfTINRelief
required: false
multivalued: true

```
</details>