#While the Probelm is called fuel, this simply converts fractions into percentages

while True: #This sets up a loop
    try:
        fraction = input("Fraction:").split("/") # We are splitting the numerator and denominator

        # These two lines are to ensure that the input we obtain are converted from a string to numerical values
        x = int(fraction[0])
        y = int(fraction[1])
        f = x / y

        if f <= 1: # This code is to ensure no improper fractions
            break

    except ValueError: #This is for the case where the strings cannot be converted to integers (e.g using words like cat)
        pass
    except ZeroDivisionError: #This is for the case we have x= 0 which cannot be solved
        pass

percentage = f * 100
rounded = round(percentage) # We do not want any decimal places

if percentage >= 99:
    print("F")
elif percentage <= 1:
    print("E")
else:
    print(f"{rounded}%")
