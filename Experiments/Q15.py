# Random Forest Classifier (Iris)
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load data
data = load_iris()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Create model
model = RandomForestClassifier(n_estimators=100)

# Train model
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("Random Forest Accuracy:", accuracy)

# Feature importance
importances = model.feature_importances_
features = data.feature_names

print("Feature Importance:", importances)

# Plot graph
plt.bar(features, importances)
plt.title("Feature Importance (Iris)")
plt.xticks(rotation=45)
plt.show()