from math import sqrt

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(3, int(sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True

def get_num_primes_equation(a, b):
    n = 0
    while True:
        equation = n ** 2 + a * n + b
        if not is_prime(equation):
            break
        n += 1
    return n

def quadratic_primes(a_lower, a_higher, b_lower, b_higher):
    best, besta, bestb = 0, 0, 0
    for a in range(a_lower, a_higher+1):
        """
        b must be positive, because when n=0 case where the expression can be reduced to b,
         which therefore has to be prime.
        """
        for b in range(2, b_higher+1):
            c = get_num_primes_equation(a, b) 
            if c > best:
                best, besta, bestb = c, a, b
    return besta * bestb

print(quadratic_primes(-1000, 1000, -1000, 1000))