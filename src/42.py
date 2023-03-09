def load_file(path):
    lines = []
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    lines = [s.strip("\"") for s in lines[0].split(",")]
    return lines

def get_alphabetical_value(string):
    value = 0
    for c in string:
        value += ord(c) - ord('A') + 1
    return value

def get_triangle_numbers(n):
    triangle_nums = [-1] * (n+1)
    for i in range(1, n+1):
        triangle_nums[i] = 0.5 * i * (i+1)
    return triangle_nums

def coded_triangle_numbers(n, path):
    triangle_nums = get_triangle_numbers(n)
    words = load_file(path)
    ans = 0
    for w in words:
        if get_alphabetical_value(w) in triangle_nums:
            ans += 1
    return ans

print(coded_triangle_numbers(2000, "../p042_words.txt"))