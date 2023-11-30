people = 76

result = None

if 50 <= people <= 100:
    if people == 50:
        result = f'Total: {people} ====> 20 crew, {people - 20} passengers'
    elif 50 < people <= 75:
        result = f'Total: {people} ====> 25 crew, {people - 25} passengers'
    else:
        result = f'Total: {people} ====> 30 crew, {people - 30} passengers'
else:
    result = 'Number of people on the ship is not valid'

print(result)

print('----------------------------------------------------------------------------')

people2 = 100

result2 = None

if people2 == 50 or people2 == 75 or people2 == 100:
    if people2 == 50:
        result2 = 'Total: 50  ====> 20 crew, 30 passengers'
    elif people2 == 75:
        result2 = 'Total: 75  ====> 25 crew, 50 passengers'
    else:
        result2 = 'Total: 100 ====> 30 crew, 70 passengers'
else:
    result2 = 'Number of people on the ship is not valid'

print(result2)
