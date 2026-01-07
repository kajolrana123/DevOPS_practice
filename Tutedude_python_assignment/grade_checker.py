# Que 1 Grade Checker using if-else statement

marks = int(input("HI, enter your marks "))

if marks >= 90:       # marks 90+ grade 'A'
    grades = 'A'
    print("nice dude good job")
elif marks >= 80:     # any marks between 80-89 grade 'B'
    grades = 'B'
    print("Good job")
elif marks >= 70:     # any marks between 70-79 grade 'C'
    grades = 'C'
    print("Do better")
elif marks >= 60:     # any marks between 60-69 grade 'D'
    grades = 'D'
    print("Okaish")
else:
    grades = 'F'
    print("study hard")

print("your grades is ", grades)