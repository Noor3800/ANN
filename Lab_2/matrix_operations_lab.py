"""matrix_operations_lab.ipynb


Original file is located at
    https://colab.research.google.com/drive/1fv4KYOMyGU5vpuK5fOXsYtS7Tji85A0i

# **Lab Task 2**

1. Matrix Declaration
"""

import numpy as np

matrix_int = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

matrix_float = np.array([[1.1, 2.2, 3.3],
                        [4.4, 5.5, 6.6],
                        [7.7, 8.8, 9.9]])

print(matrix_int)
print(matrix_float)

"""2.Basic Matrix Operations"""

element_addition = matrix_int + matrix_float
element_multiplication = matrix_int * matrix_float
transpose = matrix_int.T

print(element_addition)
print(element_multiplication)
print(transpose)

"""3.Advanced Matrix Operations"""

matrix_multiplication = np.dot(matrix_int, matrix_float)
determinant = np.linalg.det(matrix_int)
inverse= np.linalg.inv(matrix_float)

print(matrix_multiplication)
print(determinant)
print(inverse)

