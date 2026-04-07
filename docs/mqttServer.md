

# Slot: mqttServer 


_Specifies the name of the MQTT Server. This attribute is relevant when the MQTT Protocol is used to connect to a Sensor API._





URI: [citygml:mqttServer](https://www.ogc.org/standards/citygml/mqttServer)
Alias: mqttServer

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
| self | citygml:mqttServer |
| native | citygml:mqttServer |




## LinkML Source

<details>
```yaml
name: mqttServer
description: Specifies the name of the MQTT Server. This attribute is relevant when
  the MQTT Protocol is used to connect to a Sensor API.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: mqttServer
owner: SensorConnection
domain_of:
- SensorConnection
range: string
required: false
multivalued: false

```
</details>