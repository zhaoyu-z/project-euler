from itertools import permutations

def get_all_permutations(arr):
    return list(permutations(arr))

nums = get_all_permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[999999]

print("".join(str(nums).replace(", ", "").replace("(", "").replace(")", "")))