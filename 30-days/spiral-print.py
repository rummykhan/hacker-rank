# Python3 program to print
# given matrix in spiral form

def rotate(a, r, c):
    A = []

    for i in range(c - 1, -1, -1):
        row = []
        for j in range(1, r):
            row.append(a[j][i])
        A.append(row)

    return A


def spiralPrint(r, c, a):
    while len(a) > 0:

        print(a[0])

        a = rotate(a, r, c)

        if len(a) > 0:
            r = len(a)
            c = len(a[0])


if __name__ == '__main__':
    # Driver Code
    a = [[1, 2, 3]]

    R = 1
    C = 3
    spiralPrint(R, C, a)
    print('')
