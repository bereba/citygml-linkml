

# Slot: objectID 



URI: [citygml:objectID](https://www.ogc.org/standards/citygml/objectID)
Alias: objectID

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImplicitGeometry](ImplicitGeometry.md) | ImplicitGeometry is a geometry representation where the shape is stored only ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ID](ID.md) |
| Domain Of | [ImplicitGeometry](ImplicitGeometry.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImplicitGeometry](ImplicitGeometry.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:objectID |
| native | citygml:objectID |




## LinkML Source

<details>
```yaml
name: objectID
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: objectID
owner: ImplicitGeometry
domain_of:
- ImplicitGeometry
range: ID
required: true
multivalued: false

```
</details>