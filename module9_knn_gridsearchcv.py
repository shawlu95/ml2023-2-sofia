"""
This program first reads the training and test data from the user
and then performs a hyperparameter search using GridSearchCV to f
ind the best k value for the kNN Classifier. Finally, it trains 
the kNN Classifier with the best k value and calculates the test accuracy.
"""
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def read_data(num_samples):
    x_values = []
    y_values = []
    for i in range(num_samples):
        x = float(input(f"Enter x value for sample {i + 1}: "))
        y = int(input(f"Enter y value for sample {i + 1}: "))
        x_values.append(x)
        y_values.append(y)
    return np.array(x_values), np.array(y_values)

N = int(input("Enter the number of training samples (N): "))
M = int(input("Enter the number of test samples (M): "))
train_x, train_y = read_data(N)
test_x, test_y = read_data(M)

# Range of k values to search
k_values = list(range(1, 11))


knn = KNeighborsClassifier()
param_grid = {'n_neighbors': k_values}
grid_search = GridSearchCV(knn, param_grid, cv=5)
grid_search.fit(train_x.reshape(-1, 1), train_y)

best_k = grid_search.best_params_['n_neighbors']

# train the model with the best k
best_knn = KNeighborsClassifier(n_neighbors=best_k)
best_knn.fit(train_x.reshape(-1, 1), train_y)

# Make predictions on the test set
test_predictions = best_knn.predict(test_x.reshape(-1, 1))

# Calculate the test accuracy
test_accuracy = accuracy_score(test_y, test_predictions)

# Output the results
print(f"Best k for kNN Classifier: {best_k}")
print(f"Test Accuracy: {test_accuracy:.2f}")