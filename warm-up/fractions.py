#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/plus-minus

'''
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
'''

n = 6
arr = [-4, 3, -9, 0, 4, 1]

positive = []
negative = []
zeros = []

for i in arr:
    if i > 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)
    else:
        zeros.append(i)

total = len(positive) + len(negative) + len(zeros)

print(float(len(positive)) / float(total))
print(float(len(negative)) / float(total))
print(float(len(zeros)) / float(total))
