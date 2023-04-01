"""

The first convergents are 1/1,3/2,7/5,17/12,41/29.

if p/q is one convergent, p+2q/p+q will be the next.
"""


def square_root_covergents():
    p = q = 1
    count = 0

    for i in range(1000):
        numerator = p + 2*q
        denominator = p + q

        if len(str(numerator)) > len(str(denominator)):
            count += 1

        p = numerator
        q = denominator

    return count

print(square_root_covergents())