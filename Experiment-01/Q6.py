# Feature Correlation
import pandas as pd

df = pd.read_csv("../Dataset/students_data.csv")

corr = df.corr(numeric_only=True)

print(corr)