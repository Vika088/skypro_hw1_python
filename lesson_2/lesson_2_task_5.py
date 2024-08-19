def month_to_season(m):
        if m in (12, 1, 2):
            return 'winter'
        elif m in (3, 4, 5):
            return 'spring'
        elif m in (6, 7, 8):
            return 'summer'
        elif m in (9, 10, 11):
            return 'autumn'

m = int(input('enter month number: '))
print(month_to_season(m))



# month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# m = int(input('enter month number: ')) 

# def month_to_season(m):
#     if m in month_list ([-1], [0], [1]):
#             return 'winter'
#     elif m in month_list ([2], [3], [4]):
#             return 'spring'
#     elif m in month_list ([5], [6], [7]):
#             return 'summer'
#     elif m in month_list ([8], [9], [10]):
#             return 'autumn'
  
# print(month_to_season(m))