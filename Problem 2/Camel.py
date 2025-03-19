# Get users input
camel_case = input("Give me an example of a camel case:")


# Create a loop that will go through each letter in the users response. (We will call it 'char')
# The 'char' is like when we do definitions. It is the expected input from the user
# The 'in' will loop and look at every character in the string that the user gave


for char in camel_case:

# Next we should be able to detect when a capital letter has been used
# In the situation where a capital letter has been used, 'is upper' will know which characters are capital

    if char.isupper():
# When it detects a capital letter in the loop, it will first print the underscore, convert that specific letter
#and then continue the process.

# The ' end="" ' is interesting. It will ensure the prints are in a singular line and not below eachother. This
#means we are printing every single character and then joining them together.
        print("_" + char.lower(), end="")

# This will just move on the printing process when there is a lowercase in the input
    else:
        print(char, end="")

# This final print is to make sure that the line in the terminal will be on a new line
print()


