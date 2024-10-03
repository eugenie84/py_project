'''Python lab
Eugenie Tsafack
date: 10/2/2024
max-min-values.py

Write a python program that print the largest and smallest values in a list
Print the two values on the same line, separated by a space
The largest value should appear first and the smallest value should appear second
You may assume that the list only contains numeric values.
if the list is empty, print none.
'''
# define a list of numeric values
#list = [0, 10, 3, 45,91,87,2,7]
#list = [-1, -2, -3, -4]
#list = [0, 0, 0, 0]
list = []



if len(list) != 0:
    largest = max(list)
    smallest = min(list)
    print(f"{largest} {smallest}")

else:
    print(list, "None")

    