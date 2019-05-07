def is_closer(a, b, c, key):
    dx1 = (b[0] - a[0]) ** 2
    dy1 = (b[1] - a[1]) ** 2

    dx2 = (c[0] - a[0]) ** 2
    dy2 = (c[1] - a[1]) ** 2

    return dx1 + dy1 < dx2 + dy2


def is_in_line(a, b, c):
    if a[0] == b[0] and a[1] == b[1]:
        return False

    ax = c[0] - a[0]
    ay = c[1] - a[1]

    cx = b[0] - a[0]
    cy = b[1] - a[1]

    cross = (ax * cy) - (ay * cx)

    if cross != 0:
        return False

    if abs(cx) >= abs(cy):
        if cx > 0:
            return a[0] <= c[0] and c[0] <= b[0]
        else:
            return b[0] <= c[0] and c[0] <= a[0]

    if cy > 0:
        return a[1] <= c[1] and c[1] <= b[1]

    return b[1] <= c[1] and c[1] <= a[1]


def get_ht(n, k, r_q, c_q, obstacles):
    a_min = min([abs(1 - r_q), abs(1 - c_q)])
    c_min = min([abs(1 - r_q), abs(n - c_q)])

    f_min = min([abs(n - r_q), abs(1 - c_q)])
    h_min = min([abs(n - r_q), abs(n - c_q)])

    a_start = [r_q - a_min, c_q - a_min]
    b_start = [1, c_q]
    c_start = [r_q - c_min, c_q + c_min]
    d_start = [r_q, 1]
    e_start = [r_q, n]
    f_start = [r_q + f_min, c_q - f_min]
    g_start = [n, c_q]
    h_start = [r_q + h_min, c_q + h_min]

    ht = {
        'a': a_start,
        'b': b_start,
        'c': c_start,
        'd': d_start,
        'e': e_start,
        'f': f_start,
        'g': g_start,
        'h': h_start
    }
    queen = [r_q, c_q]

    for obstacle in obstacles:

        key = None
        dist = obstacle

        if is_in_line(a_start, queen, obstacle):
            key = 'a'
            dist = [obstacle[0] + 1, obstacle[1] + 1]

        if is_in_line(b_start, queen, obstacle):
            key = 'b'
            dist = [obstacle[0] + 1, obstacle[1]]

        if is_in_line(queen, c_start, obstacle):
            key = 'c'
            dist = [obstacle[0] + 1, obstacle[1] - 1]

        if is_in_line(d_start, queen, obstacle):
            key = 'd'
            dist = [obstacle[0], obstacle[1] + 1]

        if is_in_line(queen, e_start, obstacle):
            key = 'e'
            dist = [obstacle[0], obstacle[1] - 1]

        if is_in_line(queen, f_start, obstacle):
            key = 'f'
            dist = [obstacle[0] - 1, obstacle[1] + 1]

        if is_in_line(queen, g_start, obstacle):
            key = 'g'
            dist = [obstacle[0] - 1, obstacle[1]]

        if is_in_line(queen, h_start, obstacle):
            key = 'h'
            dist = [obstacle[0] - 1, obstacle[1] - 1]

        if key is None:
            continue

        best_p = ht[key]

        if is_closer(queen, best_p, obstacle, key):
            ht[key] = best_p
        else:
            ht[key] = dist

    return ht


def queensAttack(n, k, r_q, c_q, obstacles):
    if n == 1:
        return 0

    verbose = True

    ht = get_ht(n, k, r_q, c_q, obstacles)

    if verbose:
        for k, v in ht.items():
            print('{} - {}'.format(k, v))

    a = abs(ht['a'][0] - r_q)
    b = abs(ht['b'][0] - r_q)
    c = abs(ht['c'][0] - r_q)
    d = abs(ht['d'][1] - c_q)
    e = abs(ht['e'][1] - c_q)
    f = abs(ht['f'][0] - r_q)
    g = abs(ht['g'][0] - r_q)
    h = abs(ht['h'][0] - r_q)

    return a + b + c + d + e + f + g + h


def start():
    n = 5
    k = 3
    r_q = 4
    c_q = 3
    obstacles = [
        [5, 5],
        [4, 2],
        [2, 3],
    ]
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)


def test_1():
    p1 = [1, 1]
    p2 = [1, 100000]
    p3 = [1, 201]

    p4 = [1, 1]

    in_line = is_in_line(p1, p2, p3)

    print(str(in_line))

    if in_line:
        in_line = ' In Line'
    else:
        in_line = ' Not In Line'

    print('p1:{} - p2:{} - p3:{}  -- {}'.format(p1, p2, p3, in_line))


def start_2():
    n = 4
    k = 0
    r_q = 4
    c_q = 1
    obstacles = [
        [2, 3]
    ]
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)


def start_3():
    n = 100000
    k = 100000
    r_q = 1
    c_q = 1
    obstacles = []

    with open('question/queen-attack.txt') as f:
        obstacles = [list(map(int, x.rstrip().split())) for x in f.readlines()]

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)


if __name__ == '__main__':
    # start()
    # start_2()
    start_3()
    # test_1()
