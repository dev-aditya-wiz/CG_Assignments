#-----------------------------------------------------------#
#-------------Q22. Electricity Usage Category---------------#
#-----------------------------------------------------------#
units = int(input("Enter units: "))

if units <= 100:
    print("Low Usage")
elif units <= 300:
    print("Medium Usage")
elif units <= 500:
    print("High Usage")
else:
    print("Very High Usage")