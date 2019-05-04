count = 0


def num_ways(i, N):
    global count

    if i > N:
        return

    if i == 4:
        count += 1

    if i + 1 <= 4:
        num_ways(i + 1, N)

    if i + 2 <= 4:
        num_ways(i + 2, N)


if __name__ == '__main__':
    N = 4
    num_ways(0, N)

    print('{} '.format(count))
