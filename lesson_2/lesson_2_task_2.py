year = int(input('Is year leap? '))


def is_year_leap(year):
    if (year % 4 == 0):
        return True
    else:
        return False


result = is_year_leap(year)
print(f'год {year}: {result}')
