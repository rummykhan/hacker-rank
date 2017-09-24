#!/bin/python3

# https://www.hackerrank.com/challenges/time-conversion?h_r=next-challenge&h_v=zen


def timeConversion(s):
    h = int(s[0:2])
    m = s[len(s) - 2:]
    splitted = s[0:len(s) - 2].split(':')

    if m == 'PM':
        if h < 12:
            splitted[0] = str((h + 12) % 24)
    elif m == 'AM' and h == 12:
        splitted[0] = '00'

    return ':'.join(splitted)


s = ['12:05:00AM', '12:00:59PM', '05:59:59AM', '05:59:59PM', '11:59:59AM', '11:59:59PM']
for d in s:
    result = timeConversion(d)
    print(d, result)
