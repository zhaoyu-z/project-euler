from collections import Counter

def sieve(n):
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

primes = sieve(1000000)

# primes with 3 replacable places
primes = [x for x in primes if len(str(x)) - len(set(str(x))) >= 3]

def helper(s):
    """take a number and return a list with families
    for example if the input number is 566003 then
    the result will be
    [[566003,566113,566223,566333,566443,566553,566663,566773,566883,566993],
    [500003,511003,522003,533003,544003,555003,566003,577003,588003,599003]]"""
    s = str(s)
    sol = []

    for duplicate in (Counter(s) - Counter(set(s))):
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        temp = [int(s.replace(duplicate, x)) for x in a]
        sol.append(temp)
    return sol

checked = []

def check(l):

    """take a list and remove all the values which are
    not prime numbers, finally return a list with only
    prime numbers"""

    for i in l:
        checked.append(i)
        if i not in primes:
            l.remove(i)
    return l


def prime_digit_replacements():
    i = 0
    while True:
        if primes[i] not in checked:
            replacements = helper(primes[i])
            for j in replacements:
                if len(check(j)) == 8:
                    return j[0]
        i += 1

print(prime_digit_replacements())