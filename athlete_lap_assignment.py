''' Python program
Name: Eugenie Tsafack
Date: 10/15/2024
File name: athletes.py
objective: Practice using loops to iterate through a list and display information.
Task: Write a python program that uses a list of four U.S women athletes who have completed in the 400 meters at the olympics.
'''

athletes = ["Allyson Felix", "Sanya Richards-Ross", "Shaunae Miller-Uibo", "Phyllis Francis"]

for index in range(len(athletes)):
    print(f"Lap {index + 1}: {athletes[index]} has completed their lap!")

print("All athletes have completed their laps!") 