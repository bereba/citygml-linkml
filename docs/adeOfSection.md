

# Slot: adeOfSection 


_Augments the Section with properties defined in an ADE._





URI: [citygml:adeOfSection](https://www.ogc.org/standards/citygml/adeOfSection)
Alias: adeOfSection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Section](Section.md) | A Section is a transportation space that is a segment of a Road, Railway, Tra... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfSection](ADEOfSection.md) |
| Domain Of | [Section](Section.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Section](Section.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfSection |
| native | citygml:adeOfSection |




## LinkML Source

<details>
```yaml
name: adeOfSection
description: Augments the Section with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfSection
owner: Section
domain_of:
- Section
range: ADEOfSection
required: false
multivalued: true

```
</details>