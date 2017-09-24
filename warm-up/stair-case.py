#!/bin/python3

# https://www.hackerrank.com/challenges/staircase?h_r=next-challenge&h_v=zen


def stair_case(n):
    for i in range(n):
        output = ''

        for j in range(n - 1 - i):
            output += ' '

        for k in range(i + 1):
            output += '#'

        print(output)


n = 6
stair_case(n)
