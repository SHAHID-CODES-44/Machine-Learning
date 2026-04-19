# Hierarchical Clustering (Dendrogram)
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import linkage, dendrogram

# Load dataset
data = load_iris()
X = data.data

# Apply clustering (using first 2 features for simplicity)
Z = linkage(X[:, :2], method='ward')

# Show first few values
print(Z[:5])
# Plot dendrogram
plt.figure(figsize=(8,5))
dendrogram(Z)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()