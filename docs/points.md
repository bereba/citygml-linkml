

# Slot: points 


_Relates to the 3D MultiPoint geometry of the PointCloud stored inline with the city model._





URI: [citygml:points](https://www.ogc.org/standards/citygml/points)
Alias: points

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointCloud](PointCloud.md) | A PointCloud is an unordered collection of points that is a sampling of the g... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PointCloud](PointCloud.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | citygml:points |
| native | citygml:points |




## LinkML Source

<details>
```yaml
name: points
description: Relates to the 3D MultiPoint geometry of the PointCloud stored inline
  with the city model.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: points
owner: PointCloud
domain_of:
- PointCloud
range: string
required: false
multivalued: false

```
</details>