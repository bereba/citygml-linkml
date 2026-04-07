

# Slot: targetResource 


_Specifies the URI that points to the object in the external information system._





URI: [citygml:targetResource](https://www.ogc.org/standards/citygml/targetResource)
Alias: targetResource

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
| Required | Yes |
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
| self | citygml:targetResource |
| native | citygml:targetResource |




## LinkML Source

<details>
```yaml
name: targetResource
description: Specifies the URI that points to the object in the external information
  system.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: targetResource
owner: ExternalReference
domain_of:
- ExternalReference
range: uri
required: true
multivalued: false

```
</details>