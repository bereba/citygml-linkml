

# Slot: linkToObservation 


_Specifies the complete URL to the observation request._





URI: [citygml:linkToObservation](https://www.ogc.org/standards/citygml/linkToObservation)
Alias: linkToObservation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SensorConnection](SensorConnection.md) | A SensorConnection provides all details that are required to retrieve a speci... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SensorConnection](SensorConnection.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SensorConnection](SensorConnection.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:linkToObservation |
| native | citygml:linkToObservation |




## LinkML Source

<details>
```yaml
name: linkToObservation
description: Specifies the complete URL to the observation request.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: linkToObservation
owner: SensorConnection
domain_of:
- SensorConnection
range: string
required: false
multivalued: false

```
</details>