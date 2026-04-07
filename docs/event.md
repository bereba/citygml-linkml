

# Slot: event 


_Indicates the specific event type._





URI: [citygml:event](https://www.ogc.org/standards/citygml/event)
Alias: event

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConstructionEvent](ConstructionEvent.md) | A ConstructionEvent is a data type used to describe a specific event that is ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EventValue](EventValue.md) |
| Domain Of | [ConstructionEvent](ConstructionEvent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ConstructionEvent](ConstructionEvent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:event |
| native | citygml:event |




## LinkML Source

<details>
```yaml
name: event
description: Indicates the specific event type.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: event
owner: ConstructionEvent
domain_of:
- ConstructionEvent
range: EventValue
required: true
multivalued: false

```
</details>