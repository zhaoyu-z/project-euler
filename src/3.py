import math

def largest_prime_factor(n):
    while n % 2 == 0:
        n = n // 2
        last_factor = 2

    factor = 3
    max_factor = math.sqrt(n)
    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            n = n // factor
            last_factor = factor
            while n % factor == 0:
                n = n // factor
            max_factor = math.sqrt(n)
        factor += 2
        
    return last_factor if n == 1 else n

print(largest_prime_factor(600851475143))