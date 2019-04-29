#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)
    i = 0
    end = n
    step = 0

    while i < end - 1:

        print('{} - {}  -- {}'.format(i, step, n))

        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1

        step += 1

    return step


if __name__ == '__main__':
    n = 6
    c = [0, 0, 0, 1, 0, 0]

    print(jumpingOnClouds(c))
