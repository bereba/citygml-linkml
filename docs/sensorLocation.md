

# Slot: sensorLocation 


_Relates the sensor to the city object where it is located._





URI: [citygml:sensorLocation](https://www.ogc.org/standards/citygml/sensorLocation)
Alias: sensorLocation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SensorConnection](SensorConnection.md) | A SensorConnection provides all details that are required to retrieve a speci... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AbstractCityObject](AbstractCityObject.md) |
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
| self | citygml:sensorLocation |
| native | citygml:sensorLocation |




## LinkML Source

<details>
```yaml
name: sensorLocation
description: Relates the sensor to the city object where it is located.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: sensorLocation
owner: SensorConnection
domain_of:
- SensorConnection
range: AbstractCityObject
required: false
multivalued: false

```
</details>