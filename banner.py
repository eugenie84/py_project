# Building a banner that display a text message using a # symbol

import pyfiglet
from colorama import Fore

# define a variable user_name
user_name = pyfiglet.figlet_format ("Eugenie", font = "big")

# define a rectangle using #symbol
banner1 = "#" * 100
banner3 = "\v #                                                                                                   #" * 7


# define a message
banner2 = pyfiglet.figlet_format ("WELCOME TO STREET FIGHTER :", font = "big")

# Combine everything
banner = f"{banner1}{banner3}\n{banner2}{user_name}{banner3}\n{banner1}"

# print the banner
print (banner)
