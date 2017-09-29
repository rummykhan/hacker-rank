#!/bin/python3


# https://www.hackerrank.com/challenges/migratory-birds

def migratoryBirds(n, ar):
    import operator
    results = {}

    for i in ar:

        try:
            results[i] += 1
            continue
        except:
            results[i] = 1
            continue

    k, v = sorted(results.items(), key=operator.itemgetter(1), reverse=True)[0]

    return k


n = 6
ar = [1, 4, 4, 4, 5, 5, 3]
result = migratoryBirds(n, ar)
print(result)
