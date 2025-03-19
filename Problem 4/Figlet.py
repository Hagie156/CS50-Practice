# First lets import the modules that we will use


import sys # Recall that this will allow us hold the command-line arguments passed to the script
import random # This module helps in selecting random items
from pyfiglet import Figlet #This is a class from the pyfiglet library, used to create ASCII art from text using different fonts.

figlet = Figlet()


#Here we need to establish cases for what the user may input.


if len(sys.argv) == 1: #This is case 1 which is if the user does not specify a font
    random_font = True

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts(): #This is case 2 which is if the user does specify a font
    random_font = False

else: #This is case 3 where the user doesn't follow the structure intended
    print("Invalid usage")
    sys.exit(1)

prompt = input("Input: ")

figlet.getFonts()

if random_font:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
    print("Output:")
    print(figlet.renderText(prompt))

else:
    figlet.setFont(font=sys.argv[2])
    print("Output:")
    print(figlet.renderText(prompt))
