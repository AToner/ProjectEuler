# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

day_of_week = 1
day = 1
month = 1
year = 1900

sundays = 0

while True:
    if day_of_week == 7:
        day_of_week = 0
        if (1901 <= year <= 2000) and day == 1:
            sundays += 1

    day_of_week += 1
    day += 1

    if month in {4, 6, 9, 11}:
        if day == 31:
            day = 1
            month += 1
    elif month == 2:
        days = 28
        if year % 4 == 0:
            days = 29

        if year % 100 == 0:
            days = 28
            if year % 400 == 0:
                days = 29

        if day == days + 1:
            day = 1
            month += 1
    else:
        if day == 32:
            day = 1
            month += 1

    if month == 13:
        year += 1
        month = 1

    if year >= 2001:
        break


print(sundays)
