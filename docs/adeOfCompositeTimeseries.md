

# Slot: adeOfCompositeTimeseries 


_Augments the CompositeTimeseries with properties defined in an ADE._





URI: [citygml:adeOfCompositeTimeseries](https://www.ogc.org/standards/citygml/adeOfCompositeTimeseries)
Alias: adeOfCompositeTimeseries

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CompositeTimeseries](CompositeTimeseries.md) | A CompositeTimeseries is a (possibly recursive) aggregation of atomic and com... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfCompositeTimeseries](ADEOfCompositeTimeseries.md) |
| Domain Of | [CompositeTimeseries](CompositeTimeseries.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | citygml:adeOfCompositeTimeseries |
| native | citygml:adeOfCompositeTimeseries |




## LinkML Source

<details>
```yaml
name: adeOfCompositeTimeseries
description: Augments the CompositeTimeseries with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfCompositeTimeseries
owner: CompositeTimeseries
domain_of:
- CompositeTimeseries
range: ADEOfCompositeTimeseries
required: false
multivalued: true

```
</details>