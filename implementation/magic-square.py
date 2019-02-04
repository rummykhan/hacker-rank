# https://www.hackerrank.com/challenges/magic-square-forming

# !/bin/python3
# This solution is still incomplete

def check_sum(s):
    x1 = s[0][0] + s[0][1] + s[0][2]
    x2 = s[1][0] + s[1][1] + s[1][2]
    x3 = s[2][0] + s[2][1] + s[2][2]

    y1 = s[0][0] + s[1][0] + s[2][0]
    y2 = s[0][1] + s[1][1] + s[2][1]
    y3 = s[0][2] + s[1][2] + s[2][2]

    return x1 == x2 and x2 == x3 and x3 == y1 and y1 == y2 and y2 == y3


def is_magical(s):
    arr = [True] * 9
    fixes = []
    repeat = [0] * 9

    # center = '1,1'  should be 5
    # edge should be even numbers
    # center sides should be odd numbers

    for i in range(0, 3):
        for j in range(0, 3):

            repeat[s[i][j] - 1] += 1

            if i is 1 and j is 1 and s[i][j] is not 5:
                fixes.append([1, 1, s[1][1]])
                continue
            elif i is 1 and j is 1 and s[i][j] is 5:
                arr[s[i][j] - 1] = False
                continue

            if s[i][j] % 2 != ((i + j) % 2):
                fixes.append([i, j, s[i][j]])
                continue

            arr[s[i][j] - 1] = False

    if len(fixes) > 0:
        return fixes, arr, repeat

    magical = check_sum(s)

    return fixes, magical, magical


def apply_fixes(s, fixes, vals, repeat):
    misplaced = [(i + 1) for i, v in enumerate(vals) if v is True]
    repeat = [(index + 1) for index, val in enumerate(repeat) if val > 1]

    print(fixes)
    print(misplaced)
    print(repeat)


def get_cost(s):
    v = False

    while v is not True:
        fixes, v, repeat = is_magical(s)

        if v is True:
            return 0

        if v is False:
            print(fixes)
            break

        s = apply_fixes(s, fixes, v, repeat)
        break


'''
s = [[4, 9, 2], [3, 5, 7], [8, 1, 7]]
cost = get_cost(s)
print('COST: {}'.format(cost))
print('\r\n================\r\n')

s = [[4, 9, 2], [4, 5, 7], [8, 1, 7]]
cost = get_cost(s)
print('COST: {}'.format(cost))
print('\r\n================\r\n')

s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
cost = get_cost(s)
print('COST: {}'.format(cost))
print('\r\n================\r\n')
'''

s = [
    [2, 1, 4],
    [7, 5, 3],
    [8, 9, 6]
]
cost = get_cost(s)
print('COST: {}'.format(cost))

s = [
    [8, 1, 4],
    [7, 5, 3],
    [2, 9, 6]
]

s = [
    [8, 1, 6],
    [7, 5, 3],
    [2, 9, 4]
]

s = [
    [8, 1, 6],
    [3, 5, 7],
    [2, 9, 4]
]

s = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]
