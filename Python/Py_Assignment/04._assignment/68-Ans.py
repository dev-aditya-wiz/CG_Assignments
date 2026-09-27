#------------------------------------------------------#
#------------Q68. College Admission System-------------#
#------------------------------------------------------#
score = int(input("Enter entrance score: "))
percentage = int(input("Enter 12th percentage: "))
category = input("Enter category: ")

match category:
    case "general":
        if score >= 80 and percentage >= 75:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")

    case "obc":
        if score >= 70 and percentage >= 70:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")

    case "sc":
        if score >= 60 and percentage >= 60:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")

    case _:
        print("Admission Not Eligible")