import math


def bisection(f, a, b, iterations):
    for x in range(0, iterations + 1):
        c = (a + b) / 2.0
        print("iteration %s: %s %s"%(x, c, f(c)))
        if f(c)*f(b) > 0:
            b = c
        else:
            a = c



if __name__ == "__main__":

    def func(x):
        return (x-2)*(x-2) - math.log(x)#math.exp(x) - 3*x - 1

    bisection(func, 1, 2, 5)



