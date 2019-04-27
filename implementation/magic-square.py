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


def check_odd_number_positions(s):
    e1 = s[0][1]
    e2 = s[2][1]

    e3 = s[1][0]
    e4 = s[1][2]

    if e1 in [1, 9]:
        e2 = [1, 9] - e1

    if e1 is [2, 7]:
        e2 = [2, 7] - e1

    if e3 in [1, 9]:
        e4 = [1, 9] - e3

    if e3 in [2, 7]:
        e4 = [1, 9] - e3


def check_number_positions(s):
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

    return True, True, True


def apply_fixes(s, fixes, vals, repeat):
    misplaced = [(i + 1) for i, v in enumerate(vals) if v is True]
    repeat = [(index + 1) for index, val in enumerate(repeat) if val > 1]

    print(fixes)
    print(misplaced)
    print(repeat)


def get_cost(s):
    v = False

    while v is not True:
        is_magical = check_sum(s)

        if is_magical is True:
            return 0

        fixes, arr, repeat = check_number_positions(s)

        # mean number are not properly positioned
        if fixes is not True:
            # apply fixes
            s = apply_fixes(s, fixes, arr, repeat)
            break
        else:
            print('Numbers are properly positioned')
            #  numbers are properly positioned
            #  numbers are mis-aligned
            break
            pass


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

s = [[2, 1, 4],[7, 5, 3],[8, 9, 6]]
cost = get_cost(s)
print('COST: {}'.format(cost))

'''

s = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 7]
]
cost = get_cost(s)
print('COST: {}'.format(cost))
print('\r\n================\r\n')
