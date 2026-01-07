def hello_world():
    print("HI Good Morning !")

def add_two_number(a):
    print("Enter a number to add ")
    b = int(input())
    c = a + b
    return c

hello_world()
d = add_two_number(5)
print(d)