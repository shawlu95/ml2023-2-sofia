import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

# Function to read a positive integer
def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a positive integer.")

# Function to read a real number
def read_real_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a real number.")

# Main program
def main():
    # Reading N and k
    N = read_positive_integer("Enter the number of data points (N): ")
    k = read_positive_integer("Enter the number of neighbors (k): ")

    # Check if k is less than or equal to N
    if k > N:
        print("Error: k should be less than or equal to N.")
        return

    # Collecting data points
    points = np.zeros((N, 2))
    for i in range(N):
        x = read_real_number(f"Enter x value for point {i+1}: ")
        y = read_real_number(f"Enter y value for point {i+1}: ")
        points[i] = [x, y]

    # Splitting points into X and Y
    X_train = points[:, 0].reshape(-1, 1)
    Y_train = points[:, 1]

    # Creating and training the k-NN model
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train, Y_train)

    # Predicting for a new X value
    X_test = read_real_number("Enter a new X value to predict Y: ")
    Y_pred = knn.predict([[X_test]])

    # Calculating coefficient of determination
    r2 = r2_score(Y_train, knn.predict(X_train))

    print(f"Predicted Y value: {Y_pred[0]}")
    print(f"Coefficient of determination (R² score): {r2}")

if __name__ == "__main__":
    main()
