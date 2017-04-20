import math

def newton(f, deriv, x0, iterations) :

    iteration = 0

    for x in range(0, iterations + 1):
        x1 = x0 - (f(x0)/deriv(x0))
        print("iteration %s: %.8s"%(iteration, x0))
        x0 = x1
        iteration += 1

def f(x):

    return x*x - 3*x* + 3

def deriv(x):

    return 3*x*x - 6*x

#newton(f, deriv, 1.5, 5)
newton(f, deriv, 2.1, 5)

