import numpy as np

def lu_factorization(A) :
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        L[j, j] = 1.0
        for i in range(j + 1):
            U[i, j] = A[i, j] - np.sum(L[i, k] * U[k, j] for k in range(i))
            if np.abs(U[j, j]) < np.power(10, -8):
                print("Error")
                return
        for i in range(j, n):
            L[i, j] = (A[i, j] - np.sum(L[i, k] * U[k, j] for k in range(j))) / U[j, j]

    L = np.around(L, 3)
    U = np.around(U, 3)
    return np.array([L, U])



A = np.array([[6, 2, 1, -1], [2, 4, 1, 0], [1, 1, 4, -1], [-1, 0, -1, 3]])
print(lu_factorization(A))
