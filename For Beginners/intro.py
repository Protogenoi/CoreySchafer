# import my_module.py
from my_module import find_index, test
# from my_module import find_index as fi, test
import sys
# Paths can be specified like
# sys.path.append('/home/michael/PycharmProjects/example')
# Or with environmental variables
# mac - /Users/USER/.bash_profile - export PYTHONPATH="/home/michael/PycharmProjects/example"
#

import random
import math
import datetime
import calendar
import os

courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)

print(random_course)

index = find_index(courses, 'Math')
# index = fi(courses, 'Math')
print(index)
print(test)

print(sys.path)

rads = math.radians(90)

print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

# Prints current working directory
print(os.getcwd())
# Prints current file location
print(os.__file__)
