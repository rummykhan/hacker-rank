# https://www.hackerrank.com/challenges/counting-valleys/problem


# !/bin/python3

import sys


def countingValleys(n, s):
    # Complete this function

    valleys = 0
    below_sea_level = 0
    above_sea_level = 0
    sea_level = True

    for c in list(s):

        if sea_level:

            if c == 'D' and above_sea_level == 0:
                sea_level = False
                below_sea_level -= 1
                print('A:[ {} ], asl: {}, bsl:{}, valleys: {}'.format(c, above_sea_level, below_sea_level, valleys))
                print('continue')
                continue

            if c == 'U':
                above_sea_level += 1
            else:
                above_sea_level -= 1

            if above_sea_level == 0:
                sea_level = False
                print('B:[ {} ], asl: {},  bsl:{}, valleys: {}'.format(c, above_sea_level,below_sea_level, valleys))
                print('continue')
                continue

        if not sea_level:

            if c == 'U' and below_sea_level == 0:
                sea_level = True
                above_sea_level += 1
                print('C:[ {} ], asl: {}, bsl:{}, valleys:{}'.format(c, above_sea_level,below_sea_level, valleys))
                print('continue')
                continue

            if c == 'U':
                below_sea_level += 1
            else:
                below_sea_level -= 1

            if below_sea_level == 0:
                valleys += 1
                sea_level = True

        print('D:[ {} ], asl: {}, bsl:{}, valleys: {}'.format(c, above_sea_level,below_sea_level, valleys))

    return valleys


# if going above ground level then first we have to reset that to 0 and start counting from that

'''
_/\      /\    /\/\_
   \    /  \  /
    \/\/    \/
'''

'''
DDUUDDUDUUUD

_          /\ 
 \  /\    /
  \/  \/\/

'''

'''
UDDDUDUDUU


_/\      /
   \    /
    \/\/

'''

'''
DDUDDUUDUU


_          _
 \        /
  \/\  /\/
     \/

'''


'''
UDDDUDUU


_/\
   \    /
    \/\/

'''

if __name__ == "__main__":
    n = 8
    s = 'DDUUDDUDUUUD'
    result = countingValleys(n, s)
    print(result)
