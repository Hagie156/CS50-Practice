# First lets import the modules that we will use

import inflect
p = inflect.engine() # In the document it says this will join words into a list (meaning it will do automatic ',' and 'and' for us)



names = [] # Create an empty list that will be filled from user input
while True:
    try:
        Input = input("Name: ").title().strip() # Prompt user to provide the names
        names.append(Input) # 'append' automatically adds the next input onto the list

    except EOFError: # Raised when the input() function hits an end-of-file condition (EOF) without reading any data (e.g ctrl d)
        print()
        break

print(f"Adieu, adieu, to", p.join(names))

