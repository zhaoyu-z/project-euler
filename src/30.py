def digit_fifth_powers(n):
    ans = []
    for i in range(2, 1000000):
        if check_sum_of_digit(i, n):
            ans.append(i)
    print(ans)
    return sum(ans)

def check_sum_of_digit(n, m):
    s = str(n)
    return sum(int(x) ** m for x in s) == n

print(digit_fifth_powers(5))
