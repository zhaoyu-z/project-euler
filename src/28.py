def number_spiral_diagonals(n):
    # a nxn square, n must be odd.
    nums = [1]
    cur = 1
    num_levels = n // 2
    for i in range(1, num_levels+1):
        increment = 2 * i
        for i in range(4):
            cur += increment
            nums.append(cur)
    return sum(nums)

print(number_spiral_diagonals(1001))