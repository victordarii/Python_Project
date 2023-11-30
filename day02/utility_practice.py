import numbers


def display_message():
    print('Hello Wisconsin')
    print('Hello World')


def square(num):
    return num * num


def divide(num1, num2):
    return num1 / num2


def square2(num: int):  # now to avoid error we must give only the required type nothing else
    return num * num  # because we are restricted to an int argument


def add(num1: int, num2: int) -> int:
    return num1 + num2


def addition(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2


def sum_numbers(n1: numbers, n2: numbers, n3: numbers = 0,
                n4: numbers = 0) -> numbers:  # this is a function(not under class)
    return n1 + n2 + n3 + n4


def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}'.strip())
