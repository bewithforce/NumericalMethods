EPS = 0.00001


# все прям как у него в лекциях
def Seidel(A, b):
    N = len(A)
    old_x = [0] * N
    new_x = [0] * N

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
    return old_x


def main():
    A = [[10.0, -1.0, 2.0, 0.0],
         [-1.0, 11.0, -1.0, 3.0],
         [2.0, -1.0, 10.0, -1.0],
         [0.0, 3.0, -1.0, 8.0]]
    b = [6.0, 25.0, -11.0, 15.0]

    t = timer()
    x = Seidel(A, b)
    elapsed = timer() - t
    print("{:.10f} secs elapsed".format(elapsed))
    print(x)
    print()

    for i in range(2, 5):
        print(i)


main()
