# Covariance Based Feature Analysis

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/students_data.csv")

# Select only numeric columns
numeric_df = df.select_dtypes(include=np.number)

# Calculate covariance matrix
cov_matrix = numeric_df.cov()

print("Covariance Matrix:\n")
print(cov_matrix)

# Visualization
plt.figure(figsize=(8,6))
sns.heatmap(cov_matrix, annot=True, cmap="coolwarm")

plt.title("Covariance Heatmap")
plt.show()