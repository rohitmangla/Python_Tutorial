import numpy as np
from numpy import dot

# Create a 2x2 matrix A
A = np.array ([[1, 2], [ 3 , 4]])
print (A)

# Create a 3x3 matrix B
B = np.array ([[2, 5, 7], [9, 6 , 2], [1, 4, 9]])
print (B)

# Create a 3x3 matrix C
C = np.array ([[1, 2, 3], [8, 2, 5], [4, 9, 7 ]])
print (C)
# Addition of two matrices [D= B+C]
D= B+C
print ('D =', D)

# matrix .dot product
E = dot (C, D)

