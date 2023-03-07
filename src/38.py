def is_pandigital(n):
    # Checks if a number is 1 to 9 pandigital.
    return ''.join(sorted(str(n))) == '123456789'

largest_pandigital = 0


"""
Starting number must have 4 digits.

Reason:

Let's assume that the starting integer has one digit.
In this case, the concatenated product with (1,2,...,n)
can have at most 5 digits (since 9 x 1 × 2 × 3 × 4 = 9 × 24 = 216,
which has three digits). Similarly, if the starting integer has two digits,
the concatenated product can have at most 6 digits (since 98 × 1 × 2 × 3 = 588,
which has three digits). Therefore, we can focus on starting integers
with three or more digits.

Let's assume that the starting integer has three digits,
and let's call it "abc". Then, the concatenated product
with (1,2,...,n) can have at most 9 digits if n = 3
(since 999 × 1 × 2 × 3 = 17982, which has five digits)
or n = 4 (since 999 × 1 × 2 × 3 × 4 = 71988, which has
five digits). Therefore, the maximum possible concatenated
product for a three-digit starting integer is a five-digit number.

Next, let's assume that the starting integer has four digits,
and let's call it "abcd". Then, the concatenated product with
(1,2,...,n) can have at most 9 digits if n = 2 (since 9999 × 1 × 2 = 19998,
which has five digits) or n = 3 (since 9999 × 1 × 2 × 3 = 59994,
which has five digits). Therefore, the maximum possible concatenated
product for a four-digit starting integer is a five-digit number.

Finally, let's assume that the starting integer has five digits or more.
In this case, the concatenated product with (1,2,...,n) will have at least
10 digits, which is not possible.

Therefore, we can conclude that the starting integer must have four digits,
and we can search for the largest possible concatenated product by trying
different four-digit starting integers and their concatenated products with
(1,2,...,n) for n = 2 and n = 3.
"""
for n in range(1000, 10000):
    concatenated_product = int(str(n) + str(n*2))
    if is_pandigital(concatenated_product) and concatenated_product > largest_pandigital:
        largest_pandigital = concatenated_product
    concatenated_product = int(str(n) + str(n*2) + str(n*3))
    if is_pandigital(concatenated_product) and concatenated_product > largest_pandigital:
        largest_pandigital = concatenated_product

print(largest_pandigital)
