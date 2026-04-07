

# Slot: crs 



URI: [citygml:crs](https://www.ogc.org/standards/citygml/crs)
Alias: crs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TexCoordGen](TexCoordGen.md) | TexCoordGen defines texture parameterization using a transformation matrix |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [TexCoordGen](TexCoordGen.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TexCoordGen](TexCoordGen.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:crs |
| native | citygml:crs |




## LinkML Source

<details>
```yaml
name: crs
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: crs
owner: TexCoordGen
domain_of:
- TexCoordGen
range: string
required: false
multivalued: false

```
</details>