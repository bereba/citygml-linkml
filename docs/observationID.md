

# Slot: observationID 


_Specifies the unique identifier of the observation that is retrieved by the SensorConnection._





URI: [citygml:observationID](https://www.ogc.org/standards/citygml/observationID)
Alias: observationID

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
| self | citygml:observationID |
| native | citygml:observationID |




## LinkML Source

<details>
```yaml
name: observationID
description: Specifies the unique identifier of the observation that is retrieved
  by the SensorConnection.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: observationID
owner: SensorConnection
domain_of:
- SensorConnection
range: string
required: false
multivalued: false

```
</details>