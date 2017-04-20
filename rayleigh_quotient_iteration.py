import numpy as np
from numpy import linalg as ln

def rayleigh(A, x, k):
    for i in range(1, k + 1):
        theta = np.dot(np.transpose(x), np.dot(A, x)) / np.dot(np.transpose(x), x)
        B = A - (theta * np.identity(np.shape(A)[0]))
        x = ln.solve(B, x)
        norm = np.linalg.norm(x, 2)
        x = x / norm
        print("iteration %s: %s" % (i, x))

A = np.array(([-2, 1, 4], [1, 1, 1], [4, 1, -2]))
x0 = np.array([1, 2, -1])

rayleigh(A, x0, 3)