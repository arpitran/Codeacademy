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

|    |   Year | Datetime            | Stage   | Stadium        | City       | Home Team Name   |   Home Team Goals |   Away Team Goals | Away Team Name   | Win conditions   |   Attendance |   Half-time Home Goals |   Half-time Away Goals | Referee                | Assistant 1              | Assistant 2                |   RoundID |   MatchID | Home Team Initials   | Away Team Initials   |
|---:|-------:|:--------------------|:--------|:---------------|:-----------|:-----------------|------------------:|------------------:|:-----------------|:-----------------|-------------:|-----------------------:|-----------------------:|:-----------------------|:-------------------------|:---------------------------|----------:|----------:|:---------------------|:---------------------|
|  0 |   1930 | 13 Jul 1930 - 15:00 | Group 1 | Pocitos        | Montevideo | France           |                 4 |                 1 | Mexico           |                  |         4444 |                      3 |                      0 | LOMBARDI Domingo (URU) | CRISTOPHE Henry (BEL)    | REGO Gilberto (BRA)        |       201 |      1096 | FRA                  | MEX                  |
|  1 |   1930 | 13 Jul 1930 - 15:00 | Group 4 | Parque Central | Montevideo | USA              |                 3 |                 0 | Belgium          |                  |        18346 |                      2 |                      0 | MACIAS Jose (ARG)      | MATEUCCI Francisco (URU) | WARNKEN Alberto (CHI)      |       201 |      1090 | USA                  | BEL                  |
|  2 |   1930 | 14 Jul 1930 - 12:45 | Group 2 | Parque Central | Montevideo | Yugoslavia       |                 2 |                 1 | Brazil           |                  |        24059 |                      2 |                      0 | TEJADA Anibal (URU)    | VALLARINO Ricardo (URU)  | BALWAY Thomas (FRA)        |       201 |      1093 | YUG                  | BRA                  |
|  3 |   1930 | 14 Jul 1930 - 14:50 | Group 3 | Pocitos        | Montevideo | Romania          |                 3 |                 1 | Peru             |                  |         2549 |                      1 |                      0 | WARNKEN Alberto (CHI)  | LANGENUS Jean (BEL)      | MATEUCCI Francisco (URU)   |       201 |      1098 | ROU                  | PER                  |
|  4 |   1930 | 15 Jul 1930 - 16:00 | Group 1 | Parque Central | Montevideo | Argentina        |                 1 |                 0 | France           |                  |        23409 |                      0 |                      0 | REGO Gilberto (BRA)    | SAUCEDO Ulises (BOL)     | RADULESCU Constantin (ROU) |       201 |      1085 | ARG                  | FRA                  |