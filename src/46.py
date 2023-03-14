from math import sqrt
from sympy import isprime

number = 3
primes = [2]

while True:
    if isprime(number):
        primes.append(number)
    else:
        for i in primes:
            if sqrt((number-i)/2) == int(sqrt((number-i)/2)):
                break
        else:
            print(number)
            break

    number += 2