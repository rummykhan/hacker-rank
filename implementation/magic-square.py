# https://www.hackerrank.com/challenges/magic-square-forming

# !/bin/python3


def is_magical(s):
    ref = 0
    n = len(s)

    # checking horizontal
    for i in range(0, n):

        if ref == 0:
            ref = sum(s[i])
            continue

        if sum(s[i]) != ref:
            return {'d': 'Horizontal', 'i': i}

    # check vertical
    for i in range(0, n):

        if sum([s[0][i], s[1][i], s[2][i]]) != ref:
            return {'d': 'Vertical', 'i': i}

    # check diagonal
    first = 0
    for i in range(0, n):
        first += s[i][i]

    if first != ref:
        return {'d': 'Diagonal', 'i': 1}

    second = 0
    for i in reversed(range(0, n)):
        second += s[n - i - 1][i]

    if second != ref:
        return {'d': 'Diagonal', 'i': 2}

    return True


def get_cost(s):
    cost = 0
    magical = False

    while not magical:
        print(magical)

        magical = is_magical(s)

    return cost


s = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

cost = get_cost(s)

print(cost)
