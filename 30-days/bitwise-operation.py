#!/bin/python3

import math
import os
import random
import re
import sys
import time


def start_2(n, k):
    best_match = None

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):

            v = i & j

            if v == (k - 1):
                return v

            if int(v) >= k:
                continue

            if best_match is None:
                best_match = v
                continue

            if v > best_match:
                best_match = v

    return best_match


def start_3(n, k):
    best_match = None

    start = 1
    if k > 2:
        start = k - 2

    for i in range(start, n):
        for j in range(i + 1, n + 1):

            v = i & j

            if v == (k - 1):
                return v

            if v >= k:
                continue

            if best_match is None:
                best_match = v
                continue

            if v > best_match:
                best_match = v

    return best_match


def start_4(n, k):
    if k - 1 | k <= n:
        return k - 1
    else:
        return k - 2


def start_5(n, k):
    c = k - 3 & k - 2
    a = k - 2 & k - 1
    b = k - 1 & k
    d = k & k + 1

    print('{} - {} - {} -  {}'.format(a, b, c,  d))


def start_file():
    path = 'bitwise/bitwise.txt'
    result_path = 'bitwise/result.txt'

    data = []
    data_result = []
    with open(path, 'r') as file:
        data = file.readlines()

    with open(result_path, 'r') as file:
        data_result = file.readlines()

    lines = []
    for line in data:
        line = line.replace('\n', '')
        lines.append(line)

    results = []
    for line in data_result:
        line = line.replace('\n', '')
        results.append(line)

    total_start = time.time()
    for i in range(0, len(lines)):
        n, k = lines[i].split(' ')
        result = int(results[i])

        time_start = time.time()
        c_result = start_4(int(n), int(k))

        if c_result != result:
            print('n:{}, k:{} -- E:{}, G:{}'.format(n, k, result, c_result))
        else:
            # print('Passed! n:{}, k:{} -- E:{}, G:{}'.format(n, k, result, c_result))
            pass

    print('Total time took: {} seconds'.format(time.time() - total_start))


if __name__ == '__main__':
    # hr()
    # start_file()
    # print(start_3(2, 2))
    # start_2(178, 104)
    start_5(955, 236)
