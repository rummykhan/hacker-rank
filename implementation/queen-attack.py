import time


def is_obstacle(c, A):
    return False

    c = int('{}_{}'.format(c[0], c[1]))

    return c in A


def queensAttack(n, k, r_q, c_q, obstacles):
    verbose = True
    if n == 1:
        return 0
    a = 0

    i = r_q
    j = c_q
    obstacle_found = False

    if verbose:
        print('Q:{}'.format([r_q, c_q]))
    start_time = time.time()
    while (i > 1 and j > 1) and obstacle_found is False:
        i -= 1
        j -= 1

        coord = [i, j]

        obstacle_found = is_obstacle(coord, obstacles)

        if obstacle_found:
            break

        a += 1

    if verbose:
        print('A took {}'.format(time.time() - start_time))

    start_time = time.time()
    i = r_q
    j = c_q
    b = 0
    obstacle_found = False
    while (i > 1) and obstacle_found is False:
        i -= 1

        coord = [i, j]
        obstacle_found = is_obstacle(coord, obstacles)

        if obstacle_found:
            break
        b += 1

    if verbose:
        print('B took {}'.format(time.time() - start_time))

    i = r_q
    j = c_q
    c = 0
    obstacle_found = False
    start_time = time.time()
    while (i > 1 and j < n) and obstacle_found is False:
        i -= 1
        j += 1

        coord = [i, j]
        obstacle_found = is_obstacle(coord, obstacles)
        if obstacle_found:
            break
        c += 1

    if verbose:
        print('C took {}'.format(time.time() - start_time))

    i = r_q
    j = c_q
    d = 0
    obstacle_found = False
    start_time = time.time()
    while j > 1 and obstacle_found is False:
        j -= 1

        coord = [i, j]
        obstacle_found = is_obstacle(coord, obstacles)
        if obstacle_found:
            break
        d += 1

    if verbose:
        print('D took {}'.format(time.time() - start_time))

    i = r_q
    j = c_q
    e = 0
    obstacle_found = False
    start_time = time.time()
    while j < n and obstacle_found is False:
        j += 1

        coord = [i, j]
        obstacle_found = is_obstacle(coord, obstacles)
        if obstacle_found:
            break
        e += 1

    if verbose:
        print('E took {}'.format(time.time() - start_time))

    i = r_q
    j = c_q
    f = 0
    obstacle_found = False
    start_time = time.time()
    while i < n and j > 1 and obstacle_found is False:
        i += 1
        j -= 1

        coord = [i, j]
        obstacle_found = is_obstacle(coord, obstacles)
        if obstacle_found:
            break
        f += 1

    if verbose:
        print('F took {}'.format(time.time() - start_time))

    i = r_q
    j = c_q
    g = 0
    obstacle_found = False
    start_time = time.time()
    while i < n and obstacle_found is False:
        i += 1

        coord = [i, j]
        obstacle_found = is_obstacle(coord, obstacles)
        if obstacle_found:
            break
        g += 1

    if verbose:
        print('G took {}'.format(time.time() - start_time))

    i = r_q
    j = c_q
    h = 0
    obstacle_found = False
    start_time = time.time()
    while i < n and j < n and obstacle_found is False:
        i += 1
        j += 1

        coord = [i, j]
        obstacle_found = is_obstacle(coord, obstacles)
        if obstacle_found:
            break
        h += 1

    if verbose:
        print('H took {}'.format(time.time() - start_time))

    if verbose:
        print('a:{}, b:{}, c:{}, d:{}, e:{}, f:{}, g:{}, h:{}'.format(a, b, c, d, e, f, g, h))

    return a + b + c + d + e + f + g + h


def start():
    n = 5
    k = 3
    r_q = 4
    c_q = 3
    obstacles = [
        '5_5',
        '4_2',
        '2_3'
    ]
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print('res: {}'.format(result))


def start_2():
    n = 4
    k = 0
    r_q = 4
    c_q = 4
    obstacles = [
    ]
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print('res: {}'.format(result))


def start_3():
    n = 100000
    k = 100000
    r_q = 6453
    c_q = 3654
    obstacles = [
    ]

    with open('question/queen-attack.txt', 'r')  as f:
        obstacles = [
            int(line.rstrip().replace(' ', '_')) for line in f.readlines()
        ]

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print('res: {}'.format(result))


if __name__ == '__main__':
    # start()
    # start_2()
    start_3()
