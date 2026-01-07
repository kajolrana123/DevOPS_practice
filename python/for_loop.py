numbers = [1,2,3,4,5,6]

for i in numbers:
    print(i)

# or

for i in numbers:
    if i == 1:
        print('one')
    elif i == 2:
        print('two')
    elif i == 3:
        print('three')
    else:
        print('other')

# or

num = range(10)
print(num)

# or

list = list(range(10))
print(list)

for i in list:
    if i == 1:
        print('one')
    elif i == 2:
        print('two')
    elif i == 3:
        print('three')
    else:
        print('other')

# or
for i in range(5):
    if i == 1:
        print('one')
    elif i == 2:
        print('two')
    elif i == 3:
        print('three')
    else:
        print('other')
