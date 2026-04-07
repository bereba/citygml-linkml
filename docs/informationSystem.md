

# Slot: informationSystem 


_Specifies the URI that points to the external information system._





URI: [citygml:informationSystem](https://www.ogc.org/standards/citygml/informationSystem)
Alias: informationSystem

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExternalReference](ExternalReference.md) | ExternalReference is a reference to a corresponding object in another informa... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [ExternalReference](ExternalReference.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ExternalReference](ExternalReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:informationSystem |
| native | citygml:informationSystem |




## LinkML Source

<details>
```yaml
name: informationSystem
description: Specifies the URI that points to the external information system.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: informationSystem
owner: ExternalReference
domain_of:
- ExternalReference
range: uri
required: false
multivalued: false

```
</details>