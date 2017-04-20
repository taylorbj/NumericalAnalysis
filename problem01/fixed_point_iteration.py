import math


def fixedp(f, x0, iterations):

    iteration = 0

    for x in range(0, iterations + 1):
        x = f(x0)
        print("iteration %s: %.7s"%(iteration, x0))
        x0 = x
        iteration = iteration + 1



if __name__ == "__main__":

    def func(x):
       return math.log(3*x + 1)

    fixedp(func, 1, 15)

