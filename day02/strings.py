name = 'Python'

print(len(name))

print(name[0])

print(name[len(name) - 1])
print(name[-1])

s = 'Java programming language'

print(s[5:16])
print(s[:16])
print(s[5:])

print('-----------------------------------------------------------')

h = 'Python'
print(h)

h2 = str(reversed(h))
print(h2)

print('-----------------------------------------------------------')

d = 'Python'
d2 = str(d[::-1])
print(d2)

print(reversed(d2))
print('------------------str methods-----------------------------------------')

word = 'python lang'
word = word.capitalize()  # capitalizes the first letter
print(word)

print('--------------------title()---------------------------')

name = 'vasile iepureanu i cimislia md i ababa'
name = name.title()

print(name)

print('---------------------strip() lstrip() rstrip() similar to trim() in Java-------------------')

book1 = '   Smelly Cat   '
book2 = '   Smelyy Dog   '
book3 = '   Smelly Joe   '

book1 = book1.strip()
book2 = book2.lstrip()
book3 = book3.rstrip()

print(book1)
print(book2)
print(book3)

print('------------------------index() rindex() ------------------------------')

p = 'Java'

print(p.index('a'))
print(p.rindex('a'))

p = p.index('a')

print(type(p))
print('------------------------replace() ------------------------------')

s = 'Java Java Ruby'
s = s.replace('Java', 'Python')  # replaces all 'Java' with 'Python'
print(s)

s = 'Java Java Java Ruby'
s = s.replace('Java', 'Python', 1)  # only replace first 'Java'
print(s)

s = 'Java Java Java Ruby'
s = s.replace(' Java', ' Python', 1)  # only replace the uniquely identified ' Java' with a space
print(s)

print('------------------------ count() ------------------------------')

s = 'jAva Java Java Java Python Python'

count_Java = s.count("Java")
print(count_Java)
print(s.count('Python'))

# ignore case sensitivity to count all 'jaVa'
all_Javas = s.lower().count('java')
print(all_Javas)

print('------------------------ ignore case sensitivity ---------------')

s1 = 'java'
s2 = 'JAVA'

print(s1 == s2)
print(s1.lower() == s2.lower())

print('------------------------ islower() isupper() ---------------')

s = 'Java'

print(s.islower())  # checks if all characters are lower case
print(s[0].islower())  # checks only given character at that specific index whether it's lower case or not

print('------------------------ isalpha() isdigit() ---------------')

s = 'a'
print(s.isalpha())

s = '1'
print(s.isdigit())

i = 10
# print(i.isdigit())  # gives error since we cannot call a str method from an integer

print('------------------------ istitle() ---------------')

s = 'Java Bad'
print(s.istitle())

s = 'java Bad'
print(s.istitle())
