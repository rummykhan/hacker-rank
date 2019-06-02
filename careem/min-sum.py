MAX_VALUE = 5001


def getMinimumUniqueSum(arr):
    unique = set()
    for a in arr:
        for x in range(a, MAX_VALUE):
            if x not in unique:
                break
        unique.add(x)
    return sum(unique)


if __name__ == '__main__':
    arr = [1, 2, 2, 2, 5, 6]

    result = getMinimumUniqueSum(arr)

    print(result)
