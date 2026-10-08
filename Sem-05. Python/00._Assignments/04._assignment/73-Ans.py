#------------------------------------------------------#
#------------Q73. Nested if Execution Flow-------------#
#------------------------------------------------------#
# INPUT:
age = 20
has_id = False

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Underage")
# OUTPUT:
# ID Required

# INPUT:
age = 16
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Underage")
# OUTPUT:
# Underage