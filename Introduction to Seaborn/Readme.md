## Visualizing World Cup Data With Seaborn

A little primer on the Fifa World Cup: The FIFA World Cup, or simply the World Cup, is an international fútbol competition where 32 countries qualify to send teams made up of the best players from that nation to compete against each other for the World Cup championship.

The World Cup championship has been awarded every four years since the inaugural tournament in 1930, except in 1942 and 1946 when it was not held because of the Second World War.

The current format of the tournament involves 32 teams competing for the title at venues within the host nation over a period of one month.

Import the models you will be using in this project. 
```python
#load the packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
Load the Data Frame and Inspect the data frame
```python
df = pd.read_csv("data/WorldCupMatches.csv")
display(df)

```

|    |         A |        B |         C |        D |
|---:|----------:|---------:|----------:|---------:|
|  0 | 0.469294  | 0.191427 | 0.585911  | 0.200162 |
|  1 | 0.74057   | 0.96346  | 0.59603   | 0.675298 |
|  2 | 0.742893  | 0.495007 | 0.0825576 | 0.236011 |
|  3 | 0.0569408 | 0.608854 | 0.945528  | 0.370119 |
|  4 | 0.947972  | 0.19386  | 0.0729927 | 0.212709 |
|  5 | 0.615882  | 0.374566 | 0.399265  | 0.188595 |
|  6 | 0.310301  | 0.866071 | 0.202605  | 0.295075 |
|  7 | 0.380198  | 0.748381 | 0.148389  | 0.23381  |
|  8 | 0.975261  | 0.935911 | 0.417544  | 0.711685 |
|  9 | 0.758021  | 0.550602 | 0.066535  | 0.858383 |