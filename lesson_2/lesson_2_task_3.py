import math as m

num = float(input('enter number: '))


def square(num):
    if isinstance(num, int):
        square_of_a_num = num ** 2
        return square_of_a_num
    else:
        return m.ceil(square_of_a_num)


result = square(num)
print('square = ', result)
