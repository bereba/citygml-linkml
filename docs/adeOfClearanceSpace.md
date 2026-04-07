

# Slot: adeOfClearanceSpace 


_Augments the ClearanceSpace with properties defined in an ADE._





URI: [citygml:adeOfClearanceSpace](https://www.ogc.org/standards/citygml/adeOfClearanceSpace)
Alias: adeOfClearanceSpace

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClearanceSpace](ClearanceSpace.md) | A ClearanceSpace represents the actual free space above a TrafficArea within ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfClearanceSpace](ADEOfClearanceSpace.md) |
| Domain Of | [ClearanceSpace](ClearanceSpace.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ClearanceSpace](ClearanceSpace.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfClearanceSpace |
| native | citygml:adeOfClearanceSpace |




## LinkML Source

<details>
```yaml
name: adeOfClearanceSpace
description: Augments the ClearanceSpace with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfClearanceSpace
owner: ClearanceSpace
domain_of:
- ClearanceSpace
range: ADEOfClearanceSpace
required: false
multivalued: true

```
</details>