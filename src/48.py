def self_powers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i ** i
    return str(sum)[-10:]

print(self_powers(1000))