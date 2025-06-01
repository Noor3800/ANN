"""data_analysis_lab.ipynb

Original file is located at
    https://colab.research.google.com/drive/1tHI10ObXRpMOb1tni_kfT2H3bAQ5fxNA

# **Lab Task 3**
"""

import numpy as np
import matplotlib.pyplot as plt

"""Load and display dataset"""

data = np.array([[1, 85, 78, 92],
                 [2, 76, 85, 88],
                 [3, 90, 92, 95],
                 [4, 68, 72, 70],
                 [5, 88, 89, 94]])

print(data)

"""Extract and analyze"""

math_grades = data[:, 1]
science_grades = data[:, 2]
english_grades = data[:, 3]

math_avg = np.mean(math_grades)
science_avg = np.mean(science_grades)
english_avg = np.mean(english_grades)

print("Math Average:", math_avg)
print("Science Average:", science_avg)
print("English Average:", english_avg)

"""Basic stastical analysis"""

student_averages = np.mean(data[:, 1:], axis=1)

highest_avg_student = np.argmax(student_averages) + 1
lowest_avg_student = np.argmin(student_averages) + 1

print("student average", student_averages)
print("Highest Average Student:", highest_avg_student)
print("Lowest Average Student:", lowest_avg_student)

"""Manipulate and Transform"""

math_grades += 5
new_student_averages = np.mean(np.column_stack((math_grades, science_grades, english_grades)), axis=1)

print("New Student Averages:", new_student_averages)