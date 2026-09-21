#---------------------------------#
#---Email Analyzer + Membership---#
#---------------------------------#
email = input()
print(f"@ Present: {'@' in email}")
parts = email.split("@")
username = parts[0]
domain = parts[1]
print(f"Username: {username}")
print(f"Domain: {domain}")