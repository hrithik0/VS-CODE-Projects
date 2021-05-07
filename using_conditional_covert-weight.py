weight = input('Write your weight: ')
select = input('(L)for lbs or (K)for kg: ')


if select.upper() == 'K':
    converted = 0.45 * float(weight)
    print('Weight converted into {}kgs'.format(converted))
elif select.upper() == 'L':
    converted = 2.2 * float(weight)
    print('Weight converted into {}lbs'.format(converted))
elif select == " ":
    print('No choice is entered.')
else:
    print('wrong choice is entered.')
