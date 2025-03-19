# Create a dictionary containing all the months
months = {
    "January": 1 ,
    "February" : 2 ,
    "March" : 3 ,
    "April" : 4 ,
    "May" : 5 ,
    "June" : 6 ,
    "July" : 7 ,
    "August" : 8 ,
    "September" : 9 ,
    "October" : 10 ,
    "November" : 11 ,
    "December" : 12 ,
}

while True: #Create a loop that lasts forever until a valid answer is provided
    date = input("Date: ").strip() # Prompt user to give a date


#This scenario is if the user writes the date with '/' seperations
    try:
        (month, day, year) = date.split("/")
        if 1<= int(month) <= 12  and 1<= int(day) <= 31:
            print(f"{int(year):04d}-{int(month):02d}-{int(day):02d}")
            break
#Note  with the '0xd' the 'x' represents the number of digits you want and there will be enough zero padding


#This scenario is if the user writes uses spaces for seperations and writes the month name
    except ValueError: # 'Value error' is when you request a string like 'abc' within 'int()' which does not work
        try:
            parts = date.split()
            if len(parts) == 3:
                (month_name, day, year) = parts
                if not day.endswith(","): # this is for a specific scenario such that they do not include a ','
                    continue # Ironically 'continue' just skips the code and does a reprompt
                day = day.replace("," , "")
                month_name = month_name.title()
                if month_name in months and 1<= int(day) <= 31:
                    adjusted_month = months[month_name]
                    print(f"{int(year):04d}-{int(adjusted_month):02d}-{int(day):02d}")
                    break

#This scenario is if the user writes something that is just not valid at all. A reprompt will occur
        except:
            pass




