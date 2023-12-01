# class Employee:
#
#     def __init__(self):
#         self.name = None
#         self.job_title = None
#         self.salary = None
#
# # create an obj then print its name attribute
# employee1 = Employee()
# print(employee1.name)  # prints None


# to print some other value we need to create a parameterized constructor that will take a value for that name

# class Employee:
#
#     def __init__(self, name, job_title, salary):
#         self.name = name
#         self.job_title = job_title
#         self.salary = salary
#
#
# # Now when we create an object of this class we are forced to initialize those attributes
#
# employee1 = Employee('John', 'Developer', 100000)
#
# print(employee1.name)  # prints 'John'


# ------------------------------------------------------------------------------------------------

# restrict the type of values that will be stored into those attributes
import numbers


class Employee:
    is_human = True

    def __init__(self, name: str = 'Unknown', job_title: str = 'Unknown', salary: numbers = 0):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f'{self.name} is fucking working!')

    # def __str__(self):
    #     return f'name: {self.name}, job_title: {self.job_title}'

    # easier way:
    def __str__(self):
        return f'{type(self).__name__}: {self.__dict__}'


print('------------------------------------------------------------')

employee1 = Employee()

print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

print('------------------------------------------------------------')

employee2 = Employee("Victor")

print(employee2.name)
print(employee2.job_title)
print(employee2.salary)

print('------------------------------------------------------------')

employee3 = Employee("John", 'Doctor')

print(employee3.name)
print(employee3.job_title)
print(employee3.salary)

print('------------------------------------------------------------')

employee4 = Employee("Alex", 'Driver', 90000)

print(employee4.name)
print(employee4.job_title)
print(employee4.salary)
print('------------------------------------------------------------')

# print(Employee.name)
print(Employee.is_human)

print(employee1)
print(employee2)
print(employee3)
print(employee4)
