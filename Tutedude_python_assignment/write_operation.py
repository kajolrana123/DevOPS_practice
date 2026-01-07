# Que 3. Write to a File
# Write a program to create a text file and write some content to it.

file = open("example.txt", "w")   # Open file in write mode
file.write("Hello, this is a sample text file.\n")
file.write("This file was created using Python.\n")
file.write("File handling is easy!")
file.close()

print("Content written to file successfully.")

