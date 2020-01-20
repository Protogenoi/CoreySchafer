
language = 'Python'

print('-----Basic if, elif and else-----')
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is Java')
else:
    print('No Match')

if True:
    print('Conditional was True')

print('-----Check if user is admin and is logged in-----')
user = 'Admin'
loggedIn = True

if user == 'Admin' and loggedIn:
    print('Admin Page')
else:
    print('Bad Creds')

print('-----Test if two objects have the same ID in memory-----')
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(id(a))
print(id(b))
print(a is b)
print(a is c)

print('-----False Values-----')

condition = None
condition2 = False
condition3 = 0
condition4 = []  # Empty list
condition5 = {}  # Empty mapping (Dictionary)

if condition:
    print('Evaluated to True')
elif condition2:
    print('Evaluated to True')
elif condition3:
    print('Evaluated to True')
elif condition4:
    print('Evaluated to True')
elif condition5:
    print('Evaluated to True')
else:
    print('Evaluated to False')



