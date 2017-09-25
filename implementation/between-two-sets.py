# https://www.hackerrank.com/challenges/between-two-sets

# !/bin/python3

'''

All elements in  are factors of .
 is a factor of all elements in .

'''


def getTotalX(a, b):
    found = []

    for e in range(min(a + b), max(a + b) + 1):

        is_found = False

        for i in a:
            if e % i == 0:
                is_found = True
            else:
                is_found = False
                break

        if is_found is False:
            continue

        for j in b:
            if j % e == 0:
                is_found = True
            else:
                is_found = False
                break

        if is_found is False:
            continue

        found.append(e)

    return len(found)


if __name__ == "__main__":
    n, m = [2, 3]
    a = [2, 4]
    b = [16, 32, 96]
    total = getTotalX(a, b)
    print(total)

    n, m = [1, 1]
    a = [1]
    b = [100]
    total = getTotalX(a, b)
    print(total)
