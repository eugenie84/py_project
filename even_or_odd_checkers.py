'''Python lab
Name: Eugenie Tsafack
Date: 10/21/2024
File name: even_or_odd_checkers.py
# Write a program that will ask user for a number and check whether that number is EVEN or ODD.

'''
# Define a function checker
def even_odd (number):
    result = number % 2
    

    if result == 0 :
        print (f"Your number {number} is an even number.")
    
    else :
        print (f"Your number {number} is an odd number")
        
# main program and Calling a function 
        
user_number = int(input("Please enter a number between 1-100 \t "))

if 1 <= user_number <= 100:
    even_odd(user_number)
else:
    print("The  number you enter is not in a range of numbers authorized to be checked")
