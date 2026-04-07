

# Slot: adeOfPointCloud 


_Augments the PointCloud with properties defined in an ADE._





URI: [citygml:adeOfPointCloud](https://www.ogc.org/standards/citygml/adeOfPointCloud)
Alias: adeOfPointCloud

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointCloud](PointCloud.md) | A PointCloud is an unordered collection of points that is a sampling of the g... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfPointCloud](ADEOfPointCloud.md) |
| Domain Of | [PointCloud](PointCloud.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PointCloud](PointCloud.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfPointCloud |
| native | citygml:adeOfPointCloud |




## LinkML Source

<details>
```yaml
name: adeOfPointCloud
description: Augments the PointCloud with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfPointCloud
owner: PointCloud
domain_of:
- PointCloud
range: ADEOfPointCloud
required: false
multivalued: true

```
</details>