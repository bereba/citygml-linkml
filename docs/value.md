

# Slot: value 



URI: [citygml:value](https://www.ogc.org/standards/citygml/value)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [UriAttribute](UriAttribute.md) | UriAttribute is a data type used to define generic attributes of type "URI" |  no  |
| [Height](Height.md) | Height represents a vertical distance (measured or estimated) between a low r... |  no  |
| [DoubleOrNilReason](DoubleOrNilReason.md) | CityGML class from package Core |  no  |
| [DateAttribute](DateAttribute.md) | DateAttribute is a data type used to define generic attributes of type "Date" |  no  |
| [DoubleAttribute](DoubleAttribute.md) | DoubleAttribute is a data type used to define generic attributes of type "Dou... |  no  |
| [StringAttribute](StringAttribute.md) | StringAttribute is a data type used to define generic attributes of type "Str... |  no  |
| [IntAttribute](IntAttribute.md) | IntAttribute is a data type used to define generic attributes of type "Intege... |  no  |
| [CodeAttribute](CodeAttribute.md) | CodeAttribute is a data type used to define generic attributes of type "Code" |  no  |
| [MeasureAttribute](MeasureAttribute.md) | MeasureAttribute is a data type used to define generic attributes of type "Me... |  no  |
| [RoomHeight](RoomHeight.md) | The RoomHeight represents a vertical distance (measured or estimated) between... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Height](Height.md), [RoomHeight](RoomHeight.md), [DoubleOrNilReason](DoubleOrNilReason.md), [CodeAttribute](CodeAttribute.md), [DateAttribute](DateAttribute.md), [DoubleAttribute](DoubleAttribute.md), [IntAttribute](IntAttribute.md), [MeasureAttribute](MeasureAttribute.md), [StringAttribute](StringAttribute.md), [UriAttribute](UriAttribute.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:value |
| native | citygml:value |




## LinkML Source

<details>
```yaml
name: value
alias: value
domain_of:
- Height
- RoomHeight
- DoubleOrNilReason
- CodeAttribute
- DateAttribute
- DoubleAttribute
- IntAttribute
- MeasureAttribute
- StringAttribute
- UriAttribute
range: string

```
</details>