pentagonals = set()
for n in range(1, 10000):
    pentagonals.add(n * (3 * n - 1) // 2)

min_diff = float('inf')
for j in range(1, 10000):
    for k in range(j+1, 10000):
        Pj, Pk = j * (3 * j - 1) // 2, k * (3 * k - 1) // 2
        if Pk - Pj >= min_diff:
            break
        if Pj + Pk in pentagonals and Pk - Pj in pentagonals:
            diff = Pk - Pj
            if diff < min_diff:
                min_diff = diff

print(min_diff)