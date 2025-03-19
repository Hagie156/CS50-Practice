def convert(face):
    # We will create a function called convert that will change the faces to what we want
    face = face.replace(":)","🙂")
    face = face.replace(":(","🙁")
    # The return will change the specific input to what we want
    return face

def main():
    face = input("Give me either a smiley face in the form of ':)' or a sad face in the form ':(' ")
    # Creating this variable will ensure we get the converted version of the input
    response = convert(face)
    print(response)

main()


