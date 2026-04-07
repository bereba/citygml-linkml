

# Slot: adeOfAbstractFurniture 


_Augments AbstractFurniture with properties defined in an ADE._





URI: [citygml:adeOfAbstractFurniture](https://www.ogc.org/standards/citygml/adeOfAbstractFurniture)
Alias: adeOfAbstractFurniture

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AbstractFurniture](AbstractFurniture.md) | AbstractFurniture is the abstract superclass for the representation of furnit... |  no  |
| [TunnelFurniture](TunnelFurniture.md) | A TunnelFurniture is an equipment for occupant use, usually not fixed to the ... |  no  |
| [BridgeFurniture](BridgeFurniture.md) | A BridgeFurniture is an equipment for occupant use, usually not fixed to the ... |  no  |
| [BuildingFurniture](BuildingFurniture.md) | A BuildingFurniture is an equipment for occupant use, usually not fixed to th... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ADEOfAbstractFurniture](ADEOfAbstractFurniture.md) |
| Domain Of | [AbstractFurniture](AbstractFurniture.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractFurniture](AbstractFurniture.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:adeOfAbstractFurniture |
| native | citygml:adeOfAbstractFurniture |




## LinkML Source

<details>
```yaml
name: adeOfAbstractFurniture
description: Augments AbstractFurniture with properties defined in an ADE.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: adeOfAbstractFurniture
owner: AbstractFurniture
domain_of:
- AbstractFurniture
range: ADEOfAbstractFurniture
required: false
multivalued: true

```
</details>