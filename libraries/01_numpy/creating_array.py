import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2], [3, 4]])

# Basic indexing
print(arr[0])  # Output: 1
print(arr[-1])  # Output: 5

# Slicing
print(arr[1:3])  # Output: [2, 3]
print(arr2d[0, 1])  # Output: 2