# Feature Selection using ANOVA F-Score

import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif

# Load dataset
df = pd.read_csv("../Dataset/students_data.csv")

# Convert Passed column to numeric (important step)
df["Passed"] = df["Passed"].map({"Yes": 1, "No": 0})

# Features (X) and Target (y)
X = df[["Age", "Study_Hours", "Attendance", "Previous_Score", "Final_Score"]]
y = df["Passed"]

# Apply ANOVA F-Test
selector = SelectKBest(score_func=f_classif, k=3)

X_new = selector.fit_transform(X, y)

# Get feature scores
scores = selector.scores_

# Display scores
feature_scores = pd.DataFrame({
    "Feature": X.columns,
    "Score": scores
})

print("Feature Scores:\n")
print(feature_scores.sort_values(by="Score", ascending=False))

# Show selected features
selected_features = X.columns[selector.get_support()]

print("\nTop Selected Features:\n")
print(selected_features)