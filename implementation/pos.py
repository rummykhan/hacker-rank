import time


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


def start():
    x = [5, 10, 15, 20, 25, 40, 45, 50, 55, 100, 120]
    # x = [55]

    A = [100, 100, 50, 40, 40, 20, 10]

    unique = list(set(A))
    unique.sort(reverse=True)

    output = []
    l = len(unique)


    for s in x:

        while l > 0 and unique[l - 1] <= s:
            l -= 1

        output.append(l+1)



'''
7
100 100 50 40 40 20 10
4
5 25 50 120
'''


def test_4():
    expected = []
    with open('answer/climbing-9-o.txt') as f:
        lines = f.readlines()
        expected = [
            int(x) for x in lines
        ]

    A = []
    with open('question/climbing-9-a.txt') as f:
        line = f.readline()
        A = [
            int(x) for x in line.split(' ')
        ]

    score = []
    with open('question/climbing-9-x.txt') as f:
        line = f.readline()
        score = [
            int(x) for x in line.split(' ')
        ]

    unique = list(set(A))
    unique.sort()

    main = unique
    start = time.time()
    output = []

    output_table = {}

    C = 0
    W = 0
    i = 0
    for x in score:

        if x in output_table:
            output.append(output_table[x])
            i += 1
            continue

        pos, found = find_pos(main, x, 0)

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

        if agg == expected[i]:
            C += 1
        else:
            W += 1

        output_table[x] = agg

        output.append(agg)

        i += 1

    diff = time.time() - start

    print("{} - C:{}, W:{}".format(diff, C, W))


if __name__ == '__main__':
    start()
    # test_4()
