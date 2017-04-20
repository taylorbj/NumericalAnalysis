import numpy as np
from numpy import linalg


def qr_algo(A, iter_count=0):

    n = np.shape(A)[0] - 1
    I = np.identity(n+1)
    tol = 1e-10

    Ak = A

    e_approx = np.zeros(n+1)


    if (n == 0):
        e_approx[n] = Ak[0][0]
        return e_approx, iter_count

    while np.abs(Ak[n, n-1]) > tol:
        shift = Ak[n][n]
        Q, R = linalg.qr(np.subtract(Ak, np.multiply(shift, I)))
        Ak = np.dot(R, Q) + np.multiply(shift, I)
        iter_count += 1


    eval = Ak[n][n]
    Ak = np.delete(Ak, n, 0)
    Ak = np.delete(Ak, n, 1)

    e_approx = [eval, qr_algo(Ak, iter_count+1)]

    return e_approx

