#---------------------------------------------------------#
#------------Q39. Exam Result with Attendance-------------#
#---------------------------------------------------------#
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))

if attendance >= 75:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible Due to Attendance")