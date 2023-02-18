from itertools import accumulate
import operator

def find_pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return [a, b, c]
    return None

ans = find_pythagorean_triplet(1000)
print(ans[2] * ans[1] * ans[0])