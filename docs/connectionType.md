

# Slot: connectionType 


_Indicates the type of Sensor API to which the SensorConnection refers._





URI: [citygml:connectionType](https://www.ogc.org/standards/citygml/connectionType)
Alias: connectionType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SensorConnection](SensorConnection.md) | A SensorConnection provides all details that are required to retrieve a speci... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SensorConnectionTypeValue](SensorConnectionTypeValue.md) |
| Domain Of | [SensorConnection](SensorConnection.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | citygml:connectionType |
| native | citygml:connectionType |




## LinkML Source

<details>
```yaml
name: connectionType
description: Indicates the type of Sensor API to which the SensorConnection refers.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: connectionType
owner: SensorConnection
domain_of:
- SensorConnection
range: SensorConnectionTypeValue
required: true
multivalued: false

```
</details>