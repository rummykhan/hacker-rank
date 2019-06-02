# Array Subset


def get_sum_2(arr, n):
    pass


def get_sum(arr):
    total = 0

    for i in range(0, len(arr) + 1):
        for j in range(i, len(arr)):
            total += sum(arr[i:j + 1])

    return total


if __name__ == '__main__':
    arr = [1, 2, 3]
    # total = get_sum(arr)
