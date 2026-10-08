#-------------------------------------------------#
#------------Q47. Bus Ticket Category-------------#
#-------------------------------------------------#
age = int(input("Enter age: "))
distance = int(input("Enter distance: "))

if age < 5:
    print("Free")
elif age >= 60:
    print("Senior")
else:
    if distance <= 10:
        print("Regular - Short Distance")
    else:
        print("Regular - Long Distance")