#----------------------------#
#---------Input Code---------#
#----------------------------#
email = input()
username, domain = email.split("@")
print(f"Username: {username}")
print(f"Domain: {domain}")