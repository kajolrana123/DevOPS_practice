marks = int(input("HI, enter your marks "))

if marks >= 90:
    grades = 'A'
    print("nice dude good job")
elif marks >= 80:
    grades = 'B'
    print("Good job")
elif marks >= 70:
    grades = 'C'
    print("Do better")
elif marks >= 60:
    grades = 'D'
    print("Okaish")
else:
    grades = 'F'
    print("study hard")

print("your grades is ", grades)