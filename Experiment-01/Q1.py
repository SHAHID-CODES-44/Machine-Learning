# Merging Data Sources – Excel File
import pandas as pd

df1 = pd.read_excel("../Dataset/students_data.xlsx")
df2 = pd.read_excel("../Dataset/students_data.xlsx")

merged = pd.merge(df1, df2, on="Student_ID")

print(merged.head())