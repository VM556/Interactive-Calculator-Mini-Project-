#This Program Is an Interactive Calculator
import math
import random
import turtle

#This Function Adds Two Numbers
def add(x, y):
    return x + y

#This Function Subtracts Two Numbers
def subtract(x, y):
    return x - y

#This Function Multiplies Two Numbers
def multiply(x, y):
    return x * y

#This Function Divides Two Numbers
def divide(x, y):
    return x / y

#This Function Evaluates the Exponent of a Number
def expo(x, y):
    return x**y

#This Function Squares a Number
def square(x):
    return x*x

#This Function Cubes a Number
def cube(x):
    return x*x*x

#This Function Finds the Cube root of the input
def cbrt(x):
    return x**(1/3)

#This is the turtle code for the ending
def t():
    win = turtle.Screen()
    rootwindow = win.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
    win.bgcolor("black")
    win.title("See You Soon...")
    turtle.color('#ffd700')
    style = ('Arial', 80)
    turtle.write('Goodbye! :)', font=style, align='center')
    turtle.hideturtle()

superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")



# This Function Defines the Index of the Program
def index():
    print("Select your Operation:", end='\n\n')
    print("0. Index")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    print(" 5.1. Square")
    print(" 5.2. Cube")
    print("6. Square Root")
    print("7. Cube Root")
    print("8. Factorial")
    print("9. Generate Random Number")
    print("10. Generate Random List", end='\n\n')

#The Program Starts Here
index()

while True:
    #Gets Two inputs From the User
    choice = input("Enter Choice-[ 0{INDEX}|1|2|3|4|5|5.1|5.2|6|7|8|9|10 ]: ")
    print("") #Blank Line

    #Checks Whether the Choice is True 
    if choice in ('1', '2', '3', '4',):
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        if choice == '1':
            print("")
            print(num1, "+", num2, "=", add(num1, num2), end='\n\n')

        elif choice == '2':
            print("")
            print(num1, "-", num2, "=", subtract(num1, num2), end='\n\n')

        elif choice == '3':
            print("")
            print(num1, "x", num2, "=", multiply(num1, num2), end='\n\n')

        elif choice == '4':
            print("")
            print(num1, "÷", num2, "=", divide(num1, num2), end='\n\n')

        
        #Confirms if the User Wants To Repeat The Program 
        print("") #Blank Line
        confirm = input("Wanna Calculate Something Else? ¯\_(ツ)_/¯ (Click ENTER to Continue ... Type 'NO[N/n]' to EXIT Program): ")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        if confirm == "n" or confirm =="N" or confirm =="no" or confirm =="NO" or confirm == "No":
            print("--------------- --------------- --------------- --------------- --------------- ---------------")
            t()
            break
        
    #Since The two inputs are changed to base and power
    elif choice == ('5'):
        num1 = int(input("Enter Base: "))
        num2 = int(input("Enter Power: "))
        numstr = str(num2)
        print("")
        print(num1, numstr.translate(superscript), " = ", expo(num1, num2), sep="", end='\n\n')#replace(num1, num2))

        confirm = input("Wanna Calculate Something Else? ¯\_(ツ)_/¯ (Click ENTER to Continue ... Type 'NO[N/n]' to EXIT Program): ")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        if confirm == "n" or confirm =="N" or confirm =="no" or confirm =="NO" or confirm == "No":
            print("--------------- --------------- --------------- --------------- --------------- ---------------")
            t()
            break

    #Since Only one Value is Required for this Function    
    elif choice == ('5.1'):
        num1 = int(input("Enter Number: ") )
        pow2 = str("2") 
        print("")
        print(num1, pow2.translate(superscript), " = ", square(num1), sep="", end="\n\n")

        confirm = input("Wanna Calculate Something Else? ¯\_(ツ)_/¯ (Click ENTER to Continue ... Type 'NO[N/n]' to EXIT Program): ")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        if confirm == "n" or confirm =="N" or confirm =="no" or confirm =="NO" or confirm == "No":
            print("--------------- --------------- --------------- --------------- --------------- ---------------")
            t()
            break
    #Here the input value is cubed
    elif choice == ('5.2'):
        num1 = int(input("Enter Number: ") )
        pow3 = str("3") 
        print("")
        print(num1, pow3.translate(superscript), " = ", cube(num1), sep="", end="\n\n")
        
        confirm = input("Wanna Calculate Something Else? ¯\_(ツ)_/¯ (Click ENTER to Continue ... Type 'NO[N/n]' to EXIT Program): ")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        if confirm == "n" or confirm =="N" or confirm =="no" or confirm =="NO" or confirm == "No":
            print("--------------- --------------- --------------- --------------- --------------- ---------------")
            t()
            break

    #Calculates The Square Root by importing Math Tool 
    elif choice == ('6'):
        num1= float(input("Enter a Number: "))
        print("√", num1, " = ", round(math.sqrt(num1), 4), sep="")
        
        print("") 
        confirm = input("Wanna Calculate Something Else? ¯\_(ツ)_/¯ (Click ENTER to Continue ... Type 'NO[N/n]' to EXIT Program): ")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        if confirm == "n" or confirm =="N" or confirm =="no" or confirm =="NO" or confirm == "No":
            print("--------------- --------------- --------------- --------------- --------------- ---------------")
            t()
            break
    #Calculates The Cube Root
    elif choice == ('7'):
        num1= float(input("Enter a Number: "))
        print("∛", num1, " = ", round(cbrt(num1), 4), sep="")
        
        print("") 
        confirm = input("Wanna Calculate Something Else? ¯\_(ツ)_/¯ (Click ENTER to Continue ... Type 'NO[N/n]' to EXIT Program): ")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        if confirm == "n" or confirm =="N" or confirm =="no" or confirm =="NO" or confirm == "No":
            print("--------------- --------------- --------------- --------------- --------------- ---------------")
            t()
            break


    #Calculates The Factorial by importing Math Tool 
    elif choice == ('8'):
        num1 = int(input("Enter the Number: ")) 
        print(num1, "!", " = ", math.factorial(num1), sep="")

        print("") 
        confirm = input("Wanna Calculate Something Else? ¯\_(ツ)_/¯ (Click ENTER to Continue ... Type 'NO[N/n]' to EXIT Program): ")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        if confirm == "n" or confirm =="N" or confirm =="no" or confirm =="NO" or confirm == "No":
            print("--------------- --------------- --------------- --------------- --------------- ---------------")
            t()
            break

    #Generates Random Number by importing Random Tool 
    elif choice == ('9'):
        n = random.randint(0, 101)
        print("Randomly Generated Number", "=", n)

        print("") 
        confirm = input("Wanna Calculate Something Else? ¯\_(ツ)_/¯ (Click ENTER to Continue ... Type 'NO[N/n]' to EXIT Program): ")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        if confirm == "n" or confirm =="N" or confirm =="no" or confirm =="NO" or confirm == "No":
            print("--------------- --------------- --------------- --------------- --------------- ---------------")
            t()
            break
        
    #Generates Random List between 0 to 100 by importing Random Tool 
    elif choice == ('10'):
        randomlist = [random.randint(0,101) for i in range(5)]
        print("Randomly Generated List", "=", randomlist)

        print("") 
        confirm = input("Wanna Calculate Something Else? ¯\_(ツ)_/¯ (Click ENTER to Continue ... Type 'NO[N/n]' to EXIT Program): ")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        print("--------------- --------------- --------------- --------------- --------------- ---------------")
        if confirm == "n" or confirm =="N" or confirm =="no" or confirm =="NO" or confirm == "No":
            print("--------------- --------------- --------------- --------------- --------------- ---------------")
            t()
            break
    
    #Refers back to the index for user Convenience
    elif choice == ('0'):
        index()

    #If input is Invalid, this is an error
    else:
        print("Error, Invalid Input!  o_O  .....!!!!!.....!!!!!.....!!!!!.....!!!!!.....!!!!!.....!!!!!..... ", end='\n\n')

