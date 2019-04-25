#!/bin/python3

import math
import os
import random
import re
import sys

'''

5 / 2 = 1

2 / 2 = 0

1

'''


def get_bin(n):
    binary = []

    while n > 1:
        bit = n % 2

        binary.append(bit)

        n = n // 2

    binary.append(n)

    return binary


def consecutive_one(binary):
    best_ones = 0
    session_ones = 0

    for item in binary:

        if item == 1:
            session_ones += 1
        else:
            session_ones = 0

        if session_ones > best_ones:
            best_ones = session_ones

    return best_ones


if __name__ == '__main__':
    n = int(input())

    binary = get_bin(n)

    print(binary)

    ones = consecutive_one(binary)

    print(ones)
