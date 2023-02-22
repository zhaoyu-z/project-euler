def power_digit_sum(n):
    return sum(map(int, str(2**n)))

print(power_digit_sum(1000))