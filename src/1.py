def sum_of_multiples(n, m, x):
    ans = 0
    for i in range(1, x):
        if i % n == 0 or i % m == 0:
            ans += i
    return ans

print(sum_of_multiples(3, 5, 1000))