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

    d1 = s[0][0] + s[1][1] + s[2][2]
    d2 = s[0][2] + s[1][1] + s[2][0]

    return x1 == x2 and x2 == x3 and x3 == y1 and y1 == y2 and y2 == y3 and y3 == d1 and d1 == d2 and d2 == 15


def check_cost(s, r):
    cost = 0
    for index, i in enumerate(s):
        for index2, j in enumerate(i):
            cost += abs(s[index][index2] - r[index][index2])

    return cost


def formingMagicSquare(s):
    cost = 0

    if check_sum(s):
        return 0

    pre = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    best_cost = None
    for i in pre:
        cost = check_cost(s, i)

        if best_cost is None or cost < best_cost:
            best_cost = cost

    return best_cost


'''

4 9 2
3 5 7
8 1 5
'''

s = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 5]
]
cost = formingMagicSquare(s)
print('COST: {}'.format(cost))
