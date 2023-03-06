import sympy

def is_truncatable_prime(n):
    if n < 10 or not sympy.isprime(n):
        return False
    
    # Check left-truncatability
    m = str(n)
    while m:
        if not sympy.isprime(int(m)):
            return False
        m = m[1:]
    
    # Check right-truncatability
    m = str(n)
    while m:
        if not sympy.isprime(int(m)):
            return False
        m = m[:-1]
    
    return True

trunc_primes = []
n = 10
while len(trunc_primes) < 11:
    if is_truncatable_prime(n):
        trunc_primes.append(n)
    n += 1

print(sum(trunc_primes))