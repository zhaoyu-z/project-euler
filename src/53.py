factorials = [-1] * 101

def get_factorials(num):
    if num == 0: return 1
    if num == 1: return 1
    if factorials[num] != -1:
        return factorials[num]
    ans = num * get_factorials(num-1)
    factorials[num] = ans
    return ans

def combinatorics(n, r):
    return get_factorials(n) // (get_factorials(r) * get_factorials(n-r))

def solution():
    ans = 0
    for n in range(23, 101):
        for r in range(1, n+1):
            if combinatorics(n, r) > 1_000_000:
                ans += 1
    return ans

print(solution())