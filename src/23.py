def sum_proper_divisors(n):
    divisors = set([1])
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sum(divisors)


"""
1.find all abundant numbers from 12 to 28123
2. 2 loops find all numbers that can be expressed using 2 abundant numbers and smaller than 28124
3. sum formula: 1 to 28123. minus the sum of all numbers in step 2
"""

abundant_numbers = []
for i in range(12, 28124):
    if sum_proper_divisors(i) > i:
        abundant_numbers.append(i)

all_numbers = set()
for i in abundant_numbers:
    for j in abundant_numbers:
        if i+j < 28124:
            all_numbers.add(i+j)

sum_from_1_to_28123 = (1 + 28123) * 28123 // 2
print(sum_from_1_to_28123 - sum(all_numbers))
