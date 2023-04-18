def cubic_permutations(n):
    cubes = []
    i = 0

    while True:
        cube = sorted(list(str(i**3)))
        cubes.append(cube)
        if cubes.count(cube) == n:
            return cubes.index(cube) ** 3
        i += 1

print(cubic_permutations(5))