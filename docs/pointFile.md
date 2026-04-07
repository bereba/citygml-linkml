

# Slot: pointFile 


_Specifies the URI that points to the external point cloud file._





URI: [citygml:pointFile](https://www.ogc.org/standards/citygml/pointFile)
Alias: pointFile

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PointCloud](PointCloud.md) | A PointCloud is an unordered collection of points that is a sampling of the g... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
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
| self | citygml:pointFile |
| native | citygml:pointFile |




## LinkML Source

<details>
```yaml
name: pointFile
description: Specifies the URI that points to the external point cloud file.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: pointFile
owner: PointCloud
domain_of:
- PointCloud
range: uri
required: false
multivalued: false

```
</details>