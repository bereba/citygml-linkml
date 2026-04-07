

# Slot: uriValue 


_Specifies the "URI" value of the TimeValuePair._





URI: [citygml:uriValue](https://www.ogc.org/standards/citygml/uriValue)
Alias: uriValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeValuePair](TimeValuePair.md) | A TimeValuePair represents a value that is valid for a given timepoint |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [TimeValuePair](TimeValuePair.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | citygml:uriValue |
| native | citygml:uriValue |




## LinkML Source

<details>
```yaml
name: uriValue
description: Specifies the "URI" value of the TimeValuePair.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: uriValue
owner: TimeValuePair
domain_of:
- TimeValuePair
range: uri
required: false
multivalued: false

```
</details>