from fractions import Fraction

def digit_cancelling_fractions():
    nums = find_curious_fractions()
    num = fractions_to_lowest_common_terms(nums)
    return num.denominator

"""
16/64, 19/95, 26/65, 49/98
"""
def find_curious_fractions():
    fractions_list = []
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            original_fraction = Fraction(numerator, denominator)
            # print(original_fraction)
            num_digits = set(str(numerator))
            denom_digits = set(str(denominator))
            common_digits = num_digits.intersection(denom_digits)
            if len(common_digits) == 1:
                digit = common_digits.pop()
                new_numerator = int(str(numerator).replace(digit, "", 1))
                new_denominator = int(str(denominator).replace(digit, "", 1))
                if new_denominator != 0 and \
                    Fraction(new_numerator, new_denominator) == original_fraction and \
                    denominator % 10 != 0:
                    # print(str(numerator) + "/" + str(denominator), Fraction(new_numerator, new_denominator))
                    fractions_list.append(original_fraction)
    return fractions_list

def fractions_to_lowest_common_terms(arr):
    frac = Fraction(1 ,1)
    for x in arr:
        frac *= x
    return frac

# print(find_curious_fractions())
print(digit_cancelling_fractions())