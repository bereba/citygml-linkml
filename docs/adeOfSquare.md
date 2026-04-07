

# Slot: adeOfSquare 


_Augments the Square with properties defined in an ADE._





URI: [citygml:adeOfSquare](https://www.ogc.org/standards/citygml/adeOfSquare)
Alias: adeOfSquare

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Square](Square.md) | A Square is a transportation space for unrestricted movement for vehicles, bi... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfSquare](ADEOfSquare.md) |
| Domain Of | [Square](Square.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Square](Square.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfSquare |
| native | citygml:adeOfSquare |




## LinkML Source

<details>
```yaml
name: adeOfSquare
description: Augments the Square with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfSquare
owner: Square
domain_of:
- Square
range: ADEOfSquare
required: false
multivalued: true

```
</details>