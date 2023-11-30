if False:
    print('Python Hello')

print('Java hello')

print('-----------------------------------------------')

score = 70
if score >= 60:
    print('Congrats! You passed the exam')

s = 'Hello World'

if 'H' and 'W' in s:
    print(s, 'has H and W')

print('-----------------------------------------------')

if score >= 60:
    print('Passed')
else:
    print('Failed')

print('-----------------------------------------------')

age = 20
result = None

if age >= 21:
    result = 'Eligible'
else:
    result = 'Not eligible'

print(result)

print('-----------------------------------------------')

# Ternary

age = 2
result = 'Eligible' if age >= 21 else 'Not eligible'
# similarly in Java --> String result = (age >= 21) ? "Passed" : "Failed";
# A value is assigned depending on the condition
#  give as many else as needed

print(result)

print('-----------------------------------------------')

# if we have more than two condition we use multi-branch if - same as Java

num = 10
result = None

if num > 0:
    result = 'Positive'
elif num < 0:
    result = 'Negative'
else:
    result = 'Zero'

print(result)

print('-----------------------------------------------')

num = -200

# based on the given number num=200 assign a value to result2 accordingly
result2 = 'Positive' if num > 0 else 'Negative'

print(result2)

print('-----------------------------------------------')

score = 10

if 0 < score <= 100:

    if score >= 60:
        print('Passed')
    else:
        print('Failed')
else:
    print('Invalid Score')

print('-----------------------------------------------')

score = 79

if 0 <= score <= 100:
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')
else:
    print('Invalid score')
