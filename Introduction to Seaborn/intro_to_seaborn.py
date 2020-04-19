
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('data/survey.txt')
print(df)

import math

print("Hello World")

x = int(input("Enter a number\n"))
y = int(input("Enter another numebr\n"))

hypo = x**2 + 11**2
h = math.sqrt(hypo)

print(h)

df = pd.read_csv("data/results.txt")
print(df)


sns.barplot(
	 data=df ,
	 x="Gender" ,
	 y="Mean Satisfaction"
 )
plt.show()
