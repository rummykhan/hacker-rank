#!/usr/bin/py
# Head ends here

def substrings(s):
    result = []
    for i, v in enumerate(s):
        result.append(v)
        for j in range(i + 2, len(s) + 1):
            result.append(v + s[i + 1:j])

    print(sorted(set(result)))
    return sorted(set(result))


def make_suffix_array(s):
    result = [x for x in s]

    length = len(s)
    for i, j in enumerate(s):
        result.append(s[i:length])

    for i, j in enumerate(s):
        result.append(s[0:i + 1])

    for n in range(1, len(s)):
        for i, j in enumerate(s):
            result.append(s[i:i + n])

    return sorted(set(result))


def findStrings(a, query):
    combinations = []

    for i in a:
        combinations += make_suffix_array(i)

    combinations = sorted(set(combinations))

    for q in query:

        if q <= len(combinations):
            print(combinations[q - 1])
        else:
            print('INVALID')


def test():
    n = 2
    string = ['aab', 'aac']
    string = ['rummykhan']
    q = 3
    query = [3, 8, 23]
    findStrings(string, query)


if __name__ == '__main__':
    test()
