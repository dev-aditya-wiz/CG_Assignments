#---------------------------------------------------------#
#------------Q74. match-case and Default Case-------------#
#---------------------------------------------------------#
# INPUT:
choice = 1
match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Delete")
    case _:
        print("Invalid Choice")
# OUTPUT: Add


# INPUT:
choice = 3
match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Delete")
    case _:
        print("Invalid Choice")
# OUTPUT: Delete


# INPUT:
choice = 5
match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Delete")
    case _:
        print("Invalid Choice")
# OUTPUT: Invalid Choice
