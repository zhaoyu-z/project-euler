def sum_of_squared(n):
    return sum(i**2 for i in range(1, n+1))

def squared_of_sum(n):
    return sum(range(1, n+1))**2

def difference(n):
    return abs(squared_of_sum(n) - sum_of_squared(n))

print(difference(100))