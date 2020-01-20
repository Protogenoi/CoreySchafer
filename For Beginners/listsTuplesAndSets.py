# Lists can be changed and are mutable
print('-----Lists-----')

courses = ['English', 'History', 'Math', 'Physics']
courses2 = ['Art', 'Education']
nums = [1, 5, 4, 3, 2]

print(courses)

# Return second index
print(courses[1])

# Return last index
print(courses[-1])

# Return a range
print(courses[:2])
print(courses[2:4])

# Add item to list

courses.append('Gym')
print(courses)

courses.insert(0, 'Geography')
print(courses)

# Merge two lists together
courses.extend(courses2)
print(courses)

# Remove values from a list
courses.remove('Math')
print(courses)

# Remove last value from a list
popped = courses.pop()
print(popped)
print(courses)

# Sort a list
print('-----Sort a list-----')

# This wont alter the original courses
sortedCourses = sorted(courses)
print(sortedCourses)

courses.reverse()
print(courses)

courses.sort()
print(courses)

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))

# Find the index
print(courses.index('Gym'))

print('Gym' in courses)
print('Drama' in courses)

print('-----Loop through courses-----')
for item in courses:
    print(item)

# Get index from list
print('-----Get index-----')
for index, item in enumerate(courses):
    print(index, item)

# Start at 1 instead of zero
print('-----Start at 1-----')
for index, item in enumerate(courses, start=1):
    print(index, item)

# Comma separated values
print('-----Comma separated-----')
courseStr = ', '.join(courses)
print(courseStr)

# Convert back to a list
newList = courseStr.split(', ')
print(newList)

print('-----Sets-----')

csCourses = {'History', 'Math', 'Physics', 'Gym'}
print(csCourses)

print('-----Return matches in csCourses-----')
artCourses = {'History', 'Math', 'Art', 'Design'}
print(csCourses.intersection(artCourses))
print('-----Return differences in csCourses-----')
print(csCourses.difference(artCourses))
print('-----Join both sets and combined-----')
print(csCourses.union(artCourses))

print('-----Tuples-----')
# Tuples cannot be modified and are immutable

tuple1 = ('History', 'Math', 'Physics', 'History')
tuple2 = tuple1

print(tuple1)
print(tuple2)

# This won't work because a tuple is immutable
# tuple1[0] = 'Art'

# print(tuple1)
# print(tuple2)

# Empty Lists

emptyList = []
emptyList = list()

# Empty Tuples

emptyTuple = ()
emptyTuple = tuple()

# Empty Sets

emptySet = {}  # This isn't right! It's a dict
emptySet = set()
