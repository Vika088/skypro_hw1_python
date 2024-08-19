import math as m

num = float(input('enter number: '))
square_of_a_num = num ** 2

def square(num):

    if isinstance(num, int):
        return square_of_a_num
    else:
        return m.ceil(square_of_a_num)

result = square(num)
print ('square = ', result)