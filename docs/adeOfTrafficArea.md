

# Slot: adeOfTrafficArea 


_Augments the TrafficArea with properties defined in an ADE._





URI: [citygml:adeOfTrafficArea](https://www.ogc.org/standards/citygml/adeOfTrafficArea)
Alias: adeOfTrafficArea

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrafficArea](TrafficArea.md) | A TrafficArea is the ground surface of a TrafficSpace |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfTrafficArea](ADEOfTrafficArea.md) |
| Domain Of | [TrafficArea](TrafficArea.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TrafficArea](TrafficArea.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfTrafficArea |
| native | citygml:adeOfTrafficArea |




## LinkML Source

<details>
```yaml
name: adeOfTrafficArea
description: Augments the TrafficArea with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfTrafficArea
owner: TrafficArea
domain_of:
- TrafficArea
range: ADEOfTrafficArea
required: false
multivalued: true

```
</details>