"""matrix_lab.ipynb


Original file is located at
    https://colab.research.google.com/drive/1LbFPSeOr3Tg_s1mOgMdlpjRIk0Y8zOuQ

# **SP23-BAI-046**
# **NOOR FATIMA**
# **Lab Task 1**
"""

import numpy as np

"""1. Matrix Declaration"""

matrix1 = np.array([[1,2,3],
                            [5,6,7],
                            [7,3,4]])

matrix2 = np.array([[1.5,2.5,3.5,4.5],
                          [5.5,6.5,7.5,8.5],
                          [9.5,10.5,4.5,9.5],
                          [8.5,1.5,4.5,12.5]])

print(matrix1)
print(matrix2)

"""2. Matrix Indexing"""

print("Element at 2nd row and 3rd column:" ,matrix1[1, 2])

matrix2[0,3]=20.5
print("Element at 1st row and 4rth column:" ,matrix2)

"""3. Matrix Slicing"""

print(matrix1[:2, :2])
print(matrix2[-1])