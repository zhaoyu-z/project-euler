def sieve_of_eratosthenes(n):
    """Return a list of prime numbers up to n."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i**2, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]

def circular_permutations(n):
    """Return a list of all circular permutations of n."""
    rotations = []
    digits = str(n)
    for i in range(len(digits)):
        rotation = int(digits[i:] + digits[:i])
        rotations.append(rotation)
    return rotations

primes = sieve_of_eratosthenes(1000000)
circular_primes = []
for p in primes:
    circular = True
    for perm in circular_permutations(p):
        if perm not in primes:
            circular = False
            break
    if circular:
        circular_primes.append(p)

print(len(circular_primes))