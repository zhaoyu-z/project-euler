from itertools import permutations
from string import ascii_lowercase

def load_file(path):
    with open(path, 'r') as f:
        line = f.read().splitlines()[0]
        return list(map(int, line.split(",")))


def XOR_decryption():
    nums = load_file("../p059_cipher.txt")
    length = len(nums) // 3 + 1
    ans = 0

    for permu in permutations(ascii_lowercase, 3):
        plain_text = "".join(chr(d ^ ord(p)) for d, p in zip(nums, permu * length))
        # Initially remove [plain_text.find("Euler") >= 0] and see all outputs
        # if you see a paragraph that is not garbage, then find a key word from it
        # I use "Euler" in my case, so you can output the correct output
        if plain_text.find("the") >= 0 and plain_text.find(" ") >= 0 and plain_text.find("Euler") >= 0:
            print(plain_text)
            ans = sum(ord(c) for c in plain_text)
            # print(sum(ord(c) for c in plain_text))
            print()
    return ans

print(XOR_decryption())