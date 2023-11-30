# Arithmetic operators + - * / %

print(10 - 2)
print(3 + 4)
print(6 * 4)

# Division operator works different from Java by always returning float number
print(10 / 3)  # Python result is: 3.33 Java would give an int 3

print(10 / 2)  # returns float number also

print(10 % 3)

print(100 / 2)
print(int(100 / 2))

# Shorthand assignment operators  =  +=  -=  *=  /=  %=

a = 100
a = 200

print(a)

a += 100
print(a)

a -= 50
print(a)

a /= 2
print(a)

print(type(a))

print("------------------------------")

a = int(a)
print(a)
print(type(a))

# Relational operators  >  >=  <  <=  ==  !=

print("------------------------------")
# Logical operators:  and, or, not

s = 'Hello World'

print('H' and 'W' in s)  # similar to Java's contains()

print(True and True)  # similar to Java's &&
print(True or False)  # similar to Java's ||

s = 'Java Python C# C++'

print('Java' or 'Ruby' in s)

print("------------------------------")

age = 2
citizen = 'USA'

is_eligible = (age >= 18 and citizen == 'USA')
is_eligible2 = ((age >= 18) and (citizen == 'USA'))

print(is_eligible)
print(is_eligible2)

print("------------------------------")
s = 'Java Python C# C++'
has_java = 'Java' in s
print(has_java)

print('Python' not in s)

print('Ruby' not in s)  # prints True because there is no 'Ruby' inside str s

print(not True)
print(not False)

print("------------------------------")

# Identity operators: is     Returns true if both operands are the same obj
#                     is not Returns true if both operands are Not the same obj

s1 = 'Java'
s2 = 'Java'

print(s1 is s2)  # if two var are referencing to the same obj ( == operator of Java)

print("------------------------------")

s11 = 'Hello World!'
result = 'z' not in s11 and 'x' not in s11
print(result)  # True
