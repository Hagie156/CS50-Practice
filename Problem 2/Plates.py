def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
# “All vanity plates must start with at least two letters and contain maximum 6 characters."
    if len(s) < 2 or len(s) > 6:    # 'len' looks at how long the string is
        return False



# Question states that: "All vanity plates must start with at least two letters".


# The ' [0 : 2] ' way is to isolate the first two elements of the string. The zero is before the first character and the 2 is after the second characeter.
    if not s[0 : 2].isalpha():   # 'isalpha' litterally checks is there are letters contained and
        return False



# This code below ensures that the input consists of only letters and numbers (No punctuations or spaces)
    if not s.isalnum():
        return False
    

    if not valid_position(s):
        return False

    return True



def valid_position(v):
# To find the first time a digit shows in the input, the 'for' loop will associate a number to the input's letters and numbers
    for i in range(len(v)):
        if v[i].isdigit():

# Question states that: "The first number used cannot be a ‘0’.
            if v[i] == "0":
                return False

# Question states that: "“Numbers cannot be used in the middle of a plate; they must come at the end."
            for num in range(i, len(v)):  # This will iterate numbers from the first present number to the end of the string
                if not v[num].isdigit():
                    return False
            break # The break will exit out of the loop. It also ensures the function only looks into the range we specified and not any other character
    return True


main()
