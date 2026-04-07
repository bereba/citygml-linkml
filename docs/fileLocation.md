

# Slot: fileLocation 



URI: [citygml:fileLocation](https://www.ogc.org/standards/citygml/fileLocation)
Alias: fileLocation

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
| self | citygml:fileLocation |
| native | citygml:fileLocation |




## LinkML Source

<details>
```yaml
name: fileLocation
alias: fileLocation
domain_of:
- StandardFileTimeseries
- TabulatedFileTimeseries
range: string

```
</details>