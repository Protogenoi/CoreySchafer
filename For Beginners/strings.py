greeting = 'Hello'
name = 'Michael'

# Using placeholders instead of concatenation

message = '{}, {}, Welcome!'.format(greeting, name.upper())

# Using f strings instead

message2 = f'{greeting}, {name.upper()}, Welcome!'

print(message)
print(message2)
