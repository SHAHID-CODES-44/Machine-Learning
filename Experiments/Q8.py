# Multiple Linear Regression
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("../Dataset/students_data.csv")

X = df[["Study_Hours","Attendance","Previous_Score"]]
y = df["Final_Score"]

model = LinearRegression()

model.fit(X,y)

pred = model.predict(X)

print(pred)