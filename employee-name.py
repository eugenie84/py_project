

'''Python program
student name: Eugenie Tsafack
date: 10/4/2024
file name: english-french-translator.py

Instructions: 
- Print out the last name of the second employee.
- please search through the dictionary below
- search for the name "Alexandra"

'''

# given dictionary for the research

d = {"employees": [
        {"firstName": "John", "lastName": "Doe"},
        {"firstName": "Anna", "lastName": "Smith"},
        {"firstName": "Peter", "lastName": "Jones"},
        ],
    "owners": [
        {"firstName": "Jack", "lastName": "Petter"},
        {"firstName": "Jessy", "lastName": "Petter"}
        ]
    
}

# Print out the last name of the second employee
print("The last name of the second employee is: ", d["employees"][1]["lastName"])
print("The first and last name of the first owner is: ", d["owners"][0]["firstName"], d["owners"][0]["lastName"])
print(d.get("Alexandra"))
