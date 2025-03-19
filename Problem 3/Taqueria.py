
# This is a dictionary of all the items available
Food = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

cost = 0 # When in situations where you are constantly adding new items, always set up the variable to be zero initially

while True: # Setting up the loop
    try:
        order = input("What would you like? ").title() # Recall that 'title' auto caps the first letters of users input

        if order in Food:  # 'order' is just a variable we created
            cost += Food[order] # if it so happens that the input is in the dict, the cost associated with food will add
            print(f"Current cost: $"'{:.2f}'.format(cost))

# NOTE we tried using a function called 'round' but .00 is just .0 and the check wont work
# It should be noted that this alone will ensure the loop continues even if the input is not in the dict


    except EOFError: # Raised when the input() function hits an end-of-file condition (EOF) without reading any data (e.g ctrl d)
        print()
        break # This will break the whole loop and thus the final cost will be printed by using the line below

print(f"Total cost: $"'{:.2f}'.format(cost))


