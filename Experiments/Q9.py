# Naive Bayes Classifier
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("../Dataset/students_data.csv")

le = LabelEncoder()

df["Gender"] = le.fit_transform(df["Gender"])
df["Passed"] = le.fit_transform(df["Passed"])

X = df[["Age","Study_Hours","Attendance","Previous_Score"]]
y = df["Passed"]

model = GaussianNB()

model.fit(X,y)

pred = model.predict(X)

print(pred)