

# Slot: isSmooth 


_Specifies which interpolation method is used for the shading of the surface geometry object. If the attribute is set to true, vertex normals should be used for shading (Gouraud shading). Otherwise, normals should be constant for a surface patch (flat shading)._





URI: [citygml:isSmooth](https://www.ogc.org/standards/citygml/isSmooth)
Alias: isSmooth

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [X3DMaterial](X3DMaterial.md) | X3DMaterial defines properties for surface geometry objects based on the mate... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [X3DMaterial](X3DMaterial.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [X3DMaterial](X3DMaterial.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:isSmooth |
| native | citygml:isSmooth |




## LinkML Source

<details>
```yaml
name: isSmooth
description: Specifies which interpolation method is used for the shading of the surface
  geometry object. If the attribute is set to true, vertex normals should be used
  for shading (Gouraud shading). Otherwise, normals should be constant for a surface
  patch (flat shading).
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: isSmooth
owner: X3DMaterial
domain_of:
- X3DMaterial
range: boolean
required: false
multivalued: false

```
</details>