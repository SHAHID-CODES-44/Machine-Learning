# Scatter Plot
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Dataset/students_data.csv")

plt.scatter(df["Study_Hours"], df["Final_Score"])

plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.grid()

plt.show()