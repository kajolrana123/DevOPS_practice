# Que 4. Read from a File
# We used open in read mode and file.read to read and print to display.

file = open("example.txt", "r")   # Open file in read mode
read = file.read()                # reading the whole file content
print(read)                       # print the content in the console
file.close()

