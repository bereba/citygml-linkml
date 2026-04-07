

# Slot: successor 


_Indicates the successor(s) of the TrafficSpace._





URI: [citygml:successor](https://www.ogc.org/standards/citygml/successor)
Alias: successor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrafficSpace](TrafficSpace.md) | A TrafficSpace is a space in which traffic takes place |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TrafficSpace](TrafficSpace.md) |
| Domain Of | [TrafficSpace](TrafficSpace.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TrafficSpace](TrafficSpace.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:successor |
| native | citygml:successor |




## LinkML Source

<details>
```yaml
name: successor
description: Indicates the successor(s) of the TrafficSpace.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: successor
owner: TrafficSpace
domain_of:
- TrafficSpace
range: TrafficSpace
required: false
multivalued: true

```
</details>