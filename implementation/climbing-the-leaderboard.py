#!/bin/python3

import math
import os
import random
import re
import sys


def find_pos(A, i, l):
    # print('i:{},A:{},l:{}'.format(i, A, l))

    if i >= A[0]:
        return l + 1, i == A[0]
    elif i <= A[len(A) - 1]:
        if i == A[len(A) - 1]:
            return l + len(A), i == A[len(A) - 1]

        return l + len(A) + 1, i == A[len(A) - 1]

    n = len(A)

    mid = n // 2
    mid_element = A[n // 2]

    if i == mid_element:
        return l + mid + 1, True

    left = A[0:mid]
    right = A[mid + 1:]

    if i > mid_element:
        return find_pos(left, i, l)
    elif i < mid_element:
        return find_pos(right, i, l + mid + 1)


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    unique_scores = list(set(scores))
    unique_scores.sort(reverse=True)

    output = []
    cache = {}
    for x in alice:

        if x in cache:
            output.append(cache[x])
            continue

        mid = len(unique_scores) // 2
        mid_element = unique_scores[mid]

        if x < mid_element:
            pos, found = find_pos(unique_scores[mid:], x, mid)
        else:
            pos, found = find_pos(unique_scores, x, 0)

        cache[x] = pos
        unique_scores = unique_scores[0:pos]
        print(pos)


'''
6
100 90 90 80 75 60
5
50 65 77 90 102

'''

if __name__ == '__main__':
    scores_count = 6

    scores = [100, 90, 90, 80, 75, 60]

    alice_count = 5

    alice = [50, 65, 77, 90, 102]

    result = climbingLeaderboard(scores, alice)
