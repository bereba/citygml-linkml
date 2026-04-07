

# Slot: pointFileSrsName 


_Indicates the coordinate reference system used by the external point cloud file._





URI: [citygml:pointFileSrsName](https://www.ogc.org/standards/citygml/pointFileSrsName)
Alias: pointFileSrsName

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
| self | citygml:pointFileSrsName |
| native | citygml:pointFileSrsName |




## LinkML Source

<details>
```yaml
name: pointFileSrsName
description: Indicates the coordinate reference system used by the external point
  cloud file.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: pointFileSrsName
owner: PointCloud
domain_of:
- PointCloud
range: string
required: false
multivalued: false

```
</details>