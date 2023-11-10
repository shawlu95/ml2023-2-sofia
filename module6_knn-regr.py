import numpy as np

class KNNRegression:
    def __init__(self, n, k):
        self.k = k
        self.points = np.zeros([n, 2])

    def add_point(self, i, x, y):
        self.points[i, 0] = x
        self.points[i, 1] = y
        print(f"Added point ({x}, {y}) to the dataset.")

    def knn_regression(self, x_query):
        x = self.points.T[:1, ]
        y = self.points.T[1:, ]
        distances = np.linalg.norm(x - x_query, axis=0)
        sorted_indices = np.argsort(distances)
        k_nearest_neighbors = y[0][sorted_indices[:self.k]]
        y_query = np.mean(k_nearest_neighbors)
        return y_query

def main():
      N = int(input("Enter the number of points (N): "))
      k = int(input("Enter k for k-NN Regression: "))

      if k > N:
          raise ValueError("Error: k <= N.")

      knn_regressor = KNNRegression(N, k)

      print("Enter the (x, y) points:")
      xs = []
      ys = []
      for i in range(N):
          x = float(input(f"Enter x_{i} value: "))
          xs.append(x)
      for i in range(N):
          y = float(input(f"Enter y_{i} value: "))
          ys.append(y)
      for i, (x, y) in enumerate(zip(xs, ys)):
          knn_regressor.add_point(i, x, y)

      x_query = float(input("Enter the x value for prediction: "))
      result = knn_regressor.knn_regression(x_query)

      print(f"The predicted y value for x={x_query} using k-NN Regression is: {result}")


if __name__ == "__main__":
    main()
