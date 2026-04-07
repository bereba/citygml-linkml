

# Slot: adeOfAbstractTexture 


_Augments AbstractTexture with properties defined in an ADE._





URI: [citygml:adeOfAbstractTexture](https://www.ogc.org/standards/citygml/adeOfAbstractTexture)
Alias: adeOfAbstractTexture

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AbstractTexture](AbstractTexture.md) | AbstractTexture is the abstract superclass to represent the common attributes... |  no  |
| [GeoreferencedTexture](GeoreferencedTexture.md) | A GeoreferencedTexture is a texture that uses a planimetric projection |  no  |
| [ParameterizedTexture](ParameterizedTexture.md) | A ParameterizedTexture is a texture that uses texture coordinates or a transf... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractTexture](ADEOfAbstractTexture.md) |
| Domain Of | [AbstractTexture](AbstractTexture.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractTexture](AbstractTexture.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractTexture |
| native | citygml:adeOfAbstractTexture |




## LinkML Source

<details>
```yaml
name: adeOfAbstractTexture
description: Augments AbstractTexture with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractTexture
owner: AbstractTexture
domain_of:
- AbstractTexture
range: ADEOfAbstractTexture
required: false
multivalued: true

```
</details>