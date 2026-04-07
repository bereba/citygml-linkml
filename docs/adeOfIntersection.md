

# Slot: adeOfIntersection 


_Augments the Intersection with properties defined in an ADE._





URI: [citygml:adeOfIntersection](https://www.ogc.org/standards/citygml/adeOfIntersection)
Alias: adeOfIntersection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Intersection](Intersection.md) | An Intersection is a transportation space that is a shared segment of multipl... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfIntersection](ADEOfIntersection.md) |
| Domain Of | [Intersection](Intersection.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Intersection](Intersection.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfIntersection |
| native | citygml:adeOfIntersection |




## LinkML Source

<details>
```yaml
name: adeOfIntersection
description: Augments the Intersection with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfIntersection
owner: Intersection
domain_of:
- Intersection
range: ADEOfIntersection
required: false
multivalued: true

```
</details>