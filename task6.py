import matplotlib.pyplot as plt

EPS = 0.00001


def Jacobi(A, b):
    N = len(A)
    old_x = [0] * N
    new_x = [0] * N

    condition = True
    t = 0
    while condition:
        for i in range(N):
            new_x[i] = b[i]
            for g in range(N):
                if i != g:
                    new_x[i] -= A[i][g] * old_x[g]
            new_x[i] /= A[i][i]
        norm = abs(old_x[0] - new_x[0])
        for h in range(N):
            if abs(old_x[h] - new_x[h]) > norm:
                norm = abs(old_x[h] - new_x[h])
            old_x[h] = new_x[h]
        condition = norm > EPS
        t = t + 1
    return old_x, t


def Seidel(A, b):
    N = len(A)
    old_x = [0] * N
    new_x = [0] * N

    t = 0
    condition = True
    while condition:
        for i in range(N):
            new_x[i] = b[i]
            for j in range(i):
                new_x[i] -= A[i][j] * new_x[j]
            for j in range(i + 1, N):
                new_x[i] -= A[i][j] * old_x[j]
            new_x[i] /= A[i][i]
        norm = abs(old_x[0] - new_x[0])
        for h in range(N):
            if abs(old_x[h] - new_x[h]) > norm:
                norm = abs(old_x[h] - new_x[h])
            old_x[h] = new_x[h]
        condition = norm > EPS
        t = t + 1
    return old_x, t


def main():
    for n in range(10, 15):
        alpha = 0.0
        A = [[0.0] * n for _ in range(n)]
        b = [0.0] * n

        x1 = [0.0] * 11
        x2 = [0.0] * 11
        y = [0.0] * 11

        t = 0
        while alpha <= 1:
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
            y[t] = alpha
            _, x1[t] = Jacobi(A, b)
            _, x2[t] = Seidel(A, b)
            t = t + 1

            alpha += 0.12

        plt.plot(x1, y, label="Jacobi")
        plt.plot(x2, y, label="Seidel")
        plt.legend(loc='best')
        plt.title("n = {}".format(n))
        plt.xlabel("iterations")
        plt.ylabel("alpha")
        plt.show()

    alpha = 0.0
    while alpha <= 1:
        x1 = [0.0] * 11
        x2 = [0.0] * 11
        y = [0.0] * 11

        t = 0

        for n in range(10, 21):
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
            y[t] = n
            _, x1[t] = Jacobi(A, b)
            _, x2[t] = Seidel(A, b)
            t = t + 1

        plt.plot(x1, y, label="Jacobi")
        plt.plot(x2, y, label="Seidel")
        plt.legend(loc='best')
        plt.title("alpha = {}".format(alpha))
        plt.xlabel("iterations")
        plt.ylabel("n")
        plt.show()
        alpha += 0.25


main()
