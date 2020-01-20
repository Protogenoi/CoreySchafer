
nums = [1, 2, 3, 4, 5]

# Using break
print('-----Break-----')
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

# Using continue
print('-----Continue-----')
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

# Loop in a loop
print('-----Loop within a Loop-----')
for num in nums:
    for letter in 'abc':
        print(num, letter)

# Run through a loop X times
print('-----Run through a loop 10 times-----')
for i in range(1, 11):
    print(i)

# While loops will run until a break or a condition is met
print('-----While loops-----')
x = 0
y = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

print('-----While True-----')
while True:
    if y == 5:
        break
    print(y)
    y += 1
