from sympy import isprime

def ispermutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def prime_permutations():
    i = 1488
    while i < 10000:
        if isprime(i):
            for incre in range(1, (10000-i) // 2):
                j = i + incre
                if isprime(j) and ispermutation(i, j):
                    k = j + incre
                    if isprime(k) and ispermutation(j, k):
                        return str(i)+str(j)+str(k)
        i += 1

print(prime_permutations())