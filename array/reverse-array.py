# https://www.hackerrank.com/challenges/arrays-ds/problem



def reverseArray(a):
    output = []
    for i in reversed(range(0, len(a))):
        output.append(a[i])

    return output


if __name__ == '__main__':
    arr = [1, 2, 4, 3]
    arr = reverseArray(arr)
