d1 = ('Alex')
d2 = ('Alex',)  # coma is needed just like square brackets in Java's Array

print(type(d1))  # this is class: str
print(type(d2))  # this is class: tuple

print('--------------------------------------')

days = ('Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun', 1, 2, 3, 4)

print(days)
# days[0] = 'Java'  # will throw error - Tuples don't support item assignment

print(days[0])
print(days[-1])

print('-------------------work days-------------------')

days = ('Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun')

work_days = days[:5]  # here index 5 is excluded
print(work_days)

happy_days = days[5:]  # here index 5 is included
print(happy_days)

print(type(days))  # they are all new tuples
print(type(work_days))
print(type(happy_days))

print('--------------------- == check context , is check memory-----------------------')

# == check context and see if they are equal --> this is similar to .equal() in Java
# is check memory and see if it is same object meaning it is pointing to the same memory allocation in the system
# is operator in Python is like == operator in Java

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

print(tuple1 == tuple2)  # this will only check the context/the elements
print(tuple1 is tuple2)  # this will check if they are the same objects. Does it reference to the same memory allocation

# if you change anything in any of the tuple1 or tuple2 they're reference name does not point to the same memory anymore

print('-----------------------merge tuples----------------------------')

tuple3 = tuple1 + tuple2

print(tuple3)

tuple4 = tuple1 * 3
print(tuple4)

print('----------------------------reverse tuple-----------------------------------')
days = ('Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun')
print(days)

reversed_days_tuple = days[::-1]
print(reversed_days_tuple)

reversed_days2_tuple = tuple(reversed(days))  # Create and return a new object.
print(reversed_days2_tuple)

reversed_days3_tuple = reversed(days)
# this reversed constructor function it constructs the reversed object from the tuple
# if you want to convert that object back to tuple you need to pass it inside tuple()
print(reversed_days3_tuple)
print(type(reversed_days3_tuple))  # <class 'reversed'> not
print(type(reversed_days2_tuple))  # <class 'tuple'>

print('---------------------------- index() ------------------------------------')

print(days[2])
print(days.index('Wed'))

print('---------------------------- count() ------------------------------------')

numbers = (10, 10, 10, 10, 20, 30, 40, 50, 10)
print(numbers.count(10))

# if count(character) returns 1 this is a unique character
# in Java for that reason you would use a nested loop

print('------------------------access each element in a tuple--------------------------------')

# use loop to access a tuple elements

for day in days:
    print(day)

print('--------------------------measure a tuple size and manipulate those indexes------------------------')

for each in range(0, len(days)):
    print(each)

for each in range(0, len(days)):
    print(days[each])

print('---------------------------- NESTED TUPLE --------------------------------')

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9, 10))

print(len(nested_tuple))  # size is 3 because there are 3 tuple inside one

print('---------------------------- NESTED TUPLE --------------------------------')

for each_tuple in nested_tuple:
    # print(each_tuple)
    for each_element in each_tuple:
        print(each_element)

print('--------------------------------------------------------------------------')

for each_tuple in range(0, len(nested_tuple)):
    for each_element in range(0, len(nested_tuple[each_tuple])):
        print(nested_tuple[each_tuple][each_element])
