# Python lab
# Student Name: Eugenie Tsafack
# date: 10/2/2024
# Prompt the user to enter their age as an integer and categorize the person into one of the life stage

user_age = int(input("Please enter your age \t"))
if 0<= user_age and user_age <= 1:
    print("You are an Infant")
    
elif 2<= user_age and user_age <= 3:
    print("You are a Toddler")
    
elif 4<= user_age and user_age <= 12:
    print("You are a Child")
    
elif 13<= user_age and user_age <= 19:
    print("You are a Teenager")
    
elif 20<= user_age and user_age <= 64:
    print("You are a Adult")
    
elif 65 <= user_age and user_age <= 116:
    print("You are a Senior")
    
else: 
    print("Invalid age")
