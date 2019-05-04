def fib(N):
    base = [False] * N

    base[0] = 0
    base[1] = 1
    base[2] = 1

    for i in range(3, N):
        base[i] = base[i - 1] + base[i - 2]

    return base


if __name__ == '__main__':
    N = 12
    print(fib(12))
