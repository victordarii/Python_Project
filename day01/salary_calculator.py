name = input("Enter your name\n")
hourly_rate = float(input("Enter your hourly rate\n"))
weekly_hours = float(input("How many hours you work in a week?\n"))

salary = hourly_rate * weekly_hours * 52

print(f'Hello {name}, your salary is $ {salary}')
