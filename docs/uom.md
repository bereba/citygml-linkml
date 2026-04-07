

# Slot: uom 



URI: [citygml:uom](https://www.ogc.org/standards/citygml/uom)
Alias: uom

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StandardFileTimeseries](StandardFileTimeseries.md) | A StandardFileTimeseries represents time-varying data for a single contiguous... |  no  |
| [MeasureOrNilReasonList](MeasureOrNilReasonList.md) | CityGML class from package Core |  no  |
| [AbstractAtomicTimeseries](AbstractAtomicTimeseries.md) | AbstractAtomicTimeseries represents the attributes and relationships that are... |  no  |
| [SensorConnection](SensorConnection.md) | A SensorConnection provides all details that are required to retrieve a speci... |  no  |
| [TabulatedFileTimeseries](TabulatedFileTimeseries.md) | A TabulatedFileTimeseries represents time-varying data of a specific data typ... |  no  |
| [GenericTimeseries](GenericTimeseries.md) | A GenericTimeseries represents time-varying data in the form of embedded time... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SensorConnection](SensorConnection.md), [AbstractAtomicTimeseries](AbstractAtomicTimeseries.md), [MeasureOrNilReasonList](MeasureOrNilReasonList.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:uom |
| native | citygml:uom |




## LinkML Source

<details>
```yaml
name: uom
alias: uom
domain_of:
- SensorConnection
- AbstractAtomicTimeseries
- MeasureOrNilReasonList
range: string

```
</details>