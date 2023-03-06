def double_base_palindromes(n):
    nums = []
    for i in range(n+1):
        if is_palindrome(i) and is_palindrome(bin(i)[2:]):
            nums.append(i)
    return sum(nums)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(double_base_palindromes(1000000))