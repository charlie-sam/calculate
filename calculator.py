print('''
a - add
b - sub
c - mul
d - div
''')

def x():
    if operation == 'a':
         return "+"
    elif operation == 'b':
         return "-"
    elif operation == "c":
         return "*"
    elif operation == "d":
         return "/"
while True:
    again = (input("Do you want to perform operation(y/n): "))
    if again == 'n':
        break

    elif again == 'y':

        operation = (input("which operation do you perform > "))

        a = int(input("enter your first value > "))
        b = int(input("enter your second value > "))
            
        if operation == 'a':
            c = (a+b)
        elif operation == 'b':
            c = (a-b)
        elif operation == 'c':
            c = (a*b)
        elif operation == 'd':
            c = (a/b)     
        print("your ans =:",a, x(), b,'=',c )