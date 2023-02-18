def count_divisors(n):
    count = 1
    i = 2
    while i*i <= n:
        power = 1
        while n % i == 0:
            power += 1
            n //= i
        count *= power
        i += 1
    if n > 1:
        count *= 2
    return count

def get_triangle_number_with_n_divisors(x):
    n = 1
    while True:
        if n % 2 == 0:
            divisors = count_divisors(n // 2) * count_divisors(n + 1)
        else:
            divisors = count_divisors(n) * count_divisors((n + 1) // 2)
        if divisors > x:
            triangle_number = n * (n + 1) // 2
            return triangle_number
        n += 1

print(get_triangle_number_with_n_divisors(500))