#!/bin/python3

# https://www.hackerrank.com/challenges/apple-and-orange?h_r=next-challenge&h_v=zen

s, t = [7, 11]  # house area
a, b = [5, 15]  # position of apple tree and orange tree
m, n = [5, 4]  # apple = 3 (fell), orange (2)
apple = [2, 2, 1, 3, 15]  # distance from apple tree on x-axis
orange = [-25, -4, -3, 4]  # distance from orange tree on x-axis

apples = 0
oranges = 0

for i in range(0, m):
    if a + apple[i] >= s and a + apple[i] <= t:
        apples += 1

for j in range(0, n):
    if b + orange[j] >= s and b + orange[j] <= t:
        oranges += 1

print(apples)
print(oranges)
