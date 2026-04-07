

# Slot: trafficDirection 



URI: [citygml:trafficDirection](https://www.ogc.org/standards/citygml/trafficDirection)
Alias: trafficDirection

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
| [TrafficSpace](TrafficSpace.md) | A TrafficSpace is a space in which traffic takes place |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AbstractTransportationSpace](AbstractTransportationSpace.md), [TrafficSpace](TrafficSpace.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:trafficDirection |
| native | citygml:trafficDirection |




## LinkML Source

<details>
```yaml
name: trafficDirection
alias: trafficDirection
domain_of:
- AbstractTransportationSpace
- TrafficSpace
range: string

```
</details>