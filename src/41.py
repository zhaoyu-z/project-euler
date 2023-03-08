import sympy

# pylint: disable=W0105
"""
Case: 1-digit pandigital (by enumeration)

1 is not prime

 no 1-digit pandigital number is prime



Case: 2-digit pandigital (by enumeration)

12=22x3 is not prime
21=3x7 is not prime

 no 2 -digit pandigital number is prime



Case: 3-digit pandigital (by rules of divisibility)

Observe that any such number must contain the digits 1,2,3

Now, observe that 1+2+3=6 , which is divisible by 3

⇒ any 3 -digit pandigital is divisible by 3

 no 3 -digit pandigital number is prime



Case: 5-digit pandigital (by rules of divisibility)

Observe that any such number must contain the digits 1,2,3,4,5

Now, observe that 1+2+3+4+5=15 which is divisible by 3

⇒ any 5 -digit pandigital is divisible by 3


 no 5 -digit pandigital number is prime



Case: 6-digit pandigital (by rules of divisibility)

Observe that any such number must contain the digits 1,2,3,4,5,6

Now, observe that 1+2+3+4+5+6=21 which is divisible by 3

⇒ any 6-digit pandigital is divisible by 3


 no 6-digit pandigital number is prime



Case: 8-digit pandigital (by rules of divisibility)

Observe that any such number must contain the digits 1,2,3,4,5,6,7,8

Now, observe that 1+2+3+4+5+6+7+8=36which is divisible by 3

⇒ any 8-digit pandigital is divisible by 3


 no 8-digit pandigital number is prime



Case: 9-digit pandigital (by rules of divisibility)

Observe that any such number must contain the digits 1,2,3,4,5,6,7,8,9

Now, observe that 1+2+3+4+5+6+7+8+9=45 which is divisible by 3

⇒ any 9-digit pandigital is divisible by 3


 no 9-digit pandigital number is prime

So, we only need to consider 4-digit and 7-digit numbers.
"""

def pandigital_prime(n):
    while True:
        if sympy.isprime(n) and is_pandigital(n, len(str(n))):
            return n
        n -= 1

def is_pandigital(n, m):
    return "".join(sorted(str(n))) == "".join([str(x) for x in range(1, m+1)])

print(max(pandigital_prime(7654321), pandigital_prime(4321)))