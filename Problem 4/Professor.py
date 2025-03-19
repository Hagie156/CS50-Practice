# For context, This is a reference to the toy "Little Professor" which challenges your addition skills


# First lets import the modules that we will use

import random # This module helps in selecting random items


def main():
    level = get_level() # We created the function to prompt a difficulty of either 1, 2 or 3

    score = start_game(level) #This will start the game at the chosen level

    print("Score: ", score)


def get_level():
    while True: # This is to set a loop until we get a valid number for the level
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                break # Breaks the loop if user put a valid level number

        except ValueError:
            pass
    return level #This will return the valid level the user requested






def generate_integer(level): #Now we need to establish cases depending on the level they selected

    if level == 1: # This is the easy level with only single digit calculations
        a = random.randint(0,9)
        b = random.randint(0,9)

    elif level == 2: # This is the medium level with only double digit calculations
        a = random.randint(10,99)
        b = random.randint(10,99)

    else: # Recall how 'if' statements work. its obvious that case 3 can just be registed as 'else' as that is the only option.
        a = random.randint(100,999)
        b = random.randint(100,999)

    return a,b



# Establish how rounds will work.
def start_round(a, b):
    tries = 1 # This is to initialize the number of tries the user gets each round
    while tries <= 3: # This allows the user to try at least three times
        try:
            answer = int(input(f"{a} + {b} = "))
            if answer == (a + b): # This checks if user input has put the correct answer in
                return True
            else:
                tries += 1
                print("EEE")
        except:
            tries += 1
            print("EEE")

    print(f"{a} + {b} = {a + b}") # This will show the correct answer only if all 3 tries have been used
    return False




# Establish how game will work

def start_game(level):
    round_number = 1
    score = 0

    while round_number <= 10:
        a, b = generate_integer(level) #The values of a and b will generate dependong on the level selected
        response = start_round(a , b) #This runs a single round
        if response == True:
            score += 1
        round_number +=1
    return score




if __name__ == "__main__":
    main()



















