def is_prime(n):
    """Returns True if n is prime."""

    if n == 1:
        return False

    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    count = 0
    while i * i <= n:
        print('{}: {} -- {}'.format(count, i, w))

        if n % i == 0:
            return False

        i += w
        w = 6 - w

        count += 1

    return True


def start():
    T = int(input())

    numbers = []
    for i in range(0, T):
        number = int(input())
        numbers.append(number)

    for number in numbers:

        if is_prime(number):
            print('Prime')
        else:
            print('Not prime')


if __name__ == '__main__':
    start()
