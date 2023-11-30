# name = 'John'
# age = 22
# gender = 'Male'
# company = 'Ginger Snaps'
# job_title = 'Automation Developer'
# years_of_experience = 5
# salary = 10700.5
# is_full_time = True
# is_married = False
# employee_id = 'r100'

name = input('Enter name\n')
age = input('Enter age\n')
gender = input('Enter gender\n')
company = input('Enter company\n')
job_title = input('Enter job title\n')
salary = input('Enter salary\n')

print(f'{name} is {age} years old, gender is {gender}'
      f'\n{name} works at {company} as a {job_title}'
      f'\n{name} makes $ {salary} per year')
