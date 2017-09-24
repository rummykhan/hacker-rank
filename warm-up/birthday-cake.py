# https://www.hackerrank.com/challenges/birthday-cake-candles

# !/bin/python3

import sys


def birthdayCakeCandles(n, ar):
    tallest = [0]
    for i in ar:

        if i == tallest[0]:
            tallest.append(i)
        elif i > tallest[0]:
            tallest = [i]
    return len(tallest)


n = 10
ar = [1, 2, 9, 9, 17, 17, 45, 90, 176, 176, 176]
result = birthdayCakeCandles(n, ar)
print(result)
