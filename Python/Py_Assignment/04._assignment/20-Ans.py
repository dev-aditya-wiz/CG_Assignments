#-----------------------------------------------------------#
#------------------Q20. Temperature Category----------------#
#-----------------------------------------------------------#
temperature = int(input("Enter temperature: "))

if temperature >= 40:
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Warm")
else:
    print("Cold")