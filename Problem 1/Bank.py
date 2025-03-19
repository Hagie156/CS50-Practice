# This is a Seinfeld reference. The bank will give you a cerytain amount of money depending on how you greet the prompt


greeting = input("Greetings!")
#This next line ensures case-insensitivity is fixed
adjusted = greeting.strip().lower()


if "hello" == adjusted:
    print('As you said "hello" you will receive $0')
    # For the next line, you canalso write adjusted[0] == "h"
elif adjusted.startswith('h'):
    print('Your greeting started with the letter "h" so you will only receive $20")
else:
    print('Fair play here is $100')
