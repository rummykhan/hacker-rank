#!/bin/python3

import sys

if __name__ == '__main__':
    n = 3
    a = [1, 2, 3]

    totalSwaps = 0
    for i in range(0, n):
        # Track number of elements swapped during a single array traversal

        numberOfSwaps = 0

        for j in range(0, n - 1):

            # Swap adjacent elements if they are in decreasing order
            if a[j] > a[j + 1]:
                x = a[j]
                y = a[j + 1]

                # swap
                a[j] = y
                a[j + 1] = x

                numberOfSwaps += 1

        totalSwaps += numberOfSwaps

        # If no elements were swapped during a traversal, array is sorted
        if numberOfSwaps == 0:
            break

    print("Array is sorted in {} swaps.".format(totalSwaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a) - 1]))
