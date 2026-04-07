

# Slot: ring 


_Specifies the URIs that point to the LinearRings that are parameterized using the given texture coordinates._





URI: [citygml:ring](https://www.ogc.org/standards/citygml/ring)
Alias: ring

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TexCoordList](TexCoordList.md) | TexCoordList defines texture parameterization using texture coordinates |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [TexCoordList](TexCoordList.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TexCoordList](TexCoordList.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:ring |
| native | citygml:ring |




## LinkML Source

<details>
```yaml
name: ring
description: Specifies the URIs that point to the LinearRings that are parameterized
  using the given texture coordinates.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: ring
owner: TexCoordList
domain_of:
- TexCoordList
range: uri
required: true
multivalued: true

```
</details>