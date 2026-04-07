

# Slot: adeOfAbstractPointCloud 


_Augments AbstractPointCloud with properties defined in an ADE._





URI: [citygml:adeOfAbstractPointCloud](https://www.ogc.org/standards/citygml/adeOfAbstractPointCloud)
Alias: adeOfAbstractPointCloud

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AbstractPointCloud](AbstractPointCloud.md) | AbstractPointCloud is the abstract superclass to represent PointCloud objects |  no  |
| [PointCloud](PointCloud.md) | A PointCloud is an unordered collection of points that is a sampling of the g... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractPointCloud](ADEOfAbstractPointCloud.md) |
| Domain Of | [AbstractPointCloud](AbstractPointCloud.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractPointCloud](AbstractPointCloud.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractPointCloud |
| native | citygml:adeOfAbstractPointCloud |




## LinkML Source

<details>
```yaml
name: adeOfAbstractPointCloud
description: Augments AbstractPointCloud with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractPointCloud
owner: AbstractPointCloud
domain_of:
- AbstractPointCloud
range: ADEOfAbstractPointCloud
required: false
multivalued: true

```
</details>