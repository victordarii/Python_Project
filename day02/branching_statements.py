for each in range(1, 6):
    print(each)
    if each == 3:
        break

print("-----------------------------------------")

for each in range(1, 6):
    if each == 3 or each == 4:
        continue
    print(each)

print("-----------------pass statement for achieving abstraction in Python------------------------")
# hiding the implementation details of a function
# So in Python to create a method without body/implementation is by declaring it with pass keyword inside it



