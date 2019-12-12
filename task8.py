import numpy as np
import random
import matplotlib.pyplot as plt

tol = 0.0001
it_max = 10000


def Create(n):
    A = [[1 / (i + j + 1) for j in range(n)] for i in range(n)]
    b = [sum(A[i]) for i in range(n)]
    return A, b


def cg(A, b):
    it = 0
    x = 0
    r = np.copy(b)
    r_prev = np.copy(b)
    rho = np.dot(r, r)
    p = np.copy(r)
    while np.sqrt(rho) > tol * np.sqrt(np.dot(b, b)) and it < it_max:
        it += 1
        if it == 1:
            p[:] = r[:]
        else:
            beta = np.dot(r, r) / np.dot(r_prev, r_prev)
            p = r + beta * p
            w = np.dot(A, p)
            alpha = np.dot(r, r) / np.dot(p, w)
            x = x + alpha * p
            r_prev[:] = r[:]
            r = r - alpha * w
            rho = np.dot(r, r)

    return x, it


def main():
    n = [random.randint(5, 35) for _ in range(15)]
    n.sort()
    x = [[0.0] * n[i] for i in range(15)]
    iterations = [0] * 15
    for i in range(15):
        A, b = Create(n[i])
        x[i], iterations[i] = cg(A, b)
        print("n = {}".format(n[i]))
        print(x[i])
        print()
    plt.plot(iterations, n)
    plt.title("Conjugate gradient method")
    plt.xlabel("iterations")
    plt.ylabel("n")
    plt.show()


main()
