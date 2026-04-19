# Feature Selection and Data Reduction

import pandas as pd

# Load dataset
df = pd.read_csv("../Dataset/students_data.csv")

print("Original Data:\n")
print(df.head())

# Drop unnecessary column (ID doesn't affect prediction)
df_reduced = df.drop(columns=["Student_ID"])

print("\nAfter Removing Unnecessary Column:\n")
print(df_reduced.head())

# Selecting only important features
selected_features = df[["Study_Hours", "Attendance", "Previous_Score", "Final_Score"]]

print("\nSelected Important Features:\n")
print(selected_features.head())