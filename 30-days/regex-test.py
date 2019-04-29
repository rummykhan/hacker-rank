#!/bin/python3

import math
import os
import random
import re
import sys


def get_email(email):
    import re

    regex = r"(\S+)@(\S+)"

    test_str = email

    matches = re.search(regex, test_str)

    if matches:
        return matches.group(2)


if __name__ == '__main__':
    N = int(input())

    names = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if get_email(emailID) == 'gmail.com':
            names.append(firstName)

    for name in sorted(names):
        print(name)
