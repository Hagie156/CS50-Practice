
#Get the user to provide a mass
mass =int(input("Give me a mass in kg "))


a = 3
# For value of b, the ** is a way of saying power
b = 10**8
c = a*b
Speed = c*c

Energy = mass*Speed

print("In terms of energy, the provided mass would be",Energy , "Joules")
