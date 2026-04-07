

# Slot: dateOfEvent 


_Specifies the date at which the event took or will take place._





URI: [citygml:dateOfEvent](https://www.ogc.org/standards/citygml/dateOfEvent)
Alias: dateOfEvent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConstructionEvent](ConstructionEvent.md) | A ConstructionEvent is a data type used to describe a specific event that is ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
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
| self | citygml:dateOfEvent |
| native | citygml:dateOfEvent |




## LinkML Source

<details>
```yaml
name: dateOfEvent
description: Specifies the date at which the event took or will take place.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: dateOfEvent
owner: ConstructionEvent
domain_of:
- ConstructionEvent
range: date
required: true
multivalued: false

```
</details>