def main():
    a = [
        [2, -1, 0, 0, 0],
        [-1, 2, -1, 0, 0],
        [0, -1, 2, -1, 0],
        [0, 0, -1, 2, -1],
        [0, 0, 0, -1, 2]
    ]
    b = [-4 / 25, 2 / 25, 2 / 25, 2 / 25, 2 / 25]
    l, u1, u2 = lu3(a)
    print(lu3_solve(l, u1, u2, b))
    print(lu3_determinant(u1))


# LU-разложение трехдиагональной матрицы
def lu3(a):
    l = [None] * (len(a) - 1)
    u1 = [None] * len(a)
    u2 = [None] * (len(a) - 1)
    for i in range(len(a)):
        if i < len(a) - 1:
            u2[i] = a[i][i + 1]
        if i == 0:
            u1[i] = a[i][i]
        else:
            u1[i] = a[i][i] - l[i - 1] * u2[i - 1]

        if i < len(a) - 1:
            l[i] = a[i + 1][i] / u1[i]
    return l, u1, u2


# находим решения слау Ax=b через LU разложение
# 1) Примем Ux = y и решим Ly = b, т.е. найдем y
# 2) Решим Ux = y
def lu3_solve(l, u1, u2, b):
    y = [None] * len(b)
    x = [None] * len(b)
    for i in range(len(b)):
        y[i] = b[i]
        if i > 0:
            y[i] -= l[i - 1] * y[i - 1]
    for i in range(len(b) - 1, -1, -1):
        x[i] = y[i]
        if i < len(b) - 1:
            x[i] -= u2[i] * x[i + 1]
        x[i] *= 1 / u1[i]
    return x


# вычисляем определитель матрицы через элементы на главной диагонали U матрицы из LU разложения
def lu3_determinant(u1):
    result = 1
    for i in range(len(u1)):
        result *= u1[i]
    return result


main()
