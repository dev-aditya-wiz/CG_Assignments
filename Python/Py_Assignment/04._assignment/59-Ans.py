#--------------------------------------------------------#
#---------------Q59. Email Domain Checker----------------#
#--------------------------------------------------------#
email = input("Enter email: ")

parts = email.split("@")
domain = parts[1]

if domain == "gmail.com":
    print("Gmail User")
else:
    print("Other Email Provider")