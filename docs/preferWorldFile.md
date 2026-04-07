

# Slot: preferWorldFile 


_Indicates whether the georeference from the image file or the accompanying world file should be preferred._





URI: [citygml:preferWorldFile](https://www.ogc.org/standards/citygml/preferWorldFile)
Alias: preferWorldFile

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeoreferencedTexture](GeoreferencedTexture.md) | A GeoreferencedTexture is a texture that uses a planimetric projection |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [GeoreferencedTexture](GeoreferencedTexture.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | citygml:preferWorldFile |
| native | citygml:preferWorldFile |




## LinkML Source

<details>
```yaml
name: preferWorldFile
description: Indicates whether the georeference from the image file or the accompanying
  world file should be preferred.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: preferWorldFile
owner: GeoreferencedTexture
domain_of:
- GeoreferencedTexture
range: boolean
required: false
multivalued: false

```
</details>