from sympy import isprime

def spiral_primes(given_ratio):

    num_nums = 1
    num_primes = 0

    i = 0
    num_levels = 1
    ratio = 1
    
    while ratio >= given_ratio:
        for _ in range(4):
            i += num_levels
            cur = 2 * i + 1
            num_nums += 1
            if isprime(cur):
                num_primes += 1
        ratio = num_primes  / num_nums
        num_levels += 1
    return  2 * num_levels - 1

print(spiral_primes(0.1))