"""
Java: static typing
    DataType var = Data;

Python: Dynamic Typing
    var = Data

    Python is slower then Java

    when assigning data to a var data type will be set back scene
"""

name = None

print(name)

name = 'James'

print(name)

# type() method is commonly used to check the data type of given variable
# instanceOf() in Java

print(type(name))

age = 21
print(age)
print(type(age))

age = 'lol'

print(age)

print(type(age))

# dynamic typing is when Python adds the data type not you
# unlike Java where we are the ones that add data type to a var

# unlike Java primitive/non-primitive data types in Python all data types comes from a class

is_employed = True
is_married = False

print(type(is_employed))

# Type casting use a constructor for any casting and reassign to its variable

s = '23'

print(s * 2)

s = int(s)

print(s * 2)

# Concatenation

print("Hello" + "World")



