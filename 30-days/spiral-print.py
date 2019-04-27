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
    a = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

    R = 3
    C = 6
    spiralPrint(R, C, a)
    print('')
