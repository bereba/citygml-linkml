

# Slot: adeOfAbstractFillingSurface 


_Augments AbstractFillingSurface with properties defined in an ADE._





URI: [citygml:adeOfAbstractFillingSurface](https://www.ogc.org/standards/citygml/adeOfAbstractFillingSurface)
Alias: adeOfAbstractFillingSurface

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WindowSurface](WindowSurface.md) | A WindowSurface is either a boundary surface of a Window feature or a surface... |  no  |
| [DoorSurface](DoorSurface.md) | A DoorSurface is either a boundary surface of a Door feature or a surface tha... |  no  |
| [AbstractFillingSurface](AbstractFillingSurface.md) | AbstractFillingSurface is the abstract superclass for different kinds of surf... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractFillingSurface](ADEOfAbstractFillingSurface.md) |
| Domain Of | [AbstractFillingSurface](AbstractFillingSurface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractFillingSurface](AbstractFillingSurface.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractFillingSurface |
| native | citygml:adeOfAbstractFillingSurface |




## LinkML Source

<details>
```yaml
name: adeOfAbstractFillingSurface
description: Augments AbstractFillingSurface with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractFillingSurface
owner: AbstractFillingSurface
domain_of:
- AbstractFillingSurface
range: ADEOfAbstractFillingSurface
required: false
multivalued: true

```
</details>