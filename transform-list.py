'''Python program
Name: Eugenie Tsafack
Date: 10/16/2024
File name: transform-list
Task: Write a program that will transform the initial list ["3, BaNanA", "2, ApplE", "4,Orange", "2,ApplE", "10,Grape", "1,CherrY", "3, banana", "10,Grape"] to the final list [1,CHERRY
2,APPLE
2,APPLE
3,BANANA
3,BANANA
4,ORANGE
10,GRAPPE
10,GRAPPE]
'''
# create a list
lists= ["3, BaNanA", "2, ApplE", "4,Orange", "2,ApplE", "10,Grape", "1,CherrY", "3, banana", "10,Grape"]

# Writing a loop for the lists
for thing in lists:
    print(thing)

# removed space, split the string and convert to uppercase

new_lists = []

for thing in lists:
    number, fruit = thing.split(',')
    new_lists.append((int(number.strip()), fruit.strip().upper()))

#sort the new list
new_lists.sort()
    
# loop in the new_list

for number, fruit in new_lists:
    print(f"\n {number},{fruit}")
    
    