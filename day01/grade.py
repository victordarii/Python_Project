grade = 'A'

result = None

if grade == 'A' or grade == 'B' or grade == 'C' or grade == 'D' or grade == 'F':
    if grade == 'A':
        result = 'Excellent'
    elif grade == 'B':
        result = 'Great job'
    elif grade == 'C':
        result = 'Good'
    elif grade == 'D':
        result = 'Passed'
    else:
        result = 'Failed'
else:
    result = 'Invalid grade'

print(result)
