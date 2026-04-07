

# Slot: adeOfGeoreferencedTexture 


_Augments the GeoreferencedTexture with properties defined in an ADE._





URI: [citygml:adeOfGeoreferencedTexture](https://www.ogc.org/standards/citygml/adeOfGeoreferencedTexture)
Alias: adeOfGeoreferencedTexture

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeoreferencedTexture](GeoreferencedTexture.md) | A GeoreferencedTexture is a texture that uses a planimetric projection |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfGeoreferencedTexture](ADEOfGeoreferencedTexture.md) |
| Domain Of | [GeoreferencedTexture](GeoreferencedTexture.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [GeoreferencedTexture](GeoreferencedTexture.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfGeoreferencedTexture |
| native | citygml:adeOfGeoreferencedTexture |




## LinkML Source

<details>
```yaml
name: adeOfGeoreferencedTexture
description: Augments the GeoreferencedTexture with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfGeoreferencedTexture
owner: GeoreferencedTexture
domain_of:
- GeoreferencedTexture
range: ADEOfGeoreferencedTexture
required: false
multivalued: true

```
</details>