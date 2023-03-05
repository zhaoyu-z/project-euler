import math

def digit_factorial_sum(n):
    return sum(math.factorial(int(digit)) for digit in str(n))

"""
The upper bound has 7 digits because for any 8-digit number, 
the maximum possible value of the sum of the factorial of its digits is 8 * 9! = 2903040,
which is a 7-digit number.
"""
upper_bound = 7 * math.factorial(9)  # maximum 7-digit number
solutions = []
for n in range(3, upper_bound):
    if n == digit_factorial_sum(n):
        solutions.append(n)
# print(solutions) # 145, 40585
print(sum(solutions))