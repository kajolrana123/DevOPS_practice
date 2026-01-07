#=======================================
f = open('data.txt', 'r')  # 'r' read mode

data = f.read() # read and print the whole file content

print(data)

f.close()

#=========================================
f = open('data.txt', 'r')

lines = f.readlines() # print all lines with \n

print(lines)

f.close()

#=========================================
f = open('data.txt', 'r')

line = f.readline() # read and print only first line

print(line)

f.close()

#=====================================
f = open('data.txt', 'r+')  # 'r+' read and write mode

read = f.readlines()
# print(read)

f.write("I am from uttarakhand")
r_write = f.read()
print(r_write)

f.close()