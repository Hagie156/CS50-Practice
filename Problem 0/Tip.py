def main():
#We create a function called dollars_to_float and a function called percent_to_float
    dollars= dollars_to_float(input("How much was the meal? "))
    percentage = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percentage
    print(f"Leave ${tip:.2f}")

# In this definition, the (d) is a stand in for the input the user will provide. It is not a variable.
def dollars_to_float(d):
# What this is doing is that any input will be stripped of $
    required_dollars = d.strip("$")
# We can still tamper with our definition in the return section. We ensured that the number will remain how it is with float
    return float(required_dollars)

# In this definition, the (p) is an arbitrary value for anything that the user might write.
def percent_to_float(p):
    No_percentage = p.strip("%")
    required_percentage = float(No_percentage) /100
    return required_percentage

main()
