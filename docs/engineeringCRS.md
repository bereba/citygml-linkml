

# Slot: engineeringCRS 


_Specifies the local engineering coordinate reference system of the CityModel that can be provided inline the CityModel instead of referencing a well-known CRS definition. The definition of an engineering CRS requires an anchor point which relates the origin of the local coordinate system to a point on the earth's surface in order to facilitate the transformation of coordinates from the local engineering CRS._





URI: [citygml:engineeringCRS](https://www.ogc.org/standards/citygml/engineeringCRS)
Alias: engineeringCRS

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CityModel](CityModel.md) | CityModel is the container for all objects belonging to a city model |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CityModel](CityModel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CityModel](CityModel.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:engineeringCRS |
| native | citygml:engineeringCRS |




## LinkML Source

<details>
```yaml
name: engineeringCRS
description: Specifies the local engineering coordinate reference system of the CityModel
  that can be provided inline the CityModel instead of referencing a well-known CRS
  definition. The definition of an engineering CRS requires an anchor point which
  relates the origin of the local coordinate system to a point on the earth's surface
  in order to facilitate the transformation of coordinates from the local engineering
  CRS.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
alias: engineeringCRS
owner: CityModel
domain_of:
- CityModel
range: string
required: false
multivalued: false

```
</details>