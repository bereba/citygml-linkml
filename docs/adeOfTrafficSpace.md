

# Slot: adeOfTrafficSpace 


_Augments the TrafficSpace with properties defined in an ADE._





URI: [citygml:adeOfTrafficSpace](https://www.ogc.org/standards/citygml/adeOfTrafficSpace)
Alias: adeOfTrafficSpace

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrafficSpace](TrafficSpace.md) | A TrafficSpace is a space in which traffic takes place |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfTrafficSpace](ADEOfTrafficSpace.md) |
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
| self | citygml:adeOfTrafficSpace |
| native | citygml:adeOfTrafficSpace |




## LinkML Source

<details>
```yaml
name: adeOfTrafficSpace
description: Augments the TrafficSpace with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfTrafficSpace
owner: TrafficSpace
domain_of:
- TrafficSpace
range: ADEOfTrafficSpace
required: false
multivalued: true

```
</details>