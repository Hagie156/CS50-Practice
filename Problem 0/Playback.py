#Get user to write a sentence of their choice
sentence = input("Give me a sentence and I will break it down slowly for you:")

# Create a way to split the words in the sentence by using method split
sentence = sentence.split()

#Join the words the the "join" method
slow = "...".join(sentence)

#Print out the sentence with pauses inbetween words

print(slow)
