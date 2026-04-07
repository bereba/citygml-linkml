

# Slot: shininess 


_Specifies the sharpness of the specular highlight._





URI: [citygml:shininess](https://www.ogc.org/standards/citygml/shininess)
Alias: shininess

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [X3DMaterial](X3DMaterial.md) | X3DMaterial defines properties for surface geometry objects based on the mate... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DoubleBetween0and1](DoubleBetween0and1.md) |
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
| self | citygml:shininess |
| native | citygml:shininess |




## LinkML Source

<details>
```yaml
name: shininess
description: Specifies the sharpness of the specular highlight.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: shininess
owner: X3DMaterial
domain_of:
- X3DMaterial
range: DoubleBetween0and1
required: false
multivalued: false

```
</details>