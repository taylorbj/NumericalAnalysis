import numpy as np

def backward(A, b):
    x = np.zeros_like(b)
    n = b.shape[0]
    matrix_n = A.shape[0]
    #Check dimension compatibility
    if (n != matrix_n):
        print("Incompatible dimensions")
    x[-1] = (1. / A[-1][-1]) * b[-1]
    for i in range(n-2, -1, -1):
        x[i] = (1. / A[i][i]) * (b[i] - np.sum(A[i][i+1:] * x[i+1:]))
    return x

A = np.array([[1, 2, 6, -1], [0, 3, 1, 0], [0, 0, 4, -1], [0, 0, 0 , 2]])
b = np.array([-1, -3, -2, 4])

print(backward(A, b))