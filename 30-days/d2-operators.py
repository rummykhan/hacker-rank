import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost * tip_percent) / 100
    tax = (meal_cost * tax_percent) / 100

    total = meal_cost + tip + tax

    print(total)

    print(round(total))


if __name__ == '__main__':
    meal_cost = float(10.25)

    tip_percent = int(17)

    tax_percent = int(5)

    solve(meal_cost, tip_percent, tax_percent)
