num = [0] * (10**8)
def get_collatz(n):
    if n == 1:
        return 1

    if n < 10**8 and num[n] != 0:
        return num[n]

    ans = 0
    if n % 2 == 0:
        ans = get_collatz(n // 2) + 1
    else:
        ans = get_collatz(3 * n + 1) + 1
    
    if n < 10**8:
        num[n] = ans
    return ans

def get_longest_collatz_below_n(n):
    ans, nmax = 0, 0
    for i in range(1, n+1):
        cur = get_collatz(i)
        if nmax < cur:
            nmax = cur
            ans = i
    return ans

print(get_longest_collatz_below_n(10**6))