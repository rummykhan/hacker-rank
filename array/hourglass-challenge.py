# https://www.hackerrank.com/challenges/2d-array/problem?h_r=next-challenge&h_v=zen

def get_hour_glass(arr, i, j):
    sum = 0
    string = ''
    for k in range(j, j + 3):
        sum += arr[i][k]
        string += '{},'.format(arr[i][k])

    mid = arr[i + 1][j + 1]
    sum += mid
    string += '{},'.format(mid)

    for k in range(j, j + 3):
        sum += arr[i + 2][k]
        string += '{},'.format(arr[i + 2][k])

    # print('glass: {} = {}'.format(string, sum))
    return sum


def hourglassSum(arr):
    sum = None

    for i in range(0, 4):
        for j in range(0, 4):
            hour_glass = get_hour_glass(arr, i, j)

            if sum is None:
                sum = hour_glass

            if hour_glass > sum:
                sum = hour_glass

    return sum


if __name__ == '__main__':
    arr = [
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, - 9, - 9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, - 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
    result = hourglassSum(arr)

    print('Sum: {}'.format(result))
