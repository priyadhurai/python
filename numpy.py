"""
NumPy Basics Demonstration Script
Author: Banupriya
Description:
    This script demonstrates NumPy fundamentals:
    - Creating arrays
    - Mathematical operations
    - Array indexing and slicing
    - Matrix operations
"""

import numpy as np

print("===== NumPy Basics =====")

# 1. Creating Arrays
arr1 = np.array([10, 20, 30])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# 2. Special Arrays
zeros_arr = np.zeros((3, 3))
ones_arr = np.ones((2, 4))
range_arr = np.arange(1, 11, 2)

print("Zeros Array:\n", zeros_arr)
print("Ones Array:\n", ones_arr)
print("Range Array:", range_arr)

# 3. Random Array
random_arr = np.random.randint(1, 100, size=5)
print("Random Array:", random_arr)

# 4. Operations
print("Add 10:", arr1 + 10)
print("Multiply 2:", arr1 * 2)
print("Mean:", np.mean(arr1))
print("Max:", np.max(arr1))
print("Std Dev:", np.std(arr1))

# 5. Indexing & Slicing
print("First element:", arr1[0])
print("Slice [1:3]:", arr1[1:3])

# 6. Matrix Multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.dot(A, B)

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("A x B:\n", C)

print("Program completed.")
