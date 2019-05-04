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


def get_cost(s):
    cost = 0

    if check_sum(s):
        return 0

    if s[1][1] != 5:
        cost += abs(s[1][1] - 5)
        s[1][1] = 5

    even_rules = {
        4: {'r': 2, 'l': 8, 'o': 6, 'c': 9, 'd': 3},
        6: {'r': 8, 'l': 2, 'o': 4, 'c': 1, 'd': 7},
        8: {'r': 4, 'l': 6, 'o': 2, 'c': 3, 'd': 1},
        2: {'r': 6, 'l': 4, 'o': 8, 'c': 7, 'd': 9},
    }

    rules = even_rules[s[0][0]]

    if s[2][0] != rules['r']:
        cost += abs(s[2][0] - rules['r'])
        s[2][0] = rules['r']

    if s[0][2] != rules['l']:
        cost += abs(s[0][2] - rules['l'])
        s[0][2] = rules['l']

    if s[2][2] != rules['o']:
        cost += abs(s[2][2] - rules['o'])
        s[2][2] = rules['o']

    if s[1][0] != rules['c']:
        cost += abs(s[1][0] - rules['c'])
        s[1][0] = rules['c']

    if s[0][1] != rules['d']:
        cost += abs(s[0][1] - rules['d'])
        s[0][1] = rules['d']

    odd_rules = {
        1: 9,
        7: 3,
        9: 1,
        3: 7
    }

    odd_rule_1 = odd_rules[s[1][0]]
    if s[1][2] != odd_rule_1:
        cost += abs(s[1][2] - odd_rule_1)
        s[1][2] = odd_rule_1

    odd_rule_2 = odd_rules[s[0][1]]
    if s[2][1] != odd_rule_2:
        cost += abs(s[2][1] - odd_rule_1)
        s[2][1] = odd_rule_2

    print(s)

    return cost


'''

4  3  8
9  5  1 
2  7  6
'''

s = [
    [4, 8, 2],
    [4, 5, 7],
    [6, 1, 6]
]
cost = get_cost(s)
print('COST: {}'.format(cost))
print('\r\n================\r\n')
