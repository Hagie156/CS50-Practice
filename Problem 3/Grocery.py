
shopping_list = {} # Create an empty dict that will be filled from user input

while True: #Create loop that lasts forever until user stops it
    try:
        need = input().upper().strip() # Prompt user to list what they need

        if need in shopping_list:
            shopping_list[need] += 1 # For repeated items (keys) , it will increase 'value' by 1
        else:
            shopping_list[need] = 1 #For new items (keys), it will generate a 'value' of 1 of those

    except EOFError: # Raised when the input() function hits an end-of-file condition (EOF) without reading any data (e.g ctrl d)
        for item in sorted(shopping_list.keys()): # '.keys() is a function that only looks into the key values in a dict
            print(shopping_list[item], item)
        break




