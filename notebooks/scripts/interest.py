b = float(input('Initial balance: '))
p = float(input('Interest rate in per cent: '))
i = p / 100 * b
# interest
b = b + i
# new balance
print('New balance: ${:,.2f}'.format(b))
# format currency
# https://www.kite.com/python/answers/how-to-format-currency-in-python
