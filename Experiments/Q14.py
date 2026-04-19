# Decision Tree Classifier (Iris)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load data
data = load_iris()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Create model
model = DecisionTreeClassifier(max_depth=4)

# Train model
model.fit(X_train, y_train)

# Check accuracy
accuracy = model.score(X_test, y_test)
print("Decision Tree Accuracy:", accuracy)