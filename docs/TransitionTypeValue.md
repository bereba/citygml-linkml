# Enum: TransitionTypeValue 




_TransitionTypeValue enumerates the different kinds of version transitions. “planned” and “fork” should be used in cases when from one city model version multiple successor versions are being created. “realized” and “merge” should be used when different city model versions are converging into a common successor version._



URI: [citygml:TransitionTypeValue](https://www.ogc.org/standards/citygml/TransitionTypeValue)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| planned | None |  |
| realized | None |  |
| historicalSuccession | None |  |
| fork | None |  |
| merge | None |  |













## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml






## LinkML Source

<details>
```yaml
name: TransitionTypeValue
description: TransitionTypeValue enumerates the different kinds of version transitions.
  “planned” and “fork” should be used in cases when from one city model version multiple
  successor versions are being created. “realized” and “merge” should be used when
  different city model versions are converging into a common successor version.
from_schema: https://www.ogc.org/standards/citygml
rank: 1000
permissible_values:
  planned:
    text: planned
  realized:
    text: realized
  historicalSuccession:
    text: historicalSuccession
  fork:
    text: fork
  merge:
    text: merge

```
</details>