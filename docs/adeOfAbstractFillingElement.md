

# Slot: adeOfAbstractFillingElement 


_Augments AbstractFillingElement with properties defined in an ADE._





URI: [citygml:adeOfAbstractFillingElement](https://www.ogc.org/standards/citygml/adeOfAbstractFillingElement)
Alias: adeOfAbstractFillingElement

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AbstractFillingElement](AbstractFillingElement.md) | AbstractFillingElement is the abstract superclass for different kinds of elem... |  no  |
| [Door](Door.md) | A Door is a construction for closing an opening intended primarily for access... |  no  |
| [Window](Window.md) | A Window is a construction for closing an opening in a wall  or roof, primari... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractFillingElement](ADEOfAbstractFillingElement.md) |
| Domain Of | [AbstractFillingElement](AbstractFillingElement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractFillingElement](AbstractFillingElement.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractFillingElement |
| native | citygml:adeOfAbstractFillingElement |




## LinkML Source

<details>
```yaml
name: adeOfAbstractFillingElement
description: Augments AbstractFillingElement with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractFillingElement
owner: AbstractFillingElement
domain_of:
- AbstractFillingElement
range: ADEOfAbstractFillingElement
required: false
multivalued: true

```
</details>