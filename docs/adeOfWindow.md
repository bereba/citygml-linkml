

# Slot: adeOfWindow 


_Augments the Window with properties defined in an ADE._





URI: [citygml:adeOfWindow](https://www.ogc.org/standards/citygml/adeOfWindow)
Alias: adeOfWindow

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Window](Window.md) | A Window is a construction for closing an opening in a wall  or roof, primari... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfWindow](ADEOfWindow.md) |
| Domain Of | [Window](Window.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Window](Window.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfWindow |
| native | citygml:adeOfWindow |




## LinkML Source

<details>
```yaml
name: adeOfWindow
description: Augments the Window with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfWindow
owner: Window
domain_of:
- Window
range: ADEOfWindow
required: false
multivalued: true

```
</details>