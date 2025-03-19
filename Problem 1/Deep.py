#This is to get the users' response
response = input("What is the answer to the great question of life, the universe and everything?")
#This is to ensure any mistakes or accidents will get sorted such as extra spaces or unnecessary capital letters 
adjusted = response.strip().lower()


if adjusted == "42" or adjusted == "forty-two" or adjusted == "forty two":
    print("Yes")
else:
    print("No")
