counts = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}

def number_to_english(n):
    if n == 1000:
        return "one thousand"
    elif n >= 100:
        hundreds = n // 100
        remainder = n % 100
        if remainder == 0:
            return f"{number_to_english(hundreds)} hundred"
        else:
            return f"{number_to_english(hundreds)} hundred and {number_to_english(remainder)}"
    elif n >= 20:
        tens = (n // 10) * 10
        ones = n % 10
        if ones == 0:
            return counts[tens]
        else:
            return f"{counts[tens]}-{counts[ones]}"
    else:
        return counts[n]

count = 0
for i in range(1, 1001):
    cur = number_to_english(i)
    # print(i, cur)
    count += len(cur.replace(" ", "").replace("-", ""))
print(count)