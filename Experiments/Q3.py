# Merging Data Sources – CSV File (Merge, Concat, Join)
import pandas as pd

df1 = pd.read_csv("../Dataset/students_data.csv")
df2 = pd.read_csv("../Dataset/students_data.csv")

merge = pd.merge(df1, df2, on="Student_ID")
concat = pd.concat([df1, df2])
join = df1.join(df2, lsuffix="_left", rsuffix="_right")

print("MERGE RESULT")
print(merge.head())

print("\nCONCAT RESULT")
print(concat.head())

print("\nJOIN RESULT")
print(join.head())