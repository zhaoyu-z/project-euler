def get_sum_even(n):
    a = 1
    b = 2
    sum_even = 0

    while b <= n:
        if b % 2 == 0:
            sum_even += b
        a, b = b, a + b

    return sum_even

print(get_sum_even(4000000))