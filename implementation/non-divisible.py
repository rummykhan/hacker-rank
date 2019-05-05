#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    verbose = True
    ht = {}

    for a in S:
        rem = a % k

        if rem not in ht:
            ht[rem] = []

        ht[rem].append(a)

    if verbose is True:
        print(ht)

    take = []
    blacklist = []

    if len(ht.items()) == 1:
        for ki, vi in ht.items():
            return vi

    for ki, vi in ht.items():
        for kj, vj in ht.items():

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

        if verbose:
            print('b:{}, b in take:{}'.format(b, b in take))

        if b in take:
            take[:] = (value for value in take if value != b)

    take = list(set(take))
    if verbose is True:
        print('t:{}, b:{}'.format(take, blacklist))

    output = []
    for t in take:
        output += ht[t]

    return output


if __name__ == '__main__':
    nk = [4, 3]
    nk = [15, 7]
    nk = [5, 5]
    nk = [10, 5]
    nk = [5, 1]

    n = int(nk[0])

    k = int(nk[1])

    S = [1, 7, 2, 4, 5, 6, 10, 8]
    S = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
    S = [2, 7, 12, 17, 22]
    S = [770528134, 663501748, 384261537, 800309024, 103668401, 538539662, 385488901, 101262949, 557792122, 46058493]
    S = [1, 2, 3, 4, 5]

    result = nonDivisibleSubset(k, S)

    print(result)
