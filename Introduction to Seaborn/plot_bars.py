import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

# Load results.csv here:
df = pd.read_csv("data/results.txt")
print(df)

sns.barplot(
	 data=df ,
	 x="Gender" ,
	 y="Mean Satisfaction"
 )
plt.show()

gradebook = pd.read_csv("data/gradebook.txt")
assignment1 = gradebook[gradebook.assignment_name == "Assignment 1"]
print(assignment1)
asn1_median = np.median(assignment1.grade)
print(asn1_median)
sns.barplot(data=gradebook, x="assignment_name", y="grade")

plt.show()