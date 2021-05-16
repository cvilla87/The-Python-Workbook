def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def next_day(_date):
    dt_split = _date.split('-')
    day, month, year = int(dt_split[2]), int(dt_split[1]), int(dt_split[0])

    if month == 2 and leap_year(year):
        max_day = days_month[13]
    else:
        max_day = days_month[month]

    if day != max_day:
        day += 1
    else:
        day = 1
        if month != 12:
            month += 1
        else:
            month = 1
            year += 1

    return f'{year}-{month:02}-{day:02}'


# February has 28 days in common years or 29 in leap years.
# Month 13 will work as February when in leap year.
days_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31, 13: 29}

# Tests
dates_test = ['2019-01-01', '2019-02-28', '2019-08-31', '2020-02-27', '2020-02-28',
              '2020-02-29', '2020-04-14', '2020-04-30', '2020-12-31', '2021-02-28']

for date in dates_test:
    print(f'{date} -> {next_day(date)}')
