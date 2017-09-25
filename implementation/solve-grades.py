# https://www.hackerrank.com/challenges/grading

def solve(grades):
    results = []
    for grade in grades:

        if grade < 38:
            results.append(grade)
            continue

        if (grade + 2) % 5 == 0:
            results.append(grade + 2)
            continue

        if (grade + 1) % 5 == 0:
            results.append(grade + 1)
            continue

        results.append(grade)

    return results


grades = [73, 67, 38, 33, 51, 63, 78, 55, 74]
print(grades)
result = solve(grades)
print("\n".join(map(str, result)))
