'''Python program
name: Eugenie Tsafack
date: 11/07/2024
file name: sales2.py
Instructions: Write a code using functions that will add items in your grocery cart and return total in a receipt text .

'''
# define list of order
order= {'tomato': 30, 'thyme': 4.50, 'garlic': 7.5, 'rice': 10, 'onions': 4, 'fish': 9.99 }

# define a function to add items to a cart and calculate the total
def add_item (cart_item):
    """This function to add items to a cart and calculate the total 

    Args:
        cart_item (str): name of items in the cart

    Returns:
        float: the total price of the items ordering
    """
    total_item = sum(cart_item.values())
    return total_item

# define a function to generate a receipt
def generate_receipt(cart_items, total):
    """This function will generate a receipt and add a total price of your order

    Args:
        cart_items (str): a name of items in the cart
        total (float): the total price of the items ordering
    """
    try:
        with open ('receipt.txt', 'w') as file:
            file.write("-----Grocery receipt----- \n")
            for item, price in cart_items.items():
                file.write(f"{item.capitalize()}: ${price:.2f}\n")
            file.write("--------------------\n")
            file.write(f"Total: ${total:.2f}\n")
            file.write("--------------------\n")
        print('receipt,txt')
    except FileNotFoundError as error:
        print(f"Sorry, we cannot access the file: {error}")
        
# calling the functions
total = add_item(order)
generate_receipt(order, total)
        