# Handling Missing Value
import pandas as pd

df = pd.read_csv("../Dataset/students_data.csv")

df.loc[3, "Study_Hours"] = None

missing = pd.DataFrame(df.isnull().sum(), columns=["Missing Values"])

print("Missing Value Table")
print(missing)

df = df.fillna(df.mean(numeric_only=True))

print("\nCleaned Dataset")
print(df)