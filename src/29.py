def distinct_powers(a_l, a_h, b_l, b_h):
    nums = set()
    for a in range(a_l, a_h+1):
        for b in range(b_l, b_h+1):
            nums.add(a ** b)
    return len(nums)

print(distinct_powers(2, 100, 2, 100))