

# Slot: imageURI 


_Specifies the URI that points to the external image data file._





URI: [citygml:imageURI](https://www.ogc.org/standards/citygml/imageURI)
Alias: imageURI

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
| Range | [Uri](Uri.md) |
| Domain Of | [AbstractTexture](AbstractTexture.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | citygml:imageURI |
| native | citygml:imageURI |




## LinkML Source

<details>
```yaml
name: imageURI
description: Specifies the URI that points to the external image data file.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: imageURI
owner: AbstractTexture
domain_of:
- AbstractTexture
range: uri
required: true
multivalued: false

```
</details>