def get_num_digits(n):
    return len(str(n))

def fibonacci(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def n_digit_fibonacci_number(n):
    dp = [0] * 3
    dp[1] = 1
    dp[2] = 2
    while get_num_digits(dp[-1]) < n:
        dp.append(0)
        dp[-1] = dp[-2] + dp[-3]
    return len(dp)

print(n_digit_fibonacci_number(1000))