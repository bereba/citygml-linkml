

# Slot: sensorID 


_Specifies the unique identifier of the sensor from which the SensorConnection retrieves observations._





URI: [citygml:sensorID](https://www.ogc.org/standards/citygml/sensorID)
Alias: sensorID

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
| self | citygml:sensorID |
| native | citygml:sensorID |




## LinkML Source

<details>
```yaml
name: sensorID
description: Specifies the unique identifier of the sensor from which the SensorConnection
  retrieves observations.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: sensorID
owner: SensorConnection
domain_of:
- SensorConnection
range: string
required: false
multivalued: false

```
</details>