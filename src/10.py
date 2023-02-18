def sum_of_primes_below(n):
    primes = [2]
    for i in range(3, n, 2):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
    return sum(primes)

print(sum_of_primes_below(2000000))