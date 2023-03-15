from sympy import factorint, isprime

# def four_are_distinct_primes(num):
#     a, b, c, d = num, num+1, num+2, num+3
#     # if not isprime(b) or not isprime(c) or not isprime(d):
#     #     return False
#     a1 = factorint(a).keys()
#     b1 = factorint(b).keys()
#     c1 = factorint(c).keys()
#     d1 = factorint(d).keys()
#     print(a1)
#     print(b1)
#     print(c1)
#     print(d1)
#     if a1 != b1 and b1 != c1 and c1 != d1 and a1 != d1:
#         return True
#     return False

# # print(four_are_distinct_primes(134043))

# i = 647
# while True:
#     if four_are_distinct_primes(i):
#         print(i)
#         break
#     i += 2





def npf(number):
    """function which will return
    the number of prime factors"""
    i = 2
    a = set()
    while i < number**0.5 or number == 1:
        if number % i == 0:
            number /= i
            a.add(i)
            i -= 1
        i += 1
    return (len(a)+1)

# iterator
j = 2*3*5*7


# while True:
#     if npf(j) == 4:
#         j += 1
#         if npf(j) == 4:
#             j += 1
#             if npf(j) == 4:
#                 j += 1
#                 if npf(j) == 4:
#                     print(j-3)
#                     break
#     j += 1

