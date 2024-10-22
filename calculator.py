''' Python lab
Name: Eugenie Tsafack
Date: 10/21/2024
File name: calculator.py
1- Write a calculator program 
2- Your code will provide 2 numbers (integer or float) and the user will select what type of operation needed.

'''

# define a calculator function

def calculator():
    # asking to a user to provide two number
    num1 = int(input("enter a number\t"))
    num2 = float(input("enter another number\t"))
    
    # asking to a user to choose the operation
    print("+ = Addition")
    print("- = Subtraction")
    print("* = Multiplication")
    print("/ = Division")
    operation = input("Please choose the symbol of the operation you want (+, -, *, /)\t")
    
    
    if operation == "+":
        result = num1 + num2
        print(f"The result of addition is: {result}")
        
    elif operation == "*":
        result= num1 * num2
        print(f"The result of multiplication is: {result}")
        
    elif operation == "-":
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
        
    elif operation == "/":
        
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division is: {result: .3f}")
            
        else:
            print("Error! Division by Zero is not allowed!!")
    else:
        print("Invalid operation!!!")
        
# calling the calculator function
calculator()