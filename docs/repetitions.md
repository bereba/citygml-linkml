

# Slot: repetitions 


_Specifies how often the timeseries that is referenced by the TimeseriesComponent should be iterated._





URI: [citygml:repetitions](https://www.ogc.org/standards/citygml/repetitions)
Alias: repetitions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TimeseriesComponent](TimeseriesComponent.md) | TimeseriesComponent represents an element of a CompositeTimeseries |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [TimeseriesComponent](TimeseriesComponent.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TimeseriesComponent](TimeseriesComponent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:repetitions |
| native | citygml:repetitions |




## LinkML Source

<details>
```yaml
name: repetitions
description: Specifies how often the timeseries that is referenced by the TimeseriesComponent
  should be iterated.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: repetitions
owner: TimeseriesComponent
domain_of:
- TimeseriesComponent
range: integer
required: true
multivalued: false

```
</details>