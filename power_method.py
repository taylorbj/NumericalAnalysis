import numpy as np

def power_method(A, x, k):

    for i in range(1, k+1):
        x = np.dot(A, x)
        norm = np.linalg.norm(x, 2)
        x = x / norm
        print("iteration %s: %s"%(i, x))

A = np.array(([-2, 1, 4], [1, 1, 1], [4, 1, -2]))


x0 = np.array([1, 2, -1])
print("x0 = (1, 2, -1)")
power_method(A, x0, 5)

x0 = np.array([1, 2, 1])
print("x0 = (1, 2, 1)")
power_method(A, x0, 5)




