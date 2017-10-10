# https://www.hackerrank.com/challenges/bon-appetit

# !/bin/python3

import sys


def bonAppetit(n, k, b, ar):

    del ar[k]

    equal = int(sum(ar) / 2)

    if equal == b:
        return 'Bon Appetit'

    return b - equal


n, k = [4, 1]
ar = [3, 10, 2, 9]
b = 12
result = bonAppetit(n, k, b, ar)
print(result)

n, k = [4, 1]
ar = [3, 10, 2, 9]
b = 7
result = bonAppetit(n, k, b, ar)
print(result)
