'''Python lab
# Student Name: Eugenie Tsafack
# date: 10/2/2024
# Write a program that will ask user for a number than check whether that number is EVEN or ODD.
'''

user_number = int(input("Please enter a number between 1-100 \t "))

if user_number % 2 == 0 :
    print (f"Your number {user_number} is an even number.")
    
else :
    print (f"Your number {user_number} is an odd number")