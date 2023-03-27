def is_palindrome(num):
    return str(num) == str(num)[::-1]

def palindrome(num):
    return int(str(num)[::-1])

def reverse_add(num):
    return num + palindrome(num)

def is_lychel(num):
    n = 50
    while n > 0:
        num = reverse_add(num)
        if is_palindrome(num):
            return False
        n -= 1
    return True

def lychel_numbers():
    count = 0
    for i in range(1, 10_000+1):
        if is_lychel(i):
            count += 1
    return count

print(lychel_numbers())