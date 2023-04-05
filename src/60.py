from itertools import combinations
import random

def generate_primes(n): # sieve of Erotosthenes
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    primes = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            primes.append(i)
    return primes

def is_prime(n, k = 3): # Miller–Rabin primality test
    if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
        return [False, False, True, True, False, True][n]
    elif n % 2 == 0:  # should be faster than n % 2
        return False
    else:
        s, d = 0, n - 1
        while d % 2 == 0:
            s, d = s + 1, d >> 1
        # A for loop with a random sample of numbers
        for a in random.sample(range(2, n-2), k):
            x = pow(a, d, n)
            if x != 1 and x + 1 != n:
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False  # composite for sure
                    elif x == n - 1:
                        a = 0  # so we know loop didn't continue to end
                        break  # could be strong liar, try another a
                if a:
                    return False  # composite if we reached end of this loop
        return True  # probably prime if reached end of outer loop


def test_prime_sets(prime_set):
    for n1, n2 in list(combinations(prime_set, 2)):
        if not is_prime(int(str(n1) + str(n2))) or \
            not is_prime(int(str(n2) + str(n1))):
            return False
    return True

primes = generate_primes(10_000)

def prime_pair_sets():
    for a in primes:
        for b in primes:
            if b > a and test_prime_sets([a, b]):
                for c in primes:
                    if c > b and test_prime_sets([a, b, c]):
                        for d in primes:
                            if d > c and test_prime_sets([a, b, c, d]):
                                for e in primes:
                                    if e > d and test_prime_sets([a, b, c, d, e]):
                                        return [a, b, c, d, e]

ans = prime_pair_sets()
print(ans)
print(sum(ans))