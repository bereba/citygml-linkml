

# Slot: authType 


_Specifies the type of authentication required to be able to access the Sensor API._





URI: [citygml:authType](https://www.ogc.org/standards/citygml/authType)
Alias: authType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SensorConnection](SensorConnection.md) | A SensorConnection provides all details that are required to retrieve a speci... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AuthenticationTypeValue](AuthenticationTypeValue.md) |
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
| self | citygml:authType |
| native | citygml:authType |




## LinkML Source

<details>
```yaml
name: authType
description: Specifies the type of authentication required to be able to access the
  Sensor API.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: authType
owner: SensorConnection
domain_of:
- SensorConnection
range: AuthenticationTypeValue
required: false
multivalued: false

```
</details>