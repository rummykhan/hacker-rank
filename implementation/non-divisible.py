#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    verbose = True
    output = []

    ht = {}

    for a in S:
        rem = a % k

        if rem not in ht:
            ht[rem] = []

        ht[rem].append(a)

    if verbose is True:
        for kx, vx in ht.items():
            if len(vx) < 10:
                print('{} -- {}'.format(kx, vx))
            else:
                print('{} -- {}'.format(kx, len(vx)))

    take = []
    blacklist = []

    #  Special cases
    if len(ht.items()) == 1:

        for ki, vi in ht.items():

            if ki == 0:
                return [1]

            return vi

    # Iterate on hash table
    for ki, vi in ht.items():

        for kj, vj in ht.items():

            if verbose is True:
                print('{} - {} % {} == {}'.format(ki, kj, k, ((ki + kj) % k == 0)))

            if ki == kj:
                continue

            if ki in blacklist or kj in blacklist:
                continue

            if (ki + kj) % k == 0:

                if len(vi) > len(vj):
                    take.append(ki)
                    blacklist.append(kj)
                else:
                    take.append(kj)
                    blacklist.append(ki)
            else:
                take.append(ki)
                take.append(kj)

    for b in blacklist:

        if b in take:
            take[:] = (value for value in take if value != b)

    if k % 2 == 0:
        k_half = k // 2

        if k_half in ht:
            ht[k_half] = [ht[k_half][0]]

        if 0 in ht:
            ht[0] = [ht[0][0]]

    if 0 in take and 0 in ht:
        ht[0] = [ht[0][0]]

    take = list(set(take))
    if verbose is True:
        print('t:{}, b:{}'.format(take, blacklist))

    for t in take:
        output += ht[t]

    return output


def start():
    nk = [10, 4]

    n = int(nk[0])

    k = int(nk[1])

    S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print('S:{}, K:{}'.format(S, k))
    result = nonDivisibleSubset(k, S)

    print(result)


def start_1():
    nk = []
    S = []

    with open('question/non-div.txt') as  f:
        nk = [int(x) for x in f.readline().split(' ')]
        S = [int(x) for x in f.readline().split(' ')]

    n = nk[0]
    k = nk[1]

    result = nonDivisibleSubset(k, S)

    print(len(result))
    print(nk)


if __name__ == '__main__':
    # start()
    start_1()
