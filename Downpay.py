price = 1000000
is_good_credit = True

if is_good_credit:
    down_price = 0.1*price
else:
    down_price = 0.2*price
print(f'Price of house is: {down_price}')

