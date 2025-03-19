def main():
    #First ask user what the current time is
    response = input("What is the time? ")
    # Next we will use the convert function that we defined at the bottom
    time = convert(response) #What we want is that the time will store the responded time in the format we need
    # We want breakfast to be between 7:00 and 8:00
    if 7.0 <= time <= 8.0:
        print("breakfast time") #Recall that indentations are very important
    # We want breakfast to be between 12:00 and 13:00
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    # We want breakfast to be between 18:00 and 19:00
    elif 18.0 <= time <= 19.0:
        print("dinner time")



    #Remember that t is what we will assume that the "response" will be in this local definition
def convert(t):
    #First we should split the time obtained to hours and minutes
    separated_time = t.split(":")
    hours = float(separated_time[0])
    minutes = float(separated_time[1]) / 60
    # This return function should make "convert(response)" in the time format that we require
    return hours + minutes



if __name__ == "__main__":  #I dont understand this part but they said they will explain this in the future
    main()
