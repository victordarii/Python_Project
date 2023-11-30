age = int(input('Enter your age\n'))

result = None

if 0 <= age <= 150:
    if age < 21:
        result = 'Teenager'
    elif age < 55:
        result = 'Adult'
    else:
        result = 'Senior'
else:
    result = 'Invalid age!'

print(result)
