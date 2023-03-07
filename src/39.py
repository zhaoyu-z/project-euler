from math import sqrt

def count_solutions(p):
    count = 0
    for a in range(1, p):
        for c in range(a+1, p-a):
            b = sqrt(c**2 - a**2)
            if b.is_integer() and a + b + c == p:
                count += 1
    return count

max_solutions = 0
max_p = 0

for p in range(1, 1001):
    solutions = count_solutions(p)
    if solutions > max_solutions:
        max_solutions = solutions
        max_p = p

print(max_p)
