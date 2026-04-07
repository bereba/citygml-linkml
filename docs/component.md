

# Slot: component 


_Relates to the atomic and composite timeseries that are part of the CompositeTimeseries. The referenced timeseries are sequentially ordered._





URI: [citygml:component](https://www.ogc.org/standards/citygml/component)
Alias: component

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CompositeTimeseries](CompositeTimeseries.md) | A CompositeTimeseries is a (possibly recursive) aggregation of atomic and com... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TimeseriesComponent](TimeseriesComponent.md) |
| Domain Of | [CompositeTimeseries](CompositeTimeseries.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CompositeTimeseries](CompositeTimeseries.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:component |
| native | citygml:component |




## LinkML Source

<details>
```yaml
name: component
description: Relates to the atomic and composite timeseries that are part of the CompositeTimeseries.
  The referenced timeseries are sequentially ordered.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: component
owner: CompositeTimeseries
domain_of:
- CompositeTimeseries
range: TimeseriesComponent
required: true
multivalued: true

```
</details>