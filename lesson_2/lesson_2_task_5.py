month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

m = int(input('enter month number: '))


def month_to_season(m):

    if m in month_list[-1:] + month_list[:2]:
        return 'winter'
    elif m in month_list[2:5]:
        return 'spring'
    elif m in month_list[5:8]:
        return 'summer'
    elif m in month_list[8:-1]:
        return 'autumn'


print(month_to_season(m))
