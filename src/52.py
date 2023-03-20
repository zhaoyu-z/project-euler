def permuted_multiples():
    i = 1
    while True:
        if set(str(i)) == set(str(6*i)) and \
            set(str(i)) == set(str(5*i)) and \
            set(str(i)) == set(str(4*i)) and \
            set(str(i)) == set(str(3*i)) and \
            set(str(i)) == set(str(2*i)):
            return i
        i += 1

print(permuted_multiples())
