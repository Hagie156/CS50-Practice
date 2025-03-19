def main():
    # Promt user to write anything
    prompt = input("Write anything:")
    # Call the shorten function and print the result
    print(shorten(prompt))


def shorten(word):
    result = ""
    for letter in word:
        if letter not in ["a",  "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            result += letter
    return result

if __name__ == "__main__":
    main()


