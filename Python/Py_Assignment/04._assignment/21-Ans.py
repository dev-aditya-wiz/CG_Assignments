#-----------------------------------------------------------#
#--------------------Q21. Traffic Signal--------------------#
#-----------------------------------------------------------#
color = input("Enter signal color: ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("Invalid Signal")