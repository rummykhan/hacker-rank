# https://www.hackerrank.com/challenges/breaking-best-and-worst-records

# !/bin/python3


def getRecord(s):
    highest = lowest = s[0]

    x = 0
    n = 0

    i = 1

    while i < len(s):

        if s[i] > highest:
            highest = s[i]
            x += 1
        elif s[i] < lowest:
            lowest = s[i]
            n += 1

        i += 1

    return [x, n]


s = [10, 5, 20, 20, 4, 5, 2, 25, 1]
result = getRecord(s)
print(" ".join(map(str, result)))

print('-------')

s = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
result = getRecord(s)
print(" ".join(map(str, result)))

s = [100, 45, 41, 60, 17, 41, 45, 43, 100, 40, 89, 92, 34, 6, 64, 7, 37, 81, 32, 50]
result = getRecord(s)
print(" ".join(map(str, result)))
