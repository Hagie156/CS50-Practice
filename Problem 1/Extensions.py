prompt = input("Give me a file with a suffix after:")

#This will seperate the input
separation = prompt.split(".")

#The -1 ensures the last word from the separation is selected. It will still work even if only one word was used in the input
second_word = separation[-1]
#This line ensures case-insensitivity is not an issue
adjusted = second_word.lower().strip()

if "gif" == adjusted :
    print("image/gif")

elif "jpg" == adjusted or "jpeg" == adjusted:
    print("image/jpeg")

elif "png" == adjusted:
    print("image/png")

elif "pdf" == adjusted:
    print("application/pdf")

elif "txt" == adjusted:
    print("text/plain")

elif "zip" == adjusted:
    print("application/zip")

else:
    print("application/octet-stream")
