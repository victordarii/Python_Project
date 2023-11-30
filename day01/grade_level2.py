grade_level_number = int(input('Enter your grade level number\n'))

result = None

if 1 <= grade_level_number <= 18:
    if 1 <= grade_level_number <= 5:
        result = 'Elementary school'
    elif 6 <= grade_level_number <= 8:
        result = 'Middle school'
    elif 9 <= grade_level_number <= 12:
        result = 'High school'
    elif 13 <= grade_level_number <= 16:
        result = 'College'
    else:
        result = 'Grad School'
else:
    result = 'Invalid grade level given'

print(result)

"""
14. Create a python file named grade_level2.  write a program that asks user to enter the grade level number,  determine and print which school type the person is in is in.
            grade level and types are:
                    1-5: Elementary school 
                    6-8: Middle school
                    9-12: High school
                    13-16: College
                    17-18: Grad School
                    
                    For Any Other grade: Invalid grade level given

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""
