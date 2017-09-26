# https://www.hackerrank.com/challenges/the-birthday-bar

import sys

'''
STATEMENT:

Lily wants to give Ron a piece of chocolate only if it contains 'm' consecutive squares 
whose integers sum to d.

'''


def solve(n, s, d, m):
    result = 0

    for i in range(0, n):

        if sum(s[i:i + m]) == d:
            result += 1

    return result


n = 5
s = [1, 2, 1, 3, 2]
d, m = [3, 2]
result = solve(n, s, d, m)
print(result)

print(' --- ')

n = 1
s = [4]
d, m = [4, 1]
result = solve(n, s, d, m)
print(result)

print(' --- ')
n = 6
s = [1, 1, 1, 1, 1, 1]
d, m = [3, 2]
result = solve(n, s, d, m)
print(result)
