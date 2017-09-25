# https://www.hackerrank.com/challenges/kangaroo

# !/bin/python3


'''

Explanation:

 S = vt + (already completed distance)

 S1 = v1*t + x1
 S2 = v2*t + x2

 We didn't assign t a number because this is not known

 and we want to find out after how much time then can meet togather.

 v1*t + x1 = v2*t + x2

 v1*t - v2*t = x2 - x1

 t (v1-v2) = x2 - x1

 t = x2 - x1 /  v1 - v2

 It is 100 % sure if the speed of v2 is not greater then v1 they will meet.

 if t is positive value, its sure they will meet.

 if t is negative mean they can meet but they have to run backward.

'''


def kangaroo(x1, v1, x2, v2):
    if v2 > v1:
        return 'NO'

    if x1 < x2 and v1 == v2:
        return 'NO'

    if (x2 - x1) % (v1 - v2) == 0:
        return 'YES'

    return 'NO'


x1, v1, x2, v2 = [0, 3, 4, 2]
result = kangaroo(x1, v1, x2, v2)
print(result)

x1, v1, x2, v2 = [0, 2, 5, 3]
result = kangaroo(x1, v1, x2, v2)
print(result)

x1, v1, x2, v2 = [43, 2, 70, 2]
result = kangaroo(x1, v1, x2, v2)

print(result)
