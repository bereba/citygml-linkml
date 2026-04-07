

# Slot: ambientIntensity 


_Specifies the minimum percentage of diffuseColor that is visible regardless of light sources._





URI: [citygml:ambientIntensity](https://www.ogc.org/standards/citygml/ambientIntensity)
Alias: ambientIntensity

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
| self | citygml:ambientIntensity |
| native | citygml:ambientIntensity |




## LinkML Source

<details>
```yaml
name: ambientIntensity
description: Specifies the minimum percentage of diffuseColor that is visible regardless
  of light sources.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: ambientIntensity
owner: X3DMaterial
domain_of:
- X3DMaterial
range: DoubleBetween0and1
required: false
multivalued: false

```
</details>