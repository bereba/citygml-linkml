

# Slot: fileType 



URI: [citygml:fileType](https://www.ogc.org/standards/citygml/fileType)
Alias: fileType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StandardFileTimeseries](StandardFileTimeseries.md) | A StandardFileTimeseries represents time-varying data for a single contiguous... |  no  |
| [TabulatedFileTimeseries](TabulatedFileTimeseries.md) | A TabulatedFileTimeseries represents time-varying data of a specific data typ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [StandardFileTimeseries](StandardFileTimeseries.md), [TabulatedFileTimeseries](TabulatedFileTimeseries.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:fileType |
| native | citygml:fileType |




## LinkML Source

<details>
```yaml
name: fileType
alias: fileType
domain_of:
- StandardFileTimeseries
- TabulatedFileTimeseries
range: string

```
</details>