# Get consumer to write their fruit

fruit = input("Item:").strip().lower() #Recall that strip removes unwanted spaces before the first word and after the last word


# Create a dictionary with keys values name and calories
fruits = [
    {"name": "apple" , "calories" : "130"},
    {"name" : "avocado" , "calories" : "50"},
    {"name": "banana" , "calories" : "110"} ,
    {"name": "cantaloupe" , "calories" : "50"} ,
    {"name": "grapefruit" , "calories" : "60"} ,
    {"name": "grapes" , "calories" : "90"} ,
    {"name": "honeydew Melon" , "calories" : "50"} ,
    {"name": "kiwifruit" , "calories" : "90"} ,
    {"name": "lemon" , "calories" : "15"} ,
    {"name": "lime" , "calories" : "20"} ,
    {"name": "nectarine" , "calories" : "60"} ,
    {"name": "orange" , "calories" : "80"} ,
    {"name": "peach" , "calories" : "60"} ,
    {"name": "pear" , "calories" : "100"} ,
    {"name": "pineapple" , "calories" : "50"} ,
    {"name": "plums" , "calories" : "70"} ,
    {"name": "strawberries" , "calories" : "50"} ,
    {"name": "sweet cherries" , "calories" : "100"} ,
    {"name": "tangerine" , "calories" : "50"} ,
    {"name": "watermelon" , "calories" : "80"} ,
]

located = False # This is a variable to helps us track whether an inputed fruit has been selected or not. (We set it to false early as at this point we haven't started looking for the fruit yet)

for item in fruits :     #This loop we created iterates over each dictionary in our 'fruits' list.
    if item["name"] == fruit :
        print(f"{item['calories']}")  # Remember to not use double quotes twice
        located = True
        break # Recall that breaks are used to end the loop early. E.g if the fruit was avocado, we can just break right there and then

if not located: # This means that 'if not' as in no fruit is in the list, use 'located' which we set to false 
    print("")







