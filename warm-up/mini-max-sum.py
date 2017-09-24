# https://www.hackerrank.com/challenges/mini-max-sum


arr = [1, 2, 3, 9, 5]

mini = sum(sorted(arr)[0:len(arr) - 1])
max = sum(sorted(arr, reverse=True)[0:len(arr) - 1])

print('{} {}'.format(mini, max))
