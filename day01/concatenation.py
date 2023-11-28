name = 'James'
age = 24

print('Name is: ' + name)  # will successfully print

# print('Name is: ' + age)    # will throw error

# For concatenating other types to a str is best to use format() not + operator

print('Age is: {}'.format(age))

print('My name is {} and I am {} years old'.format(name, age))

print('My age is ' + str(age))

shoes_size = 44

print('My age is ' + str(age) + " and my shoes size is " + str(shoes_size))

print(f'My name is {name} and my age is {age} - terrific')  # best practice

print('python', 3, 'is awesome:', True)

