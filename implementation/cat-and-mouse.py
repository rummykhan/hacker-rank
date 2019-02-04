#!/bin/python3

import sys


# https://www.hackerrank.com/challenges/electronics-shop/problem


def catAndMouse(x, y, z):
    d1 = abs(x - z)
    d2 = abs(y - z)

    if d1 == d2:
        return 'Mouse C'

    if d1 > d2:
        return 'Cat B'

    if d2 > d1:
        return 'Cat A'

    print("{}-{}".format(d1, d2))


questions = [i.strip() for i in open('question/cat-and-mouse.txt', mode='r').readlines()]
answers = [i.strip() for i in open('answer/cat-and-mouse.txt', mode='r').readlines()]

for index in range(0, len(questions)):
    question = questions[index]
    x, y, z = question.split(' ')
    result = catAndMouse(int(x), int(y), int(z))

    if result != answers[index]:
        print('Invalid Solution for {} = {}'.format(result, answers[index]))
