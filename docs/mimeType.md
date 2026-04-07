

# Slot: mimeType 



URI: [citygml:mimeType](https://www.ogc.org/standards/citygml/mimeType)
Alias: mimeType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StandardFileTimeseries](StandardFileTimeseries.md) | A StandardFileTimeseries represents time-varying data for a single contiguous... |  no  |
| [ImplicitGeometry](ImplicitGeometry.md) | ImplicitGeometry is a geometry representation where the shape is stored only ... |  no  |
| [PointCloud](PointCloud.md) | A PointCloud is an unordered collection of points that is a sampling of the g... |  no  |
| [AbstractTexture](AbstractTexture.md) | AbstractTexture is the abstract superclass to represent the common attributes... |  no  |
| [ParameterizedTexture](ParameterizedTexture.md) | A ParameterizedTexture is a texture that uses texture coordinates or a transf... |  no  |
| [TabulatedFileTimeseries](TabulatedFileTimeseries.md) | A TabulatedFileTimeseries represents time-varying data of a specific data typ... |  no  |
| [GeoreferencedTexture](GeoreferencedTexture.md) | A GeoreferencedTexture is a texture that uses a planimetric projection |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [StandardFileTimeseries](StandardFileTimeseries.md), [TabulatedFileTimeseries](TabulatedFileTimeseries.md), [PointCloud](PointCloud.md), [AbstractTexture](AbstractTexture.md), [ImplicitGeometry](ImplicitGeometry.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:mimeType |
| native | citygml:mimeType |




## LinkML Source

<details>
```yaml
name: mimeType
alias: mimeType
domain_of:
- StandardFileTimeseries
- TabulatedFileTimeseries
- PointCloud
- AbstractTexture
- ImplicitGeometry
range: string

```
</details>