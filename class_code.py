# write a program that writes the element of a list to the file

#define la list
list = [1, 2, 3, 4, 5]

def transform(list_data, file_name):
    with open('list.txt', 'w') as file:
        for item in list_data:
            file.write(str(item) + "\n")
        
#calling a function
list_data= list
file_name= 'list.txt'

transform(list_data, file_name)