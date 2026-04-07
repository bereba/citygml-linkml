

# Slot: theme 


_Specifies the topic of the Appearance. Each Appearance contains surface data for one theme only. Examples of themes are infrared radiation, noise pollution, or earthquake-induced structural stress._





URI: [citygml:theme](https://www.ogc.org/standards/citygml/theme)
Alias: theme

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Appearance](Appearance.md) | An Appearance is a collection of surface data, i |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Appearance](Appearance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Appearance](Appearance.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:theme |
| native | citygml:theme |




## LinkML Source

<details>
```yaml
name: theme
description: Specifies the topic of the Appearance. Each Appearance contains surface
  data for one theme only. Examples of themes are infrared radiation, noise pollution,
  or earthquake-induced structural stress.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: theme
owner: Appearance
domain_of:
- Appearance
range: string
required: false
multivalued: false

```
</details>