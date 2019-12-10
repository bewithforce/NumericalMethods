from math import sqrt


# вычисление определителя из рахложения Холецкого
def Cholesky_determinant(g):
    result = 1.0
    for i in range(len(g)):
        result *= g[i][i]
    return result


# основная функция
def Cholesky(a):
    # инициализируем основные переменные
    n = len(a)
    G = [[0.0 for _ in range(n)] for _ in range(n)]

    # все
    for i in range(len(a)):
        for j in range(i + 1):
            subtrahend = 0
            for k in range(j):
                subtrahend += G[i][k] * G[j][k]
            if i == j:
                G[i][j] = sqrt(a[i][i] - subtrahend)
            else:
                (1.0 / G[j][j] * (a[i][j] - subtrahend))

    return G


# красиво печатаем матрицу
def special_print(a):
    for i in range(len(a)):
        print(a[i])


def main():
    a = [
        [1, 1 / 2, 1 / 3, 1 / 4],
        [1 / 2, 1 / 3, 1 / 4, 1 / 5],
        [1 / 3, 1 / 4, 1 / 5, 1 / 6],
        [1 / 4, 1 / 5, 1 / 6, 1 / 7]
    ]
    G = Cholesky(a)
    special_print(G)
    print(Cholesky_determinant(G) ** 2)


main()
