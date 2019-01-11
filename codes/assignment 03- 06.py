# Program to get next day of a given date

day = int(input('Enter the day: '))
month = int(input('Enter the month: '))
year = int(input('Enter the year: '))

if year % 400 == 0:
    leap_year = True
    if year % 100 == 0:
        leap_year = False
    if year % 4 == 0:
        leap_year = True
else:
    leap_year = False
if month in [1,3,5,7,8,10,12]:
    num_days = 31
elif month == 2:
    if leap_year:
        num_days = 29
    else:
        num_days = 28
else:
    num_days = 30

if day < num_days:
    day = day + 1
else:
    day = 1

if month == 12:
    month = 1
    year = year + 1
else:
    month = month + 1

print('The date of next day is',day,month,year)
