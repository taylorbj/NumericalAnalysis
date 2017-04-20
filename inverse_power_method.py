import numpy as np
from numpy import linalg as ln

def inverse_power(A, x, theta, k):
    B = A - (theta * np.identity(np.shape(A)[0]))
    for i in range(1, k + 1):
        x = ln.solve(B, x)
        norm = np.linalg.norm(x, 2)
        x = x / norm
        print("iteration %s: %s" % (i, x))

A = np.array(([-2, 1, 4], [1, 1, 1], [4, 1, -2]))
x0 = np.array([1, 2, -1])

theta = 2
print("theta = 2:")
inverse_power(A, x0, theta, 5)

theta = 1
print("theta = 1:")
inverse_power(A, x0, theta, 5)

theta = -5
print("theta = -5:")
inverse_power(A, x0, theta, 5)
