maths = input("Write an arithmetic equation:")


# Make 4 if statements each respresenting a math symbol.
if "+" in maths:
# The split allows the speration of numbers so that we can single them out
    broken_maths = maths.split("+")
    answer = number_1 = float(broken_maths[0]) + float(broken_maths[1])
elif "-" in maths:
    broken_maths = maths.split("-")
    answer = number_1 = float(broken_maths[0]) - float(broken_maths[1])
elif "*" in maths:
    broken_maths = maths.split("*")
    answer = number_1 = float(broken_maths[0]) * float(broken_maths[1])
else:
    broken_maths = maths.split("/")
    answer = number_1 = float(broken_maths[0]) / float(broken_maths[1])

print(answer)
