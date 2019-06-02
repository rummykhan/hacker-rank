#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'largestMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def next_row(arr, c_row, c_col, start_from_i, start_from_j):
    rows = cols = len(arr)
    i = c_row + 1

    if i >= rows or c_col + 1 >= cols:
        return False

    for j in range(start_from_j, c_col + 1 + 1):
        if arr[i][j] == 0:
            return False

    return True


def next_col(arr, c_row, c_col, start_from_i, start_from_j):
    rows = cols = len(arr)

    j = c_col + 1

    if c_row + 1 >= rows or j >= cols:
        return False

    for i in range(start_from_i, c_row + 1 + 1):
        if arr[i][j] == 0:
            return False

    return True


def largestMatrix(arr):
    verbose = True
    rows = cols = len(arr)

    best_matrix = 0
    matrix_length = 0

    i = 0
    j = 0

    one_found = False

    actual_i = i
    actual_j = j

    start_from_i = 0
    start_from_j = 0

    while i < rows and j < cols:

        if verbose:
            # print('{},{}'.format(i, j))
            pass

        if arr[i][j] == 0:

            i = actual_i
            j = actual_j

            # increase index
            if j + 1 < cols:
                j += 1
                actual_j = j
            else:
                actual_j = j = 0
                i += 1
                actual_i = i

            start_from_i = i
            start_from_j = j
            continue

        one_found = True

        if next_row(arr, i, j, start_from_i, start_from_j) is True and next_col(arr, i, j, start_from_i,
                                                                                start_from_j) is True:

            i += 1
            j += 1

            matrix_length += 1

            if matrix_length > best_matrix:
                best_matrix = matrix_length
        else:

            i = actual_i
            j = actual_j

            matrix_length = 0

            # increase index
            if j + 1 < cols:
                j += 1
                actual_j += 1
            else:
                actual_j = j = 0
                i += 1
                actual_i += 1

            start_from_i = i
            start_from_j = j

    if best_matrix > 0:
        return best_matrix + 1

    if one_found:
        return 1

    return 0


if __name__ == '__main__':
    arr = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 1],
        [0, 0, 1, 1],
    ]

    result = largestMatrix(arr)

    print(result)
