# Pie Chart
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Dataset/students_data.csv")

df["Passed"].value_counts().plot.pie(autopct='%1.1f%%')

plt.title("Pass vs Fail Distribution")

plt.show()