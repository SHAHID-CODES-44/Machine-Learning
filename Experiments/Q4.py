# Outlier Detection Using IQR
import pandas as pd

df = pd.read_csv("../Dataset/students_data.csv")

Q1 = df["Study_Hours"].quantile(0.25)
Q3 = df["Study_Hours"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Study_Hours"] < lower) | (df["Study_Hours"] > upper)]
if outliers.empty:
    print("No outliers detected")
else:
    print("Outliers found:")
    print(outliers)
