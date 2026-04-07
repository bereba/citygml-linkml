

# Slot: sensorName 


_Specifies the name of the sensor from which the SensorConnection retrieves observations._





URI: [citygml:sensorName](https://www.ogc.org/standards/citygml/sensorName)
Alias: sensorName

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
| self | citygml:sensorName |
| native | citygml:sensorName |




## LinkML Source

<details>
```yaml
name: sensorName
description: Specifies the name of the sensor from which the SensorConnection retrieves
  observations.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: sensorName
owner: SensorConnection
domain_of:
- SensorConnection
range: string
required: false
multivalued: false

```
</details>