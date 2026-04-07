

# Slot: sensorConnection 


_Relates to the sensor API that delivers timeseries data._





URI: [citygml:sensorConnection](https://www.ogc.org/standards/citygml/sensorConnection)
Alias: sensorConnection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dynamizer](Dynamizer.md) | A Dynamizer is an object that injects timeseries data for an individual attri... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SensorConnection](SensorConnection.md) |
| Domain Of | [Dynamizer](Dynamizer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dynamizer](Dynamizer.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:sensorConnection |
| native | citygml:sensorConnection |




## LinkML Source

<details>
```yaml
name: sensorConnection
description: Relates to the sensor API that delivers timeseries data.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: sensorConnection
owner: Dynamizer
domain_of:
- Dynamizer
range: SensorConnection
required: false
multivalued: false

```
</details>