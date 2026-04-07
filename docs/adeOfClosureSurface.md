

# Slot: adeOfClosureSurface 


_Augments the ClosureSurface with properties defined in an ADE._





URI: [citygml:adeOfClosureSurface](https://www.ogc.org/standards/citygml/adeOfClosureSurface)
Alias: adeOfClosureSurface

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClosureSurface](ClosureSurface.md) | ClosureSurface is a special type of thematic surface used to close holes in v... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfClosureSurface](ADEOfClosureSurface.md) |
| Domain Of | [ClosureSurface](ClosureSurface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ClosureSurface](ClosureSurface.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfClosureSurface |
| native | citygml:adeOfClosureSurface |




## LinkML Source

<details>
```yaml
name: adeOfClosureSurface
description: Augments the ClosureSurface with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfClosureSurface
owner: ClosureSurface
domain_of:
- ClosureSurface
range: ADEOfClosureSurface
required: false
multivalued: true

```
</details>