

# Slot: relationType 


_Specifies a URI that additionally qualifies the ExternalReference. The URI can point to a definition from an external ontology (e.g., the sameAs relation from OWL) and allows for mapping the ExternalReference to RDF triples._





URI: [citygml:relationType](https://www.ogc.org/standards/citygml/relationType)
Alias: relationType

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
| self | citygml:relationType |
| native | citygml:relationType |




## LinkML Source

<details>
```yaml
name: relationType
description: Specifies a URI that additionally qualifies the ExternalReference. The
  URI can point to a definition from an external ontology (e.g., the sameAs relation
  from OWL) and allows for mapping the ExternalReference to RDF triples.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: relationType
owner: ExternalReference
domain_of:
- ExternalReference
range: uri
required: false
multivalued: false

```
</details>