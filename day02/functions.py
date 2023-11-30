# Java Methods:   public static void methodName(parameter){}
import numbers


# if I declare a method under a class it is considered a METHOD
# if I declare it under No class it is considered a FUNCTION - it is considered inside a module (dependency in Java)

def display_message():
    print('Hello Wisconsin')
    print('Hello World')


display_message()


def value():  # this will return a value no matter which type it is but this is not mandatory
    return 10


print(value())


def mandatory_return_int() -> int:  # arrow with desired type must be given
    return 10  # return int is mandatory otherwise will give error


def square(num):
    return num * num


print(square(4))


def divide(num1, num2):
    return num1 / num2


print(divide(10, 2))


# print(divide('Java', 'Python'))# because Python is dynamic typing it will take any type not just the needed exact type

# to prevent this we can restrict/force a SPECIFIC type for the required arguments

def square2(num: int):  # now to avoid error we must give only the required type nothing else
    return num * num  # because we are restricted to an int argument


print(square2(11))


def add(num1: int, num2: int) -> int:
    return num1 + num2


print(add(1, 4))


def addition(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2


print(addition(12.2, 2.8))
print(addition(12, 2))

print('------------------------------------------------')


# example of method overloading

def sum_numbers(n1: numbers, n2: numbers, n3: numbers = 0,
                n4: numbers = 0) -> numbers:  # this is a function(not under class)
    return n1 + n2 + n3 + n4


print(sum_numbers(10, 20))
print(sum_numbers(10, 20, 30))
print(sum_numbers(10, 20, 30, 40))

print('------------------------------------------------')


class Test:
    def method(self):  # because it is under a class this is a method
        pass


print('------------------------------------------------')


def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}'.strip())


concat('Python', 'cool')
concat('Python', 'cool', 2)
concat('Python', 'cool', 2, True)
concat('Python', 'cool', 2, True, False)

"""
Declaring
Parameters
Restricting parameters data type
Setting default value to parameters
Restricting the return type
"""
