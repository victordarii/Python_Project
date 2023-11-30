grade_level_number = int(input('Enter your grade level number\n'))

school_type = None

if grade_level_number >= 17 and grade_level_number <= 18:
    school_type = 'Grad School'
elif grade_level_number >= 13 and grade_level_number <= 16:
    school_type = 'College'
elif grade_level_number >= 9 and grade_level_number <= 12:
    school_type = 'High school'
elif grade_level_number >= 6 and grade_level_number <= 8:
    school_type = 'Middle school'
elif grade_level_number >= 1 and grade_level_number <= 5:
    school_type = 'Elementary school'
else:
    print("Invalid grade level number! Available grade levels are 1-18")

print(school_type)
