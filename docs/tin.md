

# Slot: tin 


_Relates to the triangulated surface of the TINRelief._





URI: [citygml:tin](https://www.ogc.org/standards/citygml/tin)
Alias: tin

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TINRelief](TINRelief.md) | A TINRelief represents a terrain component as a triangulated irregular networ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [TINRelief](TINRelief.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | citygml:tin |
| native | citygml:tin |




## LinkML Source

<details>
```yaml
name: tin
description: Relates to the triangulated surface of the TINRelief.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: tin
owner: TINRelief
domain_of:
- TINRelief
range: string
required: true
multivalued: false

```
</details>