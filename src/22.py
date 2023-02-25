def load_file(path):
    lines = []
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    return lines

def get_alphabetical_value(string):
    value = 0
    for c in string:
        value += ord(c) - ord('A') + 1
    return value

f = load_file("../p022_names.txt")
f = [s.strip("\"") for s in f[0].split(",")]
f.sort()

ans = 0
for name in f:
    ans += get_alphabetical_value(name) * (f.index(name)+1)
print(ans)