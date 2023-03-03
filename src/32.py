"""
    la: len(a)
    lb: len(b)
    lc: len(c)

    1. a x b = c
    2. la + lb + lc = 9
    3. la + lb >= lc
    4. la <= lc and lb <= lc

    => la + lb = 5
    
    la | lb | lc
    2    3    4
    3    2    4
    1    4    4
    4    1    4

    => after removing repeat
    la | lb | lc
    1    4    4
    2    3    4
"""

from itertools import permutations

products = set()

for digits in permutations('123456789'):
    for i in range(1, 4):
        for j in range(i+1, i+6):
            multiplicand = int(''.join(digits[:i]))
            multiplier = int(''.join(digits[i:j]))
            product = int(''.join(digits[j:]))
            if multiplicand * multiplier == product:
                products.add(product)

print(sum(products))