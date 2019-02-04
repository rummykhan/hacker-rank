#!/bin/python3

import sys

#https://www.hackerrank.com/challenges/electronics-shop/problem


def getMoneySpent(keyboards, drives, s):
    keyboards = sorted(keyboards, reverse=True)
    drives = sorted(drives, reverse=True)

    min = -1
    for i in range(0, len(keyboards)):
        for j in range(0, len(drives)):
            sum = keyboards[i] + drives[j]

            if sum <= s and sum > min:
                min = sum

    return min


s, n, m = '10 2 3'.split(' ')
s, n, m = [int(s), int(n), int(m)]

keyboards = list(map(int, '3 1'.strip().split(' ')))
drives = list(map(int, '5 2 8'.strip().split(' ')))

moneySpent = getMoneySpent(keyboards, drives, s)

print(moneySpent)
