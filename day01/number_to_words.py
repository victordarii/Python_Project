num = int(input('Enter a number\n'))

result = 'Nine' if num == 9 else 'Eight' if num == 8 else 'Seven' if num == 7 else 'Six' if num == 6 \
    else 'Five' if num == 5 else 'Four' if num == 4 else 'Three' if num == 3 else 'Two' if num == 2 \
    else 'One' if num == 1 else 'Zero' if num == 0 else 'Invalid Number given! Valid numbers are 0-9!'

print(result)
