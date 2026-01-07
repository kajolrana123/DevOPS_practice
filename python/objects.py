a = [1,2,3,4,5,6,7,8,9,10]  #list
b = (1,2,3,4,5,6,7,8,9,10)  #tuples
c = {1,2,3,4,5,6,7,8,9,10}  #set
d = {'a':1,
     'b':2,
     'c':3,
     'd':4,
     'e':5,
     'f':6
    }  #dictionary
convert = { 1 :'one',
            2 :'two',
            3 :'three',
            4 :'four',
            5 :'five',
            6 :'six'
            }
convert[7] = 'seven'

#the main difference between list and tuples
# tuples value can't be change

# b[3] = 10 --> not allowed

print(a)
print(b)
print(c)
print(d)
print(convert[2])
print(convert[3])
print(convert[4])
print(convert[7])
print(convert)

del(convert[2])
print(convert)