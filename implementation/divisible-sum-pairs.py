# https://www.hackerrank.com/challenges/divisible-sum-pairs?h_r=next-challenge&h_v=zen

# !/bin/python3


def divisibleSumPairs(n, k, ar):
    results = 0
    for i in range(n):

        for j in range(n):

            if i >= j:
                continue

            if (ar[i] + ar[j]) % k == 0:
                results += 1

    return results


n, k = [6, 3]
ar = [1, 3, 2, 6, 1, 2]
result = divisibleSumPairs(n, k, ar)
print(result)
