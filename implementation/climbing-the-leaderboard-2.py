def find_pos(A, i, l):
    # print('A:{}, i:{}, l:{}'.format(A, i, l))

    if i < A[0]:
        if l == 0:
            return l - 1, True

        return l + 1, False

    elif i == A[0]:

        return l + 1, True

    elif i > A[len(A) - 1]:
        return l + len(A) + 1, False

    elif i == A[len(A) - 1]:
        return l + len(A), True

    n = len(A)

    mid = n // 2
    mid_element = A[n // 2]

    if i == mid_element:
        return l + mid + 1, True

    left = A[0:mid]
    right = A[mid + 1:]

    if i > mid_element:
        return find_pos(right, i, l + mid + 1)
    elif i < mid_element:
        return find_pos(left, i, l)


def climbingLeaderboard(A, alice):
    unique = list(set(A))
    unique.sort()

    output = []
    cache = {}
    l = 0
    for s in alice:

        if s in cache:
            output.append(cache[s])
            continue

        pos, found = find_pos(unique, s, l)

        if pos < 1:
            agg = len(unique) - pos
        elif pos >= len(unique):

            if found is True:
                agg = 1
            else:
                agg = len(unique) + 2 - pos

        else:
            if found is True:
                agg = len(unique) + 1 - pos
            else:
                agg = len(unique) + 2 - pos

        output.append(agg)

    return output


'''
7
100 100 50 40 40 20 10
4
5 25 50 120
'''
if __name__ == '__main__':
    scores_count = 6

    scores = [100, 90, 90, 80, 75, 60]

    alice_count = 5

    alice = [50, 65, 77, 90, 102]

    result = climbingLeaderboard(scores, alice)

    print(result)
