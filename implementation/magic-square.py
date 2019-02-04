# https://www.hackerrank.com/challenges/magic-square-forming

# !/bin/python3
# This solution is still incomplete

def is_magical(s):
    arr = [True] * 9

    # center = '1,1'  should be 5

    if s[1][1] is not 5:
        return False

    arr[5 - 1] = False

    edges = ['0,0', '0,2', '2,0', '2,2']  # should be even

    for edge in edges:
        i, j = edge.split(',')
        i = int(i)
        j = int(j)
        if s[i][j] % 2 != 0:
            return False

        arr[s[i][j] - 1] = False

    side_centers = ['0,1', '1,0', '1,2', '2,1']  # should be odd
    for side_center in side_centers:
        i, j = side_center.split(',')
        i = int(i)
        j = int(j)
        if s[i][j] % 2 != 1:
            return False

        arr[s[i][j] - 1] = False

    return True not in arr


def get_cost(s):
    magical = is_magical(s)

    print(magical)


s = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
get_cost(s)

s = [[4, 9, 2], [3, 5, 7], [8, 1, 7]]
get_cost(s)
