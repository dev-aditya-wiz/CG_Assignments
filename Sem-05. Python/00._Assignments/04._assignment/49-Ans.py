#------------------------------------------------------#
#------------Q49. Travel Ticket Validation-------------#
#------------------------------------------------------#
age = int(input("Enter age: "))
ticket = input("Enter ticket type: ")

if age < 5:
    print("Free Travel")
elif age >= 60:
    print("Senior Passenger")
else:
    if ticket == "AC":
        print("AC Ticket")
    elif ticket == "Sleeper":
        print("Sleeper Ticket")
    else:
        print("Invalid Ticket Type")