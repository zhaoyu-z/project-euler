import math

def triangular_pentagonal_hexagonal():
    i = 286
    while True:
        triangle = i * (i + 1) // 2
        if is_pentagonal(triangle) and is_hexagonal(triangle):
            return triangle
        i += 1

def is_hexagonal(num):
    return (1 + math.sqrt(8 * num + 1)) % 4 == 0

def is_pentagonal(num):
    return (math.sqrt(1 + 24 * num) + 1) % 6 == 0
    
print(triangular_pentagonal_hexagonal())
