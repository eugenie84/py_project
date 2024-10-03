''' Python lab
# Student Name: Eugenie Tsafack
# date: 10/2/2024
# Write a program that will ask a student for a their grade in 5 subjects and calculate their average grade
'''
# define a variable subject
subj1 = int(input("Enter your grade in Math 145 \t"))
subj2 = int(input("Enter your grade in Psych \t"))
subj3 = int(input("Enter your grade in Java 102 \t"))
subj4 = int(input("Enter your grade in Eng 101 \t"))
subj5 = int(input("Enter your grade in Python 102 \t"))

# calculate the average grade
average_grade = sum({subj1, subj2, subj3, subj4, subj5}) / 5

# range of grade
print(f"Your average grade is {average_grade: .2f}")
if average_grade > 90:
    print("Your grade is A")
elif average_grade > 80:
    print("Your grade is B")
elif average_grade > 70:
    print("Your grade is C")
elif average_grade > 60:
    print("Your grade is D")
else:
    print("Your grade is E === Failed")
