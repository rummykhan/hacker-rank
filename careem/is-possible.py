#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isPossible' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#  4. INTEGER d
#

def isPossible(a, b, c, d):
    verbose = True
    vector_a = a + b
    vector_b = c + d

    # check the base case
    # if it's possible with  first step

    if (a + b) == c and b == d:
        return 'Yes'

    if a == c and b + a == d:
        return 'Yes'

    if (a + b) > c or (a + b) > d:
        return 'No'

    actual_a = a
    actual_b = b

    # match x-axis with target
    # goto target y
    while a <= c:
        if a + b <= c:
            a += b
            print('case1: {}-{}'.format(a, b))
            continue

        break

    if verbose:
        print('{} - {} = {}'.format(c, a, c - a))
    if d - b != 0 and (d - b) % a == 0:
        if verbose:
            print(' {} - {}  % {} == {}'.format(c, a, b, (c - a) % b))
        return 'Yes'

        # match y-axis with target
        # goto target x

    a = actual_a
    b = actual_b
    while b <= d:
        if b + a <= d:
            b += a
            if verbose:
                print('case2: {}-{}'.format(a, b))
            continue
        break

    if verbose:
        print('{} - {} = {}'.format(d, b, d - b))
    if c - a != 0 and (c - a) % b == 0:
        if verbose:
            print(' {} - {}  % {} == {}'.format(d, b, a, (d - b) % a))
        return 'Yes'

    return 'No'


if __name__ == '__main__':
    a = 1
    b = 4
    c = 5
    d = 9
    data = isPossible(a, b, c, d)

    print(data)
