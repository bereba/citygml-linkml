

# Slot: section 



URI: [citygml:section](https://www.ogc.org/standards/citygml/section)
Alias: section

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Waterway](Waterway.md) | A Waterway is a transportation space used for the movement of vessels upon or... |  no  |
| [Railway](Railway.md) | A Railway is a transportation space used by wheeled vehicles on rails |  no  |
| [Road](Road.md) | A Road is a transportation space used by vehicles, bicycles and/or pedestrian... |  no  |
| [Track](Track.md) | A Track is a small path mainly used by pedestrians |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Railway](Railway.md), [Road](Road.md), [Track](Track.md), [Waterway](Waterway.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:section |
| native | citygml:section |




## LinkML Source

<details>
```yaml
name: section
alias: section
domain_of:
- Railway
- Road
- Track
- Waterway
range: string

```
</details>