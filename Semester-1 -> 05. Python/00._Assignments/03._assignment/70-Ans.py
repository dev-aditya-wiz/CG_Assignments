#----------------------------#
#---------Input Code---------#
#----------------------------#
full_name = input()
names = full_name.split()
first_name = names[0]
last_name = names[-1]
first_part = first_name[:3].upper()
last_part = last_name[-3:].lower()
reversed_name = full_name[::-1]
print(f"Original: {full_name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"First Name (Upper Part): {first_part}")
print(f"Last Name (Lower Part): {last_part}")
print(f"Full Name Reversed: {reversed_name}")