

# Slot: ridgeOrValleyLines 


_Relates to the 3D MultiCurve geometry of the MassPointRelief. This association role is used to represent ridge or valley lines._





URI: [citygml:ridgeOrValleyLines](https://www.ogc.org/standards/citygml/ridgeOrValleyLines)
Alias: ridgeOrValleyLines

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BreaklineRelief](BreaklineRelief.md) | A BreaklineRelief represents a terrain component with 3D lines |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [BreaklineRelief](BreaklineRelief.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BreaklineRelief](BreaklineRelief.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:ridgeOrValleyLines |
| native | citygml:ridgeOrValleyLines |




## LinkML Source

<details>
```yaml
name: ridgeOrValleyLines
description: Relates to the 3D MultiCurve geometry of the MassPointRelief. This association
  role is used to represent ridge or valley lines.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: ridgeOrValleyLines
owner: BreaklineRelief
domain_of:
- BreaklineRelief
range: string
required: false
multivalued: false

```
</details>