# First lets import the modules that we will use

import random # This module helps in selecting random items



#Prompt user to give a level but needs to be an integer and between 1 and 100

while True: # This is to set a loop until we get a valid number
    try:
        number = int(input(" Select your level between 1 & 100: "))
        if 1 <= number <= 100:
            break

    except ValueError:
        pass 





# Now after level has been established, we should set the random number

value = random.randint(1 , number)


# Now we get the user to play a guessing game

while True: # This is to set a loop until we get a valid number
    try:
        guess = int(input("Guess: "))

        if guess < value:
            print("Too small!")
            pass

        if guess > value:
            print("Too Large!")
            pass

        if guess == value:
            print("Just right!")
            break

    except ValueError:
        pass








