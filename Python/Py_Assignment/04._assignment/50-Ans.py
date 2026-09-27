#-----------------------------------------------------------#
#---------------------Q50. Basic Menu-----------------------#
#-----------------------------------------------------------#
choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Update")
    case 4:
        print("Delete")
    case _:
        print("Invalid Choice")