#!/bin/python3

import sys

#https://www.hackerrank.com/challenges/diagonal-difference

'''
n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
'''

n = 4
a = [[1, 2, 3, 4], [3, 2, 1, 5], [2, 4, 6, 9], [2, 8, 9, 15]]

first = 0
second = 0
for i in range(0, n):
    first += a[i][i]

for i in reversed(range(n)):
    second += a[n - i - 1][i]

print(abs(first-second))