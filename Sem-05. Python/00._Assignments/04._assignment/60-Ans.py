#-----------------------------------------------------------#
#------------Q60. Username Generator Validation-------------#
#-----------------------------------------------------------#
name = input("Enter full name: ")

parts = name.split(" ")
username = parts[0] + "." + parts[2]

if "." in username:
    print("Valid Username Format")
else:
    print("Invalid Username Format")