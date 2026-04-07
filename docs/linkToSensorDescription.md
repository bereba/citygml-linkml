

# Slot: linkToSensorDescription 


_Specifies the complete URL to the sensor description request._





URI: [citygml:linkToSensorDescription](https://www.ogc.org/standards/citygml/linkToSensorDescription)
Alias: linkToSensorDescription

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
| self | citygml:linkToSensorDescription |
| native | citygml:linkToSensorDescription |




## LinkML Source

<details>
```yaml
name: linkToSensorDescription
description: Specifies the complete URL to the sensor description request.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: linkToSensorDescription
owner: SensorConnection
domain_of:
- SensorConnection
range: string
required: false
multivalued: false

```
</details>