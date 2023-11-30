user_integer = int(input('Enter a number\n'))

if user_integer % 3 == 0 and user_integer % 5 == 0:
    print('FizzBuzz')
elif user_integer % 5 == 0:
    print('Buzz')
elif user_integer % 3 == 0:
    print("Fizz")
else:
    print("Hello Wisconsin")
