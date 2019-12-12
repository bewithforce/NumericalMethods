import matplotlib.pyplot as plt
import random

EPS = 0.00001


def OverRelaxation(A, b, omega):
    N = len(A)
    old_x = [0] * N
    new_x = [0] * N

    condition = True
    t = 0
    while condition:
        for i in range(N):
            new_x[i] = b[i]
            for j in range(i):
                new_x[i] -= A[i][j] * new_x[j]
            for j in range(i + 1, N):
                new_x[i] -= A[i][j] * old_x[j]
            new_x[i] *= omega / A[i][i]
            new_x[i] += (1 - omega) * old_x[i]
        norm = abs(old_x[0] - new_x[0])
        for h in range(N):
            if abs(old_x[h] - new_x[h]) > norm:
                norm = abs(old_x[h] - new_x[h])
            old_x[h] = new_x[h]
        condition = norm > EPS
        t = t + 1
    return old_x, t


def Create(n, alpha):
    A = [[0.0] * n for _ in range(n)]
    b = [0.0] * n
    for i in range(0, n):
        A[i][i] = 2
        if i != n - 1:
            A[i][i + 1] = -1 - alpha
        else:
            b[i] = 1 + alpha

        if i != 0:
            A[i][i - 1] = -1 + alpha
        else:
            b[i] = 1 - alpha
    return A, b


def testing():
    for i in range(5):
        n = random.randint(5, 35)
        alpha = random.random()
        A, b = Create(n, alpha)
        x = [[0.0] * n for _ in range(15)]
        iterations = [0] * 15
        omega = [random.uniform(1.1, 2) for _ in range(15)]
        omega.sort()
        for j in range(15):
            x[j], iterations[j] = OverRelaxation(A, b, omega[j])
            print(x[j])
        plt.plot(iterations, omega)
        plt.title("n = {}, alpha = {}".format(n, alpha))
        plt.xlabel("iterations")
        plt.ylabel("omega")
        plt.show()


testing()
