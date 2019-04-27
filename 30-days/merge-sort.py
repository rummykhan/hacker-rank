import math


def merge_sort(arr):
    if len(arr) > 1:
        left_half = len(arr) // 2

        L = arr[:left_half]
        R = arr[left_half:]

        merge_sort(L)
        merge_sort(R)

        print("{} -- {}".format(L, R))

        i = j = k = 0

        while i < len(L) and j < len(R):

            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1

            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    print(arr)


if __name__ == '__main__':
    arr = [9, 5, 3, 1, 7, 3, 4, 2]

    merge_sort(arr)
