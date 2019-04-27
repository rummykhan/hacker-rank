import time


def sieve_of_atkins(number):
    l1 = [2, 3, 5]

    r = number % 60


def is_prime(number, primes):
    if number <= 1:
        return False

    for i in range(2, (number // 2) + 1):

        if number % i == 0:
            return False

    return True


def start():
    T = int(input())

    numbers = []
    for i in range(0, T):
        number = int(input())
        numbers.append(number)

    primes = []
    for number in numbers:

        s = time.time()

        if is_prime(number, primes):
            interval = time.time() - s
            print('Prime - {}'.format(interval))
            primes.append(number)
        else:
            interval = time.time() - s
            print('Not prime - {}'.format(interval))


if __name__ == '__main__':
    start()
