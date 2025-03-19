import emoji # This imports the 'emoji' module which allows us to use its specific functions

prompt = input("Input: ") #This is to prompt the user. We will assume they know how to correctly write the input withought any mistakes



# The 'language = alias' parameter helps to covert different ways of the input (e.g :thumbs_up: or :thumbsup:)
convert = emoji.emojize(prompt , language = "alias")

print("Output:" , convert)
