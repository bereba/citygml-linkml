

# Slot: timestamp 


_Specifies the timepoint at which the value of the TimeValuePair is valid._





URI: [citygml:timestamp](https://www.ogc.org/standards/citygml/timestamp)
Alias: timestamp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeValuePair](TimeValuePair.md) | A TimeValuePair represents a value that is valid for a given timepoint |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [TimeValuePair](TimeValuePair.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TimeValuePair](TimeValuePair.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:timestamp |
| native | citygml:timestamp |




## LinkML Source

<details>
```yaml
name: timestamp
description: Specifies the timepoint at which the value of the TimeValuePair is valid.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: timestamp
owner: TimeValuePair
domain_of:
- TimeValuePair
range: string
required: true
multivalued: false

```
</details>