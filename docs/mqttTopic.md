

# Slot: mqttTopic 


_Names the specific datastream that is retrieved by the SensorConnection. This attribute is relevant when the MQTT Protocol is used to connect to a Sensor API._





URI: [citygml:mqttTopic](https://www.ogc.org/standards/citygml/mqttTopic)
Alias: mqttTopic

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
| self | citygml:mqttTopic |
| native | citygml:mqttTopic |




## LinkML Source

<details>
```yaml
name: mqttTopic
description: Names the specific datastream that is retrieved by the SensorConnection.
  This attribute is relevant when the MQTT Protocol is used to connect to a Sensor
  API.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: mqttTopic
owner: SensorConnection
domain_of:
- SensorConnection
range: string
required: false
multivalued: false

```
</details>