

# Slot: clearanceSpace 


_Relates to the clearance spaces that are part of the TrafficSpace._





URI: [citygml:clearanceSpace](https://www.ogc.org/standards/citygml/clearanceSpace)
Alias: clearanceSpace

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrafficSpace](TrafficSpace.md) | A TrafficSpace is a space in which traffic takes place |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ClearanceSpace](ClearanceSpace.md) |
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
| self | citygml:clearanceSpace |
| native | citygml:clearanceSpace |




## LinkML Source

<details>
```yaml
name: clearanceSpace
description: Relates to the clearance spaces that are part of the TrafficSpace.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: clearanceSpace
owner: TrafficSpace
domain_of:
- TrafficSpace
range: ClearanceSpace
required: false
multivalued: true

```
</details>