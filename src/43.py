from itertools import permutations

pandigitals = permutations("0123456789")
primes = [2, 3, 5, 7, 11, 13, 17]

ans = 0

for pandigital in pandigitals:
    substrings = ["".join(pandigital[i+1:i+4]) for i in range(7)]

    divisible = True
    for i in range(7):
        if int(substrings[i]) % primes[i] != 0:
            divisible = False
            break

    if divisible:
        ans += int("".join(pandigital))

print(ans)
