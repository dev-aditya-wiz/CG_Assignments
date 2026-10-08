#---------------------------------------------------#
#------------Q58. Student ID Validation-------------#
#---------------------------------------------------#
student_id = input("Enter student ID: ")

parts = student_id.split("-")
branch = parts[2]

if branch == "CSE":
    print("CSE Student")
else:
    print("Non-CSE Student")