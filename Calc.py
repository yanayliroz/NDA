import random
import math
running = True  
def main_program():
    def addition(a,b):
        return a+b 
    def substraction(a,b):
        return a-b
    def multiplication(a,b):
        return a*b
    def division(a,b):
        return a/b
    def power(a,b):
        return a**b
    def squareroot(a):
        return math.sqrt(a)
    def factorial(a):
        return math.factorial(a)

    # Command Line Interface
    print("Select operation.")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exponentiation")
    print("6.Square root")
    print("7.Factorial")


    choice = input("Enter choice(1/2/3/4/5/6/7)")

    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1,"+",num2,"=", addition(num1,num2))

    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1,"-",num2,"=", substraction(num1,num2))

    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1,"*",num2,"=", multiplication(num1,num2))

    elif choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1,"/",num2,"=", division(num1,num2))

    elif choice == '5':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1,"**",num2,"=", power(num1,num2))

    elif choice == '6':
        num = float(input("Enter a number: "))
        print("The square root of",num,"is",squareroot(num))

    elif choice == '7':
        num = float(input("Enter a number: "))
        print(num,"!=",factorial(num))


#while loop user input
while running:
    main_program()
    restart =input("Do you want to continue? (yes/no): ")
    if restart.lower() == 'yes' or restart.lower() == 'y':
        running = True
    elif restart.lower() == 'no' or restart.lower() == 'n':
        running = False
        
#fuck lo asinu branch hakol bamain