'''Python program
student name: Eugenie Tsafack
date: 10/24/2024
file name: sales.py
Instructions: Write a code using functions that will add items in your grocery cart and return total in a receipt text .

'''
# define list of order
order= {'tomato': 30, 'thyme': 4.50, 'garlic': 7.5, 'rice': 10, 'onions': 4, 'fish': 9.99 }

# Define a function

def order_calculator():
    
    # loop into orders and create a new order
    new_order= {}
    
    total_price = 0
    
    for product_name, price  in order.items():
        new_order[product_name] = price # adding the product and it price to a nwe_order
        total_price += price
        print(f"{product_name}: {price}")
        
        
        
    print(f"total price: {total_price}")
        
# calling a function
order_calculator()