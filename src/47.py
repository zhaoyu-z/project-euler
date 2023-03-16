def npf(number):
    """function which will return
    the number of prime factors"""
    i = 2
    a = set()
    while i < number**0.5 or number == 1:
        if number % i == 0:
            number /= i
            a.add(i)
            i -= 1
        i += 1
    return (len(a)+1)

def four_are_distinct_primes():
    j = 2*3*5*7

    while True:
        if npf(j) == 4:
            j += 1
            if npf(j) == 4:
                j += 1
                if npf(j) == 4:
                    j += 1
                    if npf(j) == 4:
                        return j-3
        j += 1

print(four_are_distinct_primes())
