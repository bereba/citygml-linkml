

# Slot: baseURL 


_Specifies the base URL of the Sensor API request._





URI: [citygml:baseURL](https://www.ogc.org/standards/citygml/baseURL)
Alias: baseURL

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SensorConnection](SensorConnection.md) | A SensorConnection provides all details that are required to retrieve a speci... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
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
| self | citygml:baseURL |
| native | citygml:baseURL |




## LinkML Source

<details>
```yaml
name: baseURL
description: Specifies the base URL of the Sensor API request.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: baseURL
owner: SensorConnection
domain_of:
- SensorConnection
range: uri
required: false
multivalued: false

```
</details>