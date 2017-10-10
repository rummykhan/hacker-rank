# https://www.hackerrank.com/challenges/day-of-the-programmer?h_r=next-challenge&h_v=zen


# !/bin/python3

'''

Day of the programmer = 256th day of the year

* From  1700 to 1917, Russia's official calendar was the Julian calendar;

* since  1919 they used the Gregorian calendar system

* The transition from the Julian to Gregorian calendar system occurred in 1918

*  when the next day after January 31st was February 14th

* This means that in 1918, February 14th was the 32 day of the year in Russia.
'''


# Old Calendar
def is_julian_leap(year):
    return year % 4 == 0


# Old Calendar
def solve_julian(year):
    if is_julian_leap(year):
        feb = 29
    else:
        feb = 28

    sum = 31 + feb + 31 + 30 + 31 + 30 + 31 + 31

    return 9, (256 - sum)


# New Calendar
def is_georgian_leap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True

    return False


# New Calendar
def solve_georgian(year):
    if is_georgian_leap(year):
        feb = 29
    else:
        feb = 28

    sum = 31 + feb + 31 + 30 + 31 + 30 + 31 + 31

    return 9, (256 - sum)


def solve_1918(year):
    if is_georgian_leap(year):
        feb = 29
    else:
        feb = 28

    sum = 31 + feb + 31 + 30 + 31 + 30 + 31 + 31 - 13

    return 9, (256 - sum)


def solve(year):
    if year == 1918:
        month, day = solve_1918(year)
    elif year < 1918:
        month, day = solve_julian(year)
    else:
        month, day = solve_georgian(year)

    return '{}.0{}.{}'.format(day, month, year)


year = 1700
result = solve(year)
print(result)

year = 1900
result = solve(year)
print(result)

year = 2000
result = solve(year)
print(result)

year = 1918
result = solve(year)
print(result)
