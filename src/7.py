def get_nth_prime(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        if all(i % p for p in primes):
            primes.append(i)
        i += 2
    return primes[-1]

print(get_nth_prime(10001))