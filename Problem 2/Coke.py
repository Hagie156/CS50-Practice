# First establish the original price
price = 50

# Here we are telling the user the original price.
# We could have also written ' print(f"Amount due: {price}") '
print("Amount Due: 50")

# Here we will establish our loop. We are saying that while the price is still above zero, the user wil get a
#prompt telling them to put money which is insert coin
while price > 0:
     money = int(input("Insert Coin:"))

# We use lots of 'if' here. The first one is to make sure the correct numbers are given
     if money == 25 or money == 10 or money == 5:
# THIS IS INTERESTING. This makes sure the 'price' will always be subtracted from the user input
          price -= money

          if price > 0:
               print(f"Amount Due: {price}") # or we can write print('Amount due:', price)

          else:
               print(f"Change Owed: {-price}")

# This bottom line work with the first if assuming the user does not give a valid number in which no new
#change will occur
     else:
        print(f"Amount Due: {price}")


