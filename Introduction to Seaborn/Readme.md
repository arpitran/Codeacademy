## Visualizing World Cup Data With Seaborn

Matplotlib is a useful tool, but it leaves much to be desired. There are several valid complaints about matplotlib that often come up:

- Matplotlib's defaults are not exactly the best choices. It was based off of MatLab circa 1999, and this shows.
- Matplotlib is relatively low-level. Doing sophisticated statistical visualization is possible, but often requires a *lot* of boilerplate code.
- Matplotlib is not designed for use with Pandas dataframes. In order to visualize data from a Pandas dataframe, you must extract each series and often concatenate these series' together into the right format.

The answer to these problems is [Seaborn](http://stanford.edu/~mwaskom/software/seaborn/). Seaborn provides an API on top of matplotlib which uses sane plot & color defaults, uses simple functions for common statistical plot types, and which integrates with the functionality provided by Pandas dataframes.

Let's take a look at Seaborn in action. We'll start by importing the key libraries we'll need.


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

The data in WorldCupMatches.csv has the goals 
scored in each match broken up by goals for the home team 
and goals for the away team. We want to visualize 
the total number of goals scored in each match.

Add a column which is the sum of Home team goals and away team goals
```python
df["TotalGoals"]=df["Home Team Goals"]+df["Away Team Goals"]
display(df.head())
```

You are going to create a bar chart visualizing how many goals were scored 
each year the World Cup was held between 1930-2014.

Set the style of your plot to be whitegrid . This will add gridlines to 
the plot which will make it easier to read the visualization.

```python
sns.set_style("whitegrid")
```

To make the text in your visualization bigger and easier to read, 
set the context to be "poster".

```python
sns.set_context("poster")
```

If you would like to further adjust the font size of your plot, 
you can pass sns.set_context() a second optional argument using the keyword 
font_scale.

```python
sns.set_context("poster",font_scale="1.25")
```

Create a figure and axes for your plot using the syntax:
```python
f, ax = plt.subplots()
```
Inside of plt.subplots(), set the size of the figure to be 12 inches 
wide and 7 inches tall.
```python
f, ax = plt.subplots(figsize=(12, 8))
```

Using the data in df and the syntax:
```python
ax = sns.barplot()
```
visualize the columns Year and Total Goals as a bar chart.
Year should be on the x-axis, and Total Goals should be on the y-axis
```python
ax = sns.barplot(data=df,x="Year",y="TotalGoals")
```

Render your bar chart so you can see it.

```python
plt.show()
```

Effective visualizations include a clear title.
Give your bar chart a meaningful title using ax.set_title().

```python
ax.set_title("Meaningful Title")
```

Complete Code
```python
sns.set_style("whitegrid")
sns.set_context("notebook",font_scale=1.25)
f, ax = plt.subplots(figsize=(12, 8))
ax = sns.barplot(data=df,x="Year",y="TotalGoals")
ax.set_title("Meaningful Title")
plt.show()
```

For more information on plotting with Seaborn, see the
 [seaborn documentation](http://stanford.edu/~mwaskom/software/seaborn), 
 the [seaborn gallery](http://stanford.edu/~mwaskom/software/seaborn/examples/index.html), 
 and the official [seaborn tutorial](http://stanford.edu/~mwaskom/software/seaborn/tutorial.html).