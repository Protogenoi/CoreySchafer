
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Gym']}

print(student)
print(student['name'])
print(student['courses'])

# Get will return None instead of a error in the key pair value is not found
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

print('-----Update Student Name-----')
student['name'] = 'Sally'
print(student['name'])

student.update({'name': 'Mikey', 'age': 32, 'phone': '07401434619'})
print(student)

# Delete specific key and its value
print('-----Delete key and value-----')
age = student.pop('age')  # del student['age']
print(student)
print(age)

# Find how many keys a dictionary has
print('-----Find keys in dictionary-----')
print(len(student))
# Find values in dictionary
print('-----Print values in dictionary-----')
print(student.values())
# Return keys and values
print('-----Print keys and values-----')
print(student.items())

# Loop through keys and values
print('-----Loop through keys and values-----')
for key, value in student.items():
    print(key, value)

