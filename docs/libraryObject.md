

# Slot: libraryObject 


_Specifies the URI that points to the prototypical geometry stored in an external file._





URI: [citygml:libraryObject](https://www.ogc.org/standards/citygml/libraryObject)
Alias: libraryObject

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImplicitGeometry](ImplicitGeometry.md) | ImplicitGeometry is a geometry representation where the shape is stored only ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [ImplicitGeometry](ImplicitGeometry.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | citygml:libraryObject |
| native | citygml:libraryObject |




## LinkML Source

<details>
```yaml
name: libraryObject
description: Specifies the URI that points to the prototypical geometry stored in
  an external file.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: libraryObject
owner: ImplicitGeometry
domain_of:
- ImplicitGeometry
range: uri
required: false
multivalued: false

```
</details>