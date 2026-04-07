

# Slot: granularity 



URI: [citygml:granularity](https://www.ogc.org/standards/citygml/granularity)
Alias: granularity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrafficSpace](TrafficSpace.md) | A TrafficSpace is a space in which traffic takes place |  no  |
| [AuxiliaryTrafficSpace](AuxiliaryTrafficSpace.md) | An AuxiliaryTrafficSpace is a space within the transportation space not inten... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AuxiliaryTrafficSpace](AuxiliaryTrafficSpace.md), [TrafficSpace](TrafficSpace.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:granularity |
| native | citygml:granularity |




## LinkML Source

<details>
```yaml
name: granularity
alias: granularity
domain_of:
- AuxiliaryTrafficSpace
- TrafficSpace
range: string

```
</details>