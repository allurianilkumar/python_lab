# matrix_operations_numpy.py

import numpy as np
# Define two matrices using numpy arrays
A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])
# Addition of matrices
added_matrix = np.add(A, B)
print("Addition of A and B:")
print(added_matrix)

# Transpose of matrix A
transposed_A = np.transpose(A)
print("\nTranspose of A:")
print(transposed_A)

# Multiplication of matrices
multiplied_matrix = np.dot(A, B)
print("\nMultiplication of A and B:")
print(multiplied_matrix)
