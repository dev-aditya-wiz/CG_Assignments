#-----------------------------------------------------------#
#------------Q29. College Admission Eligibility-------------#
#-----------------------------------------------------------#
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))

if marks >= 60 and attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")