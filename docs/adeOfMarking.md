

# Slot: adeOfMarking 


_Augments the Marking with properties defined in an ADE._





URI: [citygml:adeOfMarking](https://www.ogc.org/standards/citygml/adeOfMarking)
Alias: adeOfMarking

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Marking](Marking.md) | A Marking is a visible pattern on a transportation area relevant to the struc... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfMarking](ADEOfMarking.md) |
| Domain Of | [Marking](Marking.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Marking](Marking.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfMarking |
| native | citygml:adeOfMarking |




## LinkML Source

<details>
```yaml
name: adeOfMarking
description: Augments the Marking with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfMarking
owner: Marking
domain_of:
- Marking
range: ADEOfMarking
required: false
multivalued: true

```
</details>