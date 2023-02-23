def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

day_of_week = 1 # 0 = Sunday, 1 = Monday, ..., 6 = Saturday
sundays_on_first = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if day_of_week == 0:
            sundays_on_first += 1
        
        if month == 2:
            if is_leap_year(year):
                days_in_month = 29
            else:
                days_in_month = 28
        elif month in [4, 6, 9, 11]:
            days_in_month = 30
        else:
            days_in_month = 31
        
        day_of_week = (day_of_week + days_in_month) % 7

print(sundays_on_first)
