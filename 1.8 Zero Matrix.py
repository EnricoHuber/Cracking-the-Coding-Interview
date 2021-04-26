"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""
import numpy as np


n = 8
m = 10
matrix = np.random.randint(-10, 10, size=(n, m))
print(matrix)
for index, element in np.ndenumerate(matrix):
    if element == 0:
        matrix[index[0]] = np.zeros((1, m))
        matrix[:, index[1]] = np.zeros((n, ))
print(matrix)
