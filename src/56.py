def powerful_digit_sum():
    ans = 0
    for a in range(100):
        for b in range(100):
            ans = max(ans, digit_sum(a ** b))
    return ans

def digit_sum(n):
    return sum(list(map(int, str(n))))

print(powerful_digit_sum())