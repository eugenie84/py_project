'''Python program, 
Name: Eugenie Tsafack
date: 11/07/2024
file name: multiplier.py
Instructions: Write a function called multiply_even_number. This function accepts a list of numbers and returns the product of 
all even number in the list.
Please have exceptions handled and docstring.

'''

from math import prod

# define a function
def multiply_even_numbers(numbers):
    """This function accepts a list of numbers and returns the product of 
    all even numbers in the list.

    Args:
        numbers (list of int): a list of numbers 

    Returns:
        int: product of all even number in the list, or 1 if no even numbers are found.
    """
    try:
        even_numbers = [number for number in numbers if number % 2 == 0] # collect all the even number
        if not even_numbers:
            return 1
        result = prod(even_numbers)
        return f"The product of all even numbers in the list is {result}"
    except TypeError as e:
        print(f"Error: {e} - Please ensure all elements in the list are integers.")
    

# calculate the product of even numbers in the list
Numbers = [8, 9, 11, 20, 32, 101, 100]

even_product = multiply_even_numbers(Numbers)  
print(f"the product of even number in the list is {even_product}")  
        
    