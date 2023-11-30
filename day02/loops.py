s = 'Python'

for each in s:
    print(each)

print('----------------------------')

# popular function is range() - often used to specify the number of iterations for loop (similar to fori in Java)

for each in range(1, 10):
    print(each)
print('----------------------------')
for each in range(0, len(s)):
    print(each)
    print(s[each])

print('----------------------------')

for each in range(-len(s), 0):
    print(each)

print('------------reverse----------------')

for each in reversed(range(0, len(s))):  # stupid
    print(s[each])

print('------------reverse2----------------')

word = 'Python'
result = ""

for each in reversed(word):
    result += each

print(result)

# if you need access to the index values you need to create a range of values --> range()
print('------------- while loop ---------------')

# for whatever reason I only need a positive number form the user nothing else
num = int(input('Enter a positive number:\n'))

while num > 0:
    print('Precious')
    # some other code

    # finally to exit this while loop I will ask user to enter a positive number to do something else
    # or user can give a negative number to exit the while loop since he is ready to proceed with further code
    num = int(input('Enter a positive number to continue or a negative number to exit the while loop\n'))

print(f'You have entered {num}')

# some code here using that positive number from the user
