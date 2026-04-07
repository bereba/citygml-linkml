

# Slot: adeOfWindowSurface 


_Augments the WindowSurface with properties defined in an ADE._





URI: [citygml:adeOfWindowSurface](https://www.ogc.org/standards/citygml/adeOfWindowSurface)
Alias: adeOfWindowSurface

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WindowSurface](WindowSurface.md) | A WindowSurface is either a boundary surface of a Window feature or a surface... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfWindowSurface](ADEOfWindowSurface.md) |
| Domain Of | [WindowSurface](WindowSurface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [WindowSurface](WindowSurface.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfWindowSurface |
| native | citygml:adeOfWindowSurface |




## LinkML Source

<details>
```yaml
name: adeOfWindowSurface
description: Augments the WindowSurface with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfWindowSurface
owner: WindowSurface
domain_of:
- WindowSurface
range: ADEOfWindowSurface
required: false
multivalued: true

```
</details>