def sum_proper_divisors(n):
    divisors = set([1])
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sum(divisors)

amicable_numbers = set()
for a in range(1, 10000):
    b = sum_proper_divisors(a)
    if b != a and sum_proper_divisors(b) == a:
        amicable_numbers.add(a)
        amicable_numbers.add(b)

print(sum(amicable_numbers))
