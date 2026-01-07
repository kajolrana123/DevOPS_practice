import datetime

current_time = datetime.datetime.now()

print(current_time)

# or
# datetime is module inside that datetime is a function

from datetime import datetime

show_time = datetime.now()

print(show_time)


from math import sqrt
num = int(input("enter the number to find the square root "))
print("square root of ", num , " is ", sqrt(num))
