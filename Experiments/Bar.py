# Bar Chart
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Dataset/students_data.csv")

df.groupby("Gender")["Final_Score"].mean().plot(kind="bar")

plt.title("Average Final Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Final Score")
plt.grid()

plt.show()