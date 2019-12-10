import numpy as np
from timeit import default_timer as timer

EPS = 0.00001


# все прям как у него в лекциях
def Jacobi(A, b):
    N = len(A)
    old_x = [0] * N
    new_x = [0] * N

    condition = True
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
    return old_x


# Решаем уравнение Ax = b
# Тогда:
# x(k+1) = D^(-1) * ( b - R * x(k)), где x(k) -- вектор решения на k-ой итерации,
# D -- главная диагональ матрицы А и R = A - D
def Jacobi_vec(a, b):
    A = np.array(a)
    B = np.array(b)
    N = len(A)
    old_x = np.zeros(N)

    D = np.diag(A)
    R = A - np.diagflat(D)

    condition = True
    while condition:
        new_x = (B - np.dot(R, old_x)) / D
        condition = np.linalg.norm(new_x - old_x) > EPS
        old_x = new_x

    return old_x


def main():
    A = [[10.0, -1.0, 2.0, 0.0],
         [-1.0, 11.0, -1.0, 3.0],
         [2.0, -1.0, 10.0, -1.0],
         [0.0, 3.0, -1.0, 8.0]]
    b = [6.0, 25.0, -11.0, 15.0]

    t = timer()
    x = Jacobi(A, b)
    elapsed = timer() - t
    print("{:.10f} secs elapsed".format(elapsed))
    print(x)
    print()

    t = timer()
    x = Jacobi_vec(A, b)
    elapsed = timer() - t
    print("{:.10f} secs elapsed".format(elapsed))
    print(x)
    print()


main()
