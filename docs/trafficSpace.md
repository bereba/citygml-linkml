

# Slot: trafficSpace 


_Relates to the traffic spaces that are part of the transportation space._





URI: [citygml:trafficSpace](https://www.ogc.org/standards/citygml/trafficSpace)
Alias: trafficSpace

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Section](Section.md) | A Section is a transportation space that is a segment of a Road, Railway, Tra... |  no  |
| [Waterway](Waterway.md) | A Waterway is a transportation space used for the movement of vessels upon or... |  no  |
| [Railway](Railway.md) | A Railway is a transportation space used by wheeled vehicles on rails |  no  |
| [Road](Road.md) | A Road is a transportation space used by vehicles, bicycles and/or pedestrian... |  no  |
| [Track](Track.md) | A Track is a small path mainly used by pedestrians |  no  |
| [Square](Square.md) | A Square is a transportation space for unrestricted movement for vehicles, bi... |  no  |
| [AbstractTransportationSpace](AbstractTransportationSpace.md) | AbstractTransportationSpace is the abstract superclass of transportation obje... |  no  |
| [Intersection](Intersection.md) | An Intersection is a transportation space that is a shared segment of multipl... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TrafficSpace](TrafficSpace.md) |
| Domain Of | [AbstractTransportationSpace](AbstractTransportationSpace.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AbstractTransportationSpace](AbstractTransportationSpace.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:trafficSpace |
| native | citygml:trafficSpace |




## LinkML Source

<details>
```yaml
name: trafficSpace
description: Relates to the traffic spaces that are part of the transportation space.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: trafficSpace
owner: AbstractTransportationSpace
domain_of:
- AbstractTransportationSpace
range: TrafficSpace
required: false
multivalued: true

```
</details>