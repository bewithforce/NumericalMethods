# функция создания единичной матрицы n*n
def identity(n):
    m = [[0 for x in range(n)] for y in range(n)]
    for i in range(0, n):
        m[i][i] = 1
    return m


# основная функция
def LUP(a):
    # инициализируем основные переменные. в С будет храниться LU разложение, а в P матрица перестановок
    n = len(a)
    C = a
    P = identity(n)

    # основной ход алгоритма
    for i in range(0, n):
        pivotValue = 0
        pivot = -1

        # сначала находим наибольшее по модулю число в i-ом столбце
        # искать начинаем с i-ой строки, потому что во всех предыдущих алгоритм уже отработал
        for row in range(i, n):
            if abs(C[row][i]) > pivotValue:
                pivotValue = abs(C[row][i])
                pivot = row
        # если есть хотя бы одно отличное от нуля число, то делаем перестановку
        # если же все числа в столбце равны нулю, то т.к. у нас есть нулевой столбец,
        # то определитель матрицы равен 0 => матрица вырождена и нет LU разложения
        if pivotValue != 0:
            # меняем местами строку с выбранным элементом и строку
            P[pivot], P[i] = P[i], P[pivot]
            C[pivot], C[i] = C[i], C[pivot]
            # само LU разложение
            for j in range(i + 1, n):
                C[j][i] /= C[i][i]
                for k in range(i + 1, n):
                    C[j][k] -= C[j][i] * C[i][k]
        else:
            return
    return P, C


# из матрицы перестановок получаем вектор, в котором
# на i-ом месте стоит номер столбца, в котором
# стоит единица в i-ой строке матрицы перестановок
def get_vector(p):
    vector = []
    for i in range(len(p)):
        for j in range(len(p)):
            if p[i][j]:
                vector.append(j + 1)
                break
    return vector


# достаем L и U матрицы из С
def get_LU(c):
    L = []
    U = []
    for i in range(len(c)):
        L.append([])
        U.append([])
        for j in range(i):
            L[i].append(c[i][j])
            U[i].append(0)
        L[i].append(1)
        U[i].append(c[i][i])
        for j in range(i + 1, len(c)):
            U[i].append(c[i][j])
            L[i].append(0)
    return L, U


# красиво печатаем матрицу
def special_print(a):
    for i in range(len(a)):
        print(a[i])


def main():
    a = [
        [3, 17, 10],
        [2, 4, -2],
        [6, 18, 12]
    ]
    P, C = LUP(a)
    print(get_vector(P))
    L, U = get_LU(a)
    print("\nL:")
    special_print(L)
    print("\nU:")
    special_print(U)


main()
