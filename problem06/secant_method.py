
def secant(f, x0, x1, iterations):

    iteration = 0

    for x in range(0, iterations + 1):
        x2 = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
        print("iteration %s: %.8s"%(iteration, x2))
        x0 = x1
        x1 = x2
        iteration = iteration + 1

def f(x):

    return x*x*x - 3*x*x + 3

secant(f, 1, 2, 10)
