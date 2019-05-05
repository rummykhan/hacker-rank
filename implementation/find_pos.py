import random
import time
from bisect import *

loops = 0


def find_pos(A, i, l):
    global loops

    loops += 1
    if i >= A[0]:
        return l + 1
    elif i <= A[len(A) - 1]:

        if i == A[len(A) - 1]:
            return l + len(A)

        return l + len(A) + 1

    n = len(A)

    mid = n // 2
    mid_element = A[n // 2]

    if i == mid_element:
        return l + mid + 1

    left = A[0:mid]
    right = A[mid + 1:]

    if i > mid_element:
        return find_pos(left, i, l)
    elif i < mid_element:
        return find_pos(right, i, l + mid + 1)


def find_pos_2(arr, n, x, l):
    # Find indexs of two corners

    lo = (n - 1)
    hi = 0

    # Since array is sorted, an element present
    # in array must be in range defined by corner
    while lo <= hi and x >= arr[lo] and x <= arr[hi]:

        if lo == hi:
            if arr[lo] == x:
                return l + lo
            return -1

        # Probing the position with keeping
        # uniform distribution in mind.
        pos = hi + int(((float(lo - hi) / (arr[lo] - arr[hi])) * (x - arr[hi])))

        print(pos)

        # Condition of target found
        if arr[pos] == x:
            return l + pos

        # If x is larger, x is in upper part
        if arr[pos] < x:
            hi = pos + 1

        # If x is smaller, x is in lower part
        else:
            lo = pos - 1

    return -1


def test_1():
    i = 7

    A = [100, 90, 90, 80, 75, 60]

    unique = list(set(A))
    unique.sort()

    l = len(unique)

    while i != -1:
        x = int(input())

        pos = l - bisect_right(unique, x) + 1

        print('A:{}'.format(A))
        print('A:{} - pos:{}'.format(unique, pos))


def test_2():
    A = [random.randint(1, 1000) for x in range(10000000)]
    A.sort(reverse=True)

    i = 55

    now = time.time()

    pos, found = find_pos(A, i, 0)

    difference = time.time() - now

    print("{} - {}  = {}".format(time.time(), now, difference))

    if found is True:
        found = 'True'
    else:
        found = 'False'

    print('{} - {} - {}'.format(pos, found, difference))


def test_3():
    A = [int(x) for x in
         "295 294 291 287 287 285 285 284 283 279 277 274 274 271 270 268 268 268 264 260 259 258 257 255 252 250 244 241 240 237 236 236 231 227 227 227 226 225 224 223 216 212 200 197 196 194 193 189 188 187 183 182 178 177 173 171 169 165 143 140 137 135 133 130 130 130 128 127 122 120 116 114 113 109 106 103 99 92 85 81 69 68 63 63 63 61 57 51 47 46 38 30 28 25 22 15 14 12 6 4".split(
             ' ')]

    unique_scores = list(set(A))
    unique_scores.sort(reverse=True)

    alice_scores = [
        int(x) for x in
        "5 5 6 14 19 20 23 25 29 29 30 30 32 37 38 38 38 41 41 44 45 45 47 59 59 62 63 65 67 69 70 72 72 76 79 82 83 90 91 92 93 98 98 100 100 102 103 105 106 107 109 112 115 118 118 121 122 122 123 125 125 125 127 128 131 131 133 134 139 140 141 143 144 144 144 144 147 150 152 155 156 160 164 164 165 165 166 168 169 170 171 172 173 174 174 180 184 187 187 188 194 197 197 197 198 201 202 202 207 208 211 212 212 214 217 219 219 220 220 223 225 227 228 229 229 233 235 235 236 242 242 245 246 252 253 253 257 257 260 261 266 266 268 269 271 271 275 276 281 282 283 284 285 287 289 289 295 296 298 300 300 301 304 306 308 309 310 316 318 318 324 326 329 329 329 330 330 332 337 337 341 341 349 351 351 354 356 357 366 369 377 379 380 382 391 391 394 396 396 400".split(
            ' ')
    ]

    expected = []
    with open('answer/climbing.txt') as f:
        lines = f.readlines()
        expected = [
            int(x) for x in lines
        ]

    wrong = 0
    corrent = 0
    i = 0
    for score in alice_scores:
        pos, found = find_pos(unique_scores, score, 0)

        if found is True:
            found = 'True'
        else:
            found = 'False'

        if pos != expected[i]:
            pass
            print('X: {}, {} -- {} - {} -  {}'.format(i, found, score, pos, expected[i]))
            wrong += 1
        else:
            corrent += 1
            pass
            # print('0: {}, {}-- {} - {} -  {}'.format(i, found, score, pos, expected[i]))

        i += 1

    print('C:{}, W:{}'.format(corrent, wrong))


def test_4():
    global loops
    expected = []
    with open('answer/climbing-9-o.txt') as f:
        lines = f.readlines()
        expected = [
            int(x) for x in lines
        ]

    A = []
    with open('question/climbing-9-a.txt') as f:
        line = f.readline()
        A = [
            int(x) for x in line.split(' ')
        ]

    score = []
    with open('question/climbing-9-x.txt') as f:
        line = f.readline()
        score = [
            int(x) for x in line.split(' ')
        ]

    unique = list(set(A))
    unique.sort()

    l = len(unique)

    start = time.time()
    output = []

    for x in score:
        pos = l - bisect_right(unique, x) + 1

        output.append(pos)

    diff = time.time() - start

    print("{}".format(diff))


def test_5():
    x = 80

    A = [100, 90, 90, 80, 75, 60]

    unique = list(set(A))
    unique.sort(reverse=True)

    pos = find_pos_2(unique, len(unique), 80, 0)

    print('A:{}'.format(A))
    print('A:{} - pos:{}'.format(unique, pos))


if __name__ == '__main__':
    # test_1()
    # test_2()
    # test_3()
    test_4()
    # test_5()
