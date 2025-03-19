greeting = input("Greetings!")
#This next line ensures case-insensitivity is fixed
adjusted = greeting.strip().lower()


if "hello" == adjusted:
    print("$0")
    # For the next line, you canalso write adjusted[0] == "h"
elif adjusted.startswith('h'):
    print("$20")
else:
    print("$100")
