# Data wrangling and Feature Scaling
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("../Dataset/students_data.csv")

scaler = MinMaxScaler()

df[["Age","Study_Hours","Attendance","Previous_Score","Final_Score"]] = scaler.fit_transform(
df[["Age","Study_Hours","Attendance","Previous_Score","Final_Score"]])

print(df.head())