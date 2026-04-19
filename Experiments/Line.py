# Line Chart
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Dataset/students_data.csv")

df = df.sort_values("Study_Hours")

plt.plot(df["Study_Hours"], df["Final_Score"])

plt.title("Study Hours vs Final Score (Line Graph)")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.grid()

plt.show()