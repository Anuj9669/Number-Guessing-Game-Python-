def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
    
print("Welcome to The Calculator")
while True:
 print("MENU\n1.Addition\n2.Subtraction\n3.Multiply\n4.Division\n\n5.Exit")
 a = float(input("Enter 1st number:"))
 b = float(input("Enter 2nd number:"))
 x = int(input("Please input your choice!"))

 if x == 1:
    print("Sum =", sum(a,b))
 elif x == 2:
    print("Subtraction =", sub(a,b))
 elif x == 3:
    print("Multiplication =", mul(a,b))
 elif x == 4:
    print("Division =", div(a,b))
 elif x==5:
    print("Thank you for using this calculator!")
    break
 else:
    print("Invalid choice, please choose again!")
