from math import gcd
from functools import reduce

def generate_factors_all(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    minimal_factors = []
    for prime in primes:
        i = prime
        while i <= n:
            if prime not in minimal_factors:
                minimal_factors.append(prime)
            i *= prime
    
    return minimal_factors

# print(generate_factors_all(20))

def generate_factor_one(n):
    factors = []
    for i in range(2, n+1):
        while n % i == 0:
            factors.append(i)
            n //= i
        if n == 1:
            break
    return factors

# print(generate_factor_one(20))

def get_all_divisible(n):
    
    numbers = range(1, n+1)
    factors = [generate_factor_one(n) for n in numbers]

    prime_factors = set()
    for factor_list in factors:
        prime_factors.update(set(factor_list))

    prime_powers = []
    for factor in prime_factors:
        powers = [factor ** factor_list.count(factor) for factor_list in factors if factor in factor_list]
        prime_powers.append(max(powers))

    smallest_number = reduce(lambda x, y: x*y // gcd(x,y), prime_powers)
    return smallest_number

print(get_all_divisible(20))
