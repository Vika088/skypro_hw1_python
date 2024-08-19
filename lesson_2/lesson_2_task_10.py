def bank( x, y):
    pct = 0.10 #To increase the amount - * 1.1 or 1+pct => 1.1^years - чтобы получить повышение процента, относительно количества лет
    amount_of_money = x * ((1+pct) ** y) 
    return amount_of_money

x = float(input('your deposite amount: '))
y = int(input('number_of_years: '))

print(f'amount after {y} years: ', bank(x, y))