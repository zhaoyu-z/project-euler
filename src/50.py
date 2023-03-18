from sympy import isprime
from tqdm import tqdm

def longest_consecutive_prime_sum(n):
    primes = []
    i = 2
    while sum(primes) < n:
        if isprime(i):
            primes.append(i)
        i += 1
    
    fin_seq = []
    l = len(primes)
    j = l

    while j != 0:
        i = 0
        while i + j < l + 1:
            seq = primes[i:i+j]
            if sum(seq) <= n and isprime(sum(seq)) and len(seq) > len(fin_seq):
                fin_seq = seq
            i += 1
        j -= 1
    return(sum(fin_seq))

print(longest_consecutive_prime_sum(1_000_000))