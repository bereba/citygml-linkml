

# Slot: endTime 


_Specifies the end of the time span for which the Dynamizer provides dynamic values._





URI: [citygml:endTime](https://www.ogc.org/standards/citygml/endTime)
Alias: endTime

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dynamizer](Dynamizer.md) | A Dynamizer is an object that injects timeseries data for an individual attri... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Dynamizer](Dynamizer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | citygml:endTime |
| native | citygml:endTime |




## LinkML Source

<details>
```yaml
name: endTime
description: Specifies the end of the time span for which the Dynamizer provides dynamic
  values.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: endTime
owner: Dynamizer
domain_of:
- Dynamizer
range: string
required: false
multivalued: false

```
</details>