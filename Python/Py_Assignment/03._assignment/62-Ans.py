#----------------------------#
#-----Username Generator-----#
#----------------------------#
full_name = input()
names = full_name.split()
first_name = names[0]
last_name = names[2]
username = first_name.lower() + "." + last_name.lower()
print(username)