

# Slot: adeOfStorey 


_Augments the Storey with properties defined in an ADE._





URI: [citygml:adeOfStorey](https://www.ogc.org/standards/citygml/adeOfStorey)
Alias: adeOfStorey

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Storey](Storey.md) | A Storey is typically a horizontal section of a Building |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfStorey](ADEOfStorey.md) |
| Domain Of | [Storey](Storey.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Storey](Storey.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfStorey |
| native | citygml:adeOfStorey |




## LinkML Source

<details>
```yaml
name: adeOfStorey
description: Augments the Storey with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfStorey
owner: Storey
domain_of:
- Storey
range: ADEOfStorey
required: false
multivalued: true

```
</details>