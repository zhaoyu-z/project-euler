from tqdm import tqdm

def powerful_digit_counts(n):
    count = 0
    for base in tqdm(range(1, n)):
        for power in range(1, n):
            num = base ** power
            if len_of_num(num) == power:
                count += 1
    return count

def len_of_num(num):
    return len(str(num))

def is_nth_power(num, n):
    return round(num ** (1/n)) ** n == num

print(powerful_digit_counts(22)) # last base is 21

# pylint: disable=W0105
"""
With a little more thought on the math side, this can actually be done by hand.
x^n has n digits when

10^(n-1) <= x^n < 10^n

First of all, x < 10. So we only have to try x={1, 2, 3, ..., 9}. 
The next thing to notice is that the left inequality is true for small values of n,
but the 10^(n-1) part grows faster than the x^n part. All you have to do is find out when they meet.
This can be done like this

10^(n-1)=x^n => 0.1*10^n=x^n => log(0.1)+n*log(10)=n*log(x) 
=> log(10)=n*(log(10)-log(x)) => n=log(10)/(log(10)-log(x))

That value of n is already not good, 
so we have to round down to find out the largest integer 
for which the inequality holds true.

 x   floor(log(10)/(log(10)-log(x)))
-------------------------------------
 1   1
 2   1
 3   1
 4   2
 5   3
 6   4
 7   6
 8   10
 9   21
--------------------
Total: 49
"""