def champernownes_constant():
    string = [0]
    num = 1
    n = 1000001
    while len(string) < n:
        add(string, num)
        num += 1
    return get_ans(string)

def add(string, num):
    if num < 10:
        string.append(str(num))
    else:
        for c in str(num):
            string.append(c)

def get_ans(string):
    num = 1
    ans = 1
    while num < 1000000:
        ans *= int(string[num])
        num *= 10
    return ans

print(champernownes_constant())