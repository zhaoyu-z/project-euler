def factorial_digit_sum(n):
    fact = get_factorial(n)
    return sum(map(int, str(fact)))

def get_factorial(n):
    if n == 1:
        return 1
    return n * get_factorial(n-1)

print(factorial_digit_sum(100))