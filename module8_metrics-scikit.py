import numpy as np
from sklearn.metrics import precision_score, recall_score

def read_array(N):
    A = np.empty(N, dtype=int)
    for i in range(N):
        while True:
            try:
                x = int(input(f"for point {i + 1} (0 or 1): "))
                if x == 0 or x == 1:
                    A[i] = x
                    break
                else:
                    print(f"{A} class label should be 0 or 1.")
            except ValueError:
                print("Invalid input. Please enter 0 or 1 for the {A} class label.")

N = int(input("Enter the number of data points (N): "))

print("Enter the class labels for the predicted values (X):")
X = read_array(N)

print("Enter the class labels for the actual values (Y):")
Y = read_array(N)

# Calculate Precision and Recall using scikit-learn
precision = precision_score(X, Y)
recall = recall_score(X, Y)
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")