#!/bin/python3


def solveX(n, p):
    # let's rule out general conditions first
    if n == p or p == 0 or p == 1:
        return 0

    mean = n / 2

    # mean center of the book is greater then
    # the page we need to go
    ref = 0
    if mean >= p:
        k = 0

        while k < p:

            if k == 0:
                k += 1
            else:
                k += 2

            ref += 1

        return ref - 1

    # mean center of the book is less then
    # the page we need to go
    is_even = (n % 2 == 0)

    k = n
    while k > p:
        if is_even and k == n:
            k -= 2
        elif not is_even and k == n:
            k -= 1
        else:
            k -= 2

        ref += 1

    if is_even:
        return ref

    return ref - 1


def solve(n, p):
    print('behavior:{} - {} = {}'.format(n // 2, p // 2, (n // 2 - p // 2)))
    return min(p // 2, n // 2 - p // 2)


n = 5
p = 4
result = solve(n, p)
print(result)
print('---')

n = 4
p = 4
result = solve(n, p)
print(result)

print('---')

n = 7
p = 3
result = solve(n, p)
print(result)

print('---')

n = 6
p = 4
result = solve(n, p)
print(result)
